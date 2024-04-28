from fastapi import FastAPI

from test_deploy_koyeb.adapters.inbound.rest.v1.controllers.ping import router as ping_router

from test_deploy_koyeb.adapters.settings import settings

def get_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)

    application.include_router(ping_router)

    return application

app = get_application()