from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.auth import router as auth_router
from routes.employee import router as employee_router
from routes.attendance import router as attendance_router
from routes.leave import router as leave_router
from routes.payroll import router as payroll_router

# ==========================
# CREATE DATABASE TABLES
# ==========================
Base.metadata.create_all(bind=engine)

# ==========================
# FASTAPI APP
# ==========================
app = FastAPI(
    title="Human Resource Management System",
    version="1.0.0",
    description="HRMS Backend API"
)

# ==========================
# CORS
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# HOME
# ==========================
@app.get("/")
def home():
    return {
        "message": "HRMS Backend Running Successfully"
    }

# ==========================
# ROUTES
# ==========================
app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(attendance_router)
app.include_router(leave_router)
app.include_router(payroll_router)

# ==========================
# HEALTH CHECK
# ==========================
@app.get("/health")
def health():
    return {
        "status": "success",
        "server": "running"
    }

# ==========================
# RUN SERVER
# ==========================
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )