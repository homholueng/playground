package main

import (
	"io"
	"log"
)

type OneOffReaderWriter struct {
	p []byte
	n int
}

func (rw *OneOffReaderWriter) Read(p []byte) (int, error) {
	rw.p = make([]byte, len(p))
	copy(p, rw.p)
	return rw.n, nil
}

func (rw *OneOffReaderWriter) Write(p []byte) (int, error) {
	n := copy(rw.p, p)
	rw.n = n
	return n, nil
}

func LimitReader(r io.Reader, n int64) io.Reader {

	if n == 0 {
		return &OneOffReaderWriter{}
	}

	p := make([]byte, n)
	rw := OneOffReaderWriter{}
	_, err := r.Read(p)

	if err != nil {
		log.Fatalf("read from r error: %v", nil)
		return nil
	}

	rw.Write(p)
	return &rw
}
