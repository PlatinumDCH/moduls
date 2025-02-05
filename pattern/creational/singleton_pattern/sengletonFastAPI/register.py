from fastapi import FastAPI, APIRouter
from pattern.creational.singleton_pattern.sengletonFastAPI.routes import router as import_router

class APIRouterManager:
    _routes:list = []

    @classmethod
    def register(cls, router: APIRouter):
        cls._routes.append(router)
    
    @classmethod
    def attach(cls, app: FastAPI):
        for router in cls._routes:
            app.include_router(router)



APIRouterManager.register(import_router)



