import uvicorn
from fastapi import FastAPI

from src.api.health_controller import router as health_router
from src.di_container import DependencyContainer

app = FastAPI(title="RAG Confluence", version="0.1.0")

container = DependencyContainer()
container.wire(modules=[__name__])

app.include_router(health_router)

def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
