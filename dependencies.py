from fastapi import Depends, HTTPException
from security import get_current_user


def admin_required(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin Access Required"
        )
    return user


def employee_required(user=Depends(get_current_user)):
    if user["role"] not in ["employee", "admin"]:
        raise HTTPException(
            status_code=403,
            detail="Unauthorized"
        )
    return user