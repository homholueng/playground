import redis
import time

TIMES = 10000

def bench(func, desc):
    start = time.time()
    func()
    print('{desc} {cost} milliseconds'.format(desc=desc, cost=time.time() - start)) 

def without_pipeling():
    r = redis.Redis(host='localhost', port=6379)
    for _ in range(TIMES):
        r.ping()

def with_pipelining():
    r = redis.Redis(host='localhost', port=6379)
    with r.pipeline(transaction=False) as p:
        for _ in range(TIMES):
            p.ping()

if __name__ == '__main__':
    bench(without_pipeling, 'without_pipeling')
    bench(with_pipelining, 'with_pipelining')