from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Leave, User
from schemas import LeaveSchema, LeaveApprovalSchema

router = APIRouter(
    prefix="/leave",
    tags=["Leave"]
)


# ==========================
# APPLY FOR LEAVE
# ==========================
@router.post("/")
def apply_leave(
    data: LeaveSchema,
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

    leave = Leave(
        employee_id=data.employee_id,
        leave_type=data.leave_type,
        start_date=data.start_date,
        end_date=data.end_date,
        remarks=data.remarks,
        status="Pending"
    )

    db.add(leave)
    db.commit()
    db.refresh(leave)

    return {
        "message": "Leave Applied Successfully",
        "leave": leave
    }


# ==========================
# GET ALL LEAVES
# ==========================
@router.get("/")
def get_all_leaves(
    db: Session = Depends(get_db)
):

    return db.query(Leave).all()


# ==========================
# GET EMPLOYEE LEAVES
# ==========================
@router.get("/employee/{employee_id}")
def get_employee_leaves(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Leave).filter(
        Leave.employee_id == employee_id
    ).all()


# ==========================
# GET SINGLE LEAVE
# ==========================
@router.get("/{leave_id}")
def get_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):

    leave = db.query(Leave).filter(
        Leave.id == leave_id
    ).first()

    if not leave:
        raise HTTPException(
            status_code=404,
            detail="Leave Not Found"
        )

    return leave


# ==========================
# APPROVE / REJECT LEAVE
# ==========================
@router.put("/{leave_id}")
def approve_leave(
    leave_id: int,
    data: LeaveApprovalSchema,
    db: Session = Depends(get_db)
):

    leave = db.query(Leave).filter(
        Leave.id == leave_id
    ).first()

    if not leave:
        raise HTTPException(
            status_code=404,
            detail="Leave Not Found"
        )

    leave.status = data.status
    leave.admin_comment = data.admin_comment

    db.commit()
    db.refresh(leave)

    return {
        "message": "Leave Updated Successfully",
        "leave": leave
    }


# ==========================
# DELETE LEAVE
# ==========================
@router.delete("/{leave_id}")
def delete_leave(
    leave_id: int,
    db: Session = Depends(get_db)
):

    leave = db.query(Leave).filter(
        Leave.id == leave_id
    ).first()

    if not leave:
        raise HTTPException(
            status_code=404,
            detail="Leave Not Found"
        )

    db.delete(leave)
    db.commit()

    return {
        "message": "Leave Deleted Successfully"
    }