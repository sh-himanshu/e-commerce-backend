from .. import V1


@V1.get("/")
async def read_items():
    return {"ok": True}
