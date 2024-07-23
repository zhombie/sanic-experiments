import asyncpg


class Record(asyncpg.Record):

    def to_dict(self) -> dict:
        return dict(self)
