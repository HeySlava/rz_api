from fastapi import FastAPI
import views
import uvicorn
from settings import settings


app = FastAPI()


def routes_configure():
    app.include_router(views.router)


def configure():
    routes_configure()


def main():
    configure()
    uvicorn.run(app, port=settings.port)


if __name__ == '__main__':
    main()
else:
    configure()
