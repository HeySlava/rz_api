import views
import uvicorn

from fastapi import FastAPI
from setting import settings
from data import db_session


app = FastAPI()


def routes_configure():
    app.include_router(views.router)


def configure_database():
    db_session.global_init(settings.conn_str, debug=settings.debug)


def configure():
    routes_configure()
    configure_database()


def main():
    configure()
    uvicorn.run(app, port=settings.port)


if __name__ == '__main__':
    main()
else:
    configure()
