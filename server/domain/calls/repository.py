from core.db.db import Database


class CallsRepository:

    def __init__(self, db: Database):
        self.db = db

    async def get_calls(self):
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
