from app.routers import auth_router, student_router, admin_router
from fastapi import FastAPI, Request
from app.exceptions import UnexpectedErrorAccuerd, NotFoundError, InvalidCerdiantialsError, CourseFullOrExpierdError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(UnexpectedErrorAccuerd)
async def unexpected_error(req : Request, exc : UnexpectedErrorAccuerd):
    return JSONResponse(
        status_code=500,
        content={"detail" : str(exc)}
    )

@app.exception_handler(NotFoundError)
async def not_found_error(req : Request, exc : NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail" : str(exc)}
    )


@app.exception_handler(CourseFullOrExpierdError)
async def course_enroll_full_error(req : Request, exc : CourseFullOrExpierdError):
    return JSONResponse(
        status_code=400,
        content={"detail" : str(exc)}
    )

@app.exception_handler(InvalidCerdiantialsError)
async def user_not_found_error(req : Request, exc : InvalidCerdiantialsError):
    return JSONResponse(
        status_code=401,
        content={"detail" : str(exc)}
    )




app.include_router(auth_router)
app.include_router(student_router)
app.include_router(admin_router)


