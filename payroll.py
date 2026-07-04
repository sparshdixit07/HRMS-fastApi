from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Payroll, User
from schemas import PayrollSchema

router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)


# ==========================
# ADD PAYROLL (ADMIN)
# ==========================
@router.post("/")
def add_payroll(
    data: PayrollSchema,
    db: Session = Depends(get_db)
):

    employee = db.query(User).filter(
        User.id == data.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    payroll = Payroll(
        employee_id=data.employee_id,
        month=data.month,
        basic_salary=data.basic_salary,
        bonus=data.bonus,
        deduction=data.deduction,
        net_salary=data.net_salary
    )

    db.add(payroll)
    db.commit()
    db.refresh(payroll)

    return {
        "message": "Payroll Added Successfully",
        "payroll": payroll
    }


# ==========================
# GET ALL PAYROLL
# ==========================
@router.get("/")
def get_all_payroll(
    db: Session = Depends(get_db)
):

    return db.query(Payroll).all()


# ==========================
# GET EMPLOYEE PAYROLL
# ==========================
@router.get("/employee/{employee_id}")
def get_employee_payroll(
    employee_id: int,
    db: Session = Depends(get_db)
):

    payroll = db.query(Payroll).filter(
        Payroll.employee_id == employee_id
    ).all()

    return payroll


# ==========================
# GET SINGLE PAYROLL
# ==========================
@router.get("/{payroll_id}")
def get_payroll(
    payroll_id: int,
    db: Session = Depends(get_db)
):

    payroll = db.query(Payroll).filter(
        Payroll.id == payroll_id
    ).first()

    if not payroll:
        raise HTTPException(
            status_code=404,
            detail="Payroll Not Found"
        )

    return payroll


# ==========================
# UPDATE PAYROLL
# ==========================
@router.put("/{payroll_id}")
def update_payroll(
    payroll_id: int,
    data: PayrollSchema,
    db: Session = Depends(get_db)
):

    payroll = db.query(Payroll).filter(
        Payroll.id == payroll_id
    ).first()

    if not payroll:
        raise HTTPException(
            status_code=404,
            detail="Payroll Not Found"
        )

    payroll.month = data.month
    payroll.basic_salary = data.basic_salary
    payroll.bonus = data.bonus
    payroll.deduction = data.deduction
    payroll.net_salary = data.net_salary

    db.commit()
    db.refresh(payroll)

    return {
        "message": "Payroll Updated Successfully",
        "payroll": payroll
    }


# ==========================
# DELETE PAYROLL
# ==========================
@router.delete("/{payroll_id}")
def delete_payroll(
    payroll_id: int,
    db: Session = Depends(get_db)
):

    payroll = db.query(Payroll).filter(
        Payroll.id == payroll_id
    ).first()

    if not payroll:
        raise HTTPException(
            status_code=404,
            detail="Payroll Not Found"
        )

    db.delete(payroll)
    db.commit()

    return {
        "message": "Payroll Deleted Successfully"
    }