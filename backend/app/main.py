from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.config import settings
from app.database import init_db
import uvicorn

# Import routers
from app.routers import auth, research, ai_generation, references

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="منصة متكاملة لإنجاز البحوث الجامعية باستخدام الذكاء الاصطناعي",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "status": "error"}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc), "status": "error"}
    )


# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()
    print("✅ Database initialized")
    print(f"✅ {settings.APP_NAME} v{settings.APP_VERSION} started")


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "مرحباً بك في منصة إنجاز البحوث الجامعية",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }


# Health check
@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "version": settings.APP_VERSION
    }


# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(research.router, prefix="/api/research", tags=["Research"])
app.include_router(ai_generation.router, prefix="/api/ai", tags=["AI Generation"])
app.include_router(references.router, prefix="/api/references", tags=["References"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
