from fastapi import FastAPI
# from db import pg14

engine = FastAPI()

@engine.get(path="/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}

@engine.get(path="/items/{item_id}")
async def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}

def run() -> None:
    import uvicorn
    uvicorn.run(app=engine, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run()