import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

from .config import QUEUE_MAXSIZE
from .processor import process_message

message_queue: asyncio.Queue[dict] | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global message_queue
    message_queue = asyncio.Queue[dict](maxsize=QUEUE_MAXSIZE)

    consumer_task = asyncio.create_task(consumer(message_queue))

    yield

    consumer_task.cancel()
    try:
        await consumer_task
    except asyncio.CancelledError:
        pass


app = FastAPI(lifespan=lifespan)


async def consumer(queue: asyncio.Queue[dict]) -> None:
    while True:
        body = await queue.get()
        try:
            await asyncio.to_thread(process_message, body)
        finally:
            queue.task_done()


@app.post("/message")
async def put_message(body: dict) -> Response:
    global message_queue

    try:
        message_queue.put_nowait(body)
    except asyncio.QueueFull:
        raise HTTPException(status_code=503, detail="Queue is full")

    return Response(status_code=200)


def run():
    import uvicorn

    uvicorn.run(
        "claude_speak.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="warning",
    )


if __name__ == "__main__":
    run()
