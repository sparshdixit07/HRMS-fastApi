from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Attendance, User
from schemas import AttendanceSchema

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# ==========================
# CHECK IN / CREATE ATTENDANCE
# ==========================
@router.post("/")
def mark_attendance(data: AttendanceSchema, db: Session = Depends(get_db)):

    employee = db.query(User).filter(
        User.id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    attendance = db.query(Attendance).filter(
        Attendance.employee_id == data.employee_id,
        Attendance.date == data.date
    ).first()

    if attendance:
        raise HTTPException(
            status_code=400,
            detail="Attendance Already Marked"
        )

    new_attendance = Attendance(
        employee_id=data.employee_id,
        date=data.date,
        check_in=data.check_in,
        check_out=data.check_out,
        status=data.status
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return {
        "message": "Attendance Marked Successfully",
        "attendance": new_attendance
    }


# ==========================
# UPDATE CHECK OUT
# ==========================
@router.put("/checkout/{attendance_id}")
def checkout(
    attendance_id: int,
    check_out: str,
    db: Session = Depends(get_db)
):

    attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance Not Found"
        )

    attendance.check_out = check_out

    db.commit()
    db.refresh(attendance)

    return {
        "message": "Check Out Updated",
        "attendance": attendance
    }


# ==========================
# GET EMPLOYEE ATTENDANCE
# ==========================
@router.get("/employee/{employee_id}")
def employee_attendance(
    employee_id: int,
    db: Session = Depends(get_db)
):

    attendance = db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()

    return attendance


# ==========================
# GET ALL ATTENDANCE
# ==========================
@router.get("/")
def all_attendance(db: Session = Depends(get_db)):

    attendance = db.query(Attendance).all()

    return attendance


# ==========================
# GET SINGLE RECORD
# ==========================
@router.get("/{attendance_id}")
def get_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):

    attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance Not Found"
        )

    return attendance


# ==========================
# DELETE ATTENDANCE
# ==========================
@router.delete("/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db)
):

    attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance Not Found"
        )

    db.delete(attendance)
    db.commit()

    return {
        "message": "Attendance Deleted Successfully"
    }