from pathlib import Path

import uvicorn

from . import config


def main():
    uvicorn.run(
        f"{Path(__file__).parent.name}:app",
        host=config.HOST,
        port=config.PORT,
        log_level="info",
        reload=True,
    )
