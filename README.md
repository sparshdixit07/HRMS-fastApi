Human Resource Management System (HRMS)

A Human Resource Management System (HRMS) developed using HTML, CSS, JavaScript, FastAPI (Python), and SQLite. The system digitizes essential HR operations such as employee management, attendance, leave management, payroll, and role-based authentication.

---

Tech Stack

Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

Backend

- Python
- FastAPI
- SQLAlchemy

Database

- SQLite

Authentication

- JWT (JSON Web Token)
- Password Hashing (bcrypt)

---

Features

Authentication

- Employee/Admin Signup
- Secure Login
- Password Hashing
- JWT Authentication
- Role-Based Access

---

Employee Module

- View Profile
- Update Profile
- View Attendance
- Apply Leave
- View Leave Status
- View Payroll

---

Admin Module

- View All Employees
- Manage Employee Profiles
- View All Attendance
- Delete Attendance Records
- View Leave Requests
- Approve Leave
- Reject Leave
- Add Payroll
- View Payroll Records
- Delete Payroll Records

---

Attendance Management

- Check In
- Check Out
- Daily Attendance
- Attendance History
- Attendance Status
  - Present
  - Absent
  - Half-day
  - Leave

---

Leave Management

- Apply Leave
- Paid Leave
- Sick Leave
- Unpaid Leave
- Leave Approval
- Leave Rejection
- Admin Comments

---

Payroll Management

- Add Payroll
- View Payroll
- Update Payroll
- Delete Payroll
- Monthly Salary Details

---

Project Structure

HRMS/

│
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── dependencies.py
│   ├── requirements.txt
│   │
│   └── routes/
│       ├── auth.py
│       ├── employee.py
│       ├── attendance.py
│       ├── leave.py
│       └── payroll.py
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── employee_dashboard.html
│   ├── admin_dashboard.html
│   ├── attendance.html
│   ├── leave.html
│   ├── payroll.html
│   ├── admin_attendance.html
│   ├── admin_leave.html
│   ├── admin_payroll.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── api.js
│       ├── login.js
│       ├── signup.js
│       ├── employee.js
│       ├── admin.js
│       ├── attendance.js
│       ├── leave.js
│       ├── payroll.js
│       ├── admin_attendance.js
│       ├── admin_leave.js
│       └── admin_payroll.js
│
└── README.md

---

Installation

Clone the Repository

git clone <repository-url>

---

Go to Backend Folder

cd backend

---

Install Dependencies

pip install -r requirements.txt

---

Run Backend

python main.py

OR

uvicorn main:app --reload

Backend URL

http://127.0.0.1:8000

Swagger Documentation

http://127.0.0.1:8000/docs

---

Run Frontend

Open

frontend/index.html

using VS Code Live Server.

---

API Modules

- Authentication API
- Employee API
- Attendance API
- Leave API
- Payroll API

---

Database Tables

- users
- attendance
- leave_requests
- payroll

---

User Roles

Employee

- Login
- View Profile
- Update Profile
- Mark Attendance
- Apply Leave
- View Payroll

---

Admin

- Login
- Manage Employees
- View Attendance
- Approve Leave
- Reject Leave
- Manage Payroll

---

Security

- JWT Authentication
- Password Hashing
- Role-Based Authorization
- Protected APIs

---

Future Improvements

- Email Verification
- Forgot Password
- Attendance Calendar
- Employee Search
- Profile Picture Upload
- Payroll PDF Download
- Attendance Reports
- Leave Analytics
- Dashboard Charts
- Notification System

---

Developed By

Shobhan Dixit

B.Tech Student

Human Resource Management System (HRMS)

Built for Hackathon Submission.