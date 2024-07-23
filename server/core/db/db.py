import asyncio
import traceback
from typing import Optional

import asyncpg
from asyncpg import Pool
from orjson import orjson


class Database:
    pool: Optional[Pool] = None

    @classmethod
    async def init(cls, connection):
        for t in ['json', 'jsonb']:
            await connection.set_type_codec(
                t,
                encoder=orjson.dumps,
                decoder=orjson.loads,
                schema='pg_catalog'
            )

    async def connect(
        self,

        host: str,
        port: int,
        user: str,
        password: str,
        database: str,

        command_timeout: Optional[int] = None,
        timeout: int = 10,

        min_size: int = 1,
        max_size: int = 1,

        init=None,
    ) -> bool:
        if self.pool is None:
            self.pool = await asyncpg.create_pool(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,

                command_timeout=command_timeout,
                timeout=timeout,

                min_size=min_size,
                max_size=max_size,

                init=self.init
            )
            return True
        return False

    async def disconnect(self) -> bool:
        if self.pool is not None:
            try:
                await asyncio.wait_for(self.pool.close(), 10)
            except (Exception,):
                traceback.print_exc()
            else:
                self.pool.terminate()
            finally:
                self.pool = None
            return True
        return False


db = Database()
