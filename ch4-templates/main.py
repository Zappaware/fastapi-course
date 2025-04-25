import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles
from views import account, home, packages

import fastapi

app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host="127.0.0.1", port=8000)


def configure():
    configure_routes()
    configure_templates()


def configure_routes():
    # Include the routers from the views module
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


def configure_templates():
    # Initialize FastAPI Chameleon with the template directory
    fastapi_chameleon.global_init("templates")


if __name__ == "__main__":
    # Run the FastAPI app with Uvicorn server
    main()
else:
    configure()
