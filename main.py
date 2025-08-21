from fastapi import FastAPI
import uvicorn
from routers.user_info import router

app = FastAPI()

app.include_router(router,prefix="/skillwell/v1/logapi", tags=["skillwell"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)