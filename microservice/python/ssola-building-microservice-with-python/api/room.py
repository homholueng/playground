import uuid

from flask_injector import inject

from services.elasticsearch import ElasticsearchIndex


class Room(object):
    @inject(indexer=ElasticsearchIndex)
    def post(self, indexer: ElasticsearchIndex, room: dict) -> dict:
        if indexer.exists_by_url(room['url']):
            return room, 409

        room['id'] = str(uuid.uuid4())

        if not indexer.index(room):
            return {'error': 'Room not saved'}, 400

        return room, 201


class_instance = Room()
