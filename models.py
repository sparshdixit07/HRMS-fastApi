from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


# ==========================
# USER TABLE
# ==========================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="employee")

    phone = Column(String)
    address = Column(String)
    department = Column(String)
    designation = Column(String)
    profile_picture = Column(String, default="")

    salary = Column(Float, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)

    attendance = relationship("Attendance", back_populates="employee")
    leaves = relationship("Leave", back_populates="employee")
    payrolls = relationship("Payroll", back_populates="employee")


# ==========================
# ATTENDANCE TABLE
# ==========================
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("users.id"))

    date = Column(Date)

    check_in = Column(String)

    check_out = Column(String)

    status = Column(String)

    employee = relationship("User", back_populates="attendance")


# ==========================
# LEAVE TABLE
# ==========================
class Leave(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("users.id"))

    leave_type = Column(String)

    start_date = Column(Date)

    end_date = Column(Date)

    remarks = Column(String)

    status = Column(String, default="Pending")

    admin_comment = Column(String, default="")

    employee = relationship("User", back_populates="leaves")


# ==========================
# PAYROLL TABLE
# ==========================
class Payroll(Base):
    __tablename__ = "payroll"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("users.id"))

    month = Column(String)

    basic_salary = Column(Float)

    bonus = Column(Float)

    deduction = Column(Float)

    net_salary = Column(Float)

    employee = relationship("User", back_populates="payrolls")