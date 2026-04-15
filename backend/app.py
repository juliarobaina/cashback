from fastapi import FastAPI
import routes
from fastapi.middleware.cors import CORSMiddleware
from settings import host


app = FastAPI(title="Cashback")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routes.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=f"{host.HOST_IP}", port=host.PORT)
