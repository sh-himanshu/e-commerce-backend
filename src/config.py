from os import getenv


PORT = int(getenv("PORT", 3000))
HOST = getenv("HOST", "0.0.0.0" if getenv("DYNO") else "localhost")
