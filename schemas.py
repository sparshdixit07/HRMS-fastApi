from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


# ==========================
# AUTH
# ==========================

class SignupSchema(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    password: str
    role: str

    phone: Optional[str] = ""
    address: Optional[str] = ""
    department: Optional[str] = ""
    designation: Optional[str] = ""
    salary: Optional[float] = 0


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


# ==========================
# EMPLOYEE
# ==========================

class UpdateProfileSchema(BaseModel):
    phone: str
    address: str
    profile_picture: Optional[str] = ""


# ==========================
# ATTENDANCE
# ==========================

class AttendanceSchema(BaseModel):
    employee_id: int
    date: date
    check_in: str
    check_out: str
    status: str


# ==========================
# LEAVE
# ==========================

class LeaveSchema(BaseModel):
    employee_id: int
    leave_type: str
    start_date: date
    end_date: date
    remarks: str


class LeaveApprovalSchema(BaseModel):
    status: str
    admin_comment: Optional[str] = ""


# ==========================
# PAYROLL
# ==========================

class PayrollSchema(BaseModel):
    employee_id: int
    month: str
    basic_salary: float
    bonus: float
    deduction: float
    net_salary: float