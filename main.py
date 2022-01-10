from routers._in_routers import *
import routers._in_routers

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    routers._in_routers.router,
    prefix="/api",                
    tags=["API"],
    responses={418: {"description": "I'm teapot"}},
)

