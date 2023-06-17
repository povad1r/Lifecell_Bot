import asyncpg


class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.pool = None

    async def bd_start(self):
        self.pool = await asyncpg.create_pool(
            database=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

        async with self.pool.acquire() as conn:
            await conn.execute("CREATE TABLE IF NOT EXISTS user_info("
                               "user_id INTEGER PRIMARY KEY UNIQUE NOT NULL, "
                               "datetime TEXT)"
                               )

    async def sql_get_user_id(self, user_id):
        async with self.pool.acquire() as conn:
            result = await conn.fetchval('SELECT user_id FROM user_info WHERE user_id = $1', user_id)
            return result

    async def sql_create_user(self, user_id, datetime):
        async with self.pool.acquire() as conn:
            existing_user = await self.sql_get_user_id(user_id)
            if not existing_user:
                await conn.execute(
                    "INSERT INTO user_info (user_id, datetime) VALUES ($1, $2)",
                    user_id, datetime
                )
                return True

        return False


