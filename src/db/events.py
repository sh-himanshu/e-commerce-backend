from pathlib import Path

from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3", modules={"models": ["src.db.models"]}
    )
    # Generate the schema once
    if not Path("db.sqlite3").is_file():
        await Tortoise.generate_schemas()


async def exit_db():
    await Tortoise.close_connections()
