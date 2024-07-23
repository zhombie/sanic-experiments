from typing import Optional

from core.db.db import Database
from domain.calls.repository import CallsRepository


class DI:
    _db: Optional[Database] = None

    _calls_repository: Optional[CallsRepository] = None

    @property
    def db(self) -> Database:
        if not self._db:
            self._db = Database()
        return self._db

    @property
    def calls_repository(self) -> CallsRepository:
        if not self._calls_repository:
            self._calls_repository = CallsRepository(self.db)
        return self._calls_repository

    def destroy(self):
        self._db = None
        self._calls_repository = None


di = DI()
