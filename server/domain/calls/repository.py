from typing import List

from core.db.db import Database
from core.db.record import Record


class CallsRepository:

    def __init__(self, db: Database):
        self.db = db

    async def get_calls(self) -> List[Record]:
        return await self.db.fetch(
            '''
            SELECT 
                id,
                username,
                first_name,
                last_name,
                patronymic
            FROM public.users
            LIMIT 10
            '''
        )

    async def get_calls_count(self) -> int:
        return await self.db.fetchval(
            '''
            SELECT COUNT(*)
            FROM public.users
            '''
        )
