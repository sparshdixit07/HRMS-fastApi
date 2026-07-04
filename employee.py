from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UpdateProfileSchema

router = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)


# ==========================
# GET ALL EMPLOYEES (ADMIN)
# ==========================
@router.get("/")
def get_all_employees(db: Session = Depends(get_db)):

    employees = db.query(User).all()

    return employees


# ==========================
# GET EMPLOYEE BY ID
# ==========================
@router.get("/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):

    employee = db.query(User).filter(
        User.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee


# ==========================
# UPDATE PROFILE
# ==========================
@router.put("/{employee_id}")
def update_profile(
    employee_id: int,
    data: UpdateProfileSchema,
    db: Session = Depends(get_db)
):

    employee = db.query(User).filter(
        User.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    employee.phone = data.phone
    employee.address = data.address
    employee.profile_picture = data.profile_picture

    db.commit()
    db.refresh(employee)

    return {
        "message": "Profile Updated Successfully",
        "employee": employee
    }


# ==========================
# DELETE EMPLOYEE
# ==========================
@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(User).filter(
        User.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": "Employee Deleted Successfully"
    }