// ==========================
// CHECK LOGIN
// ==========================
const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "login.html";
}

const payload = JSON.parse(atob(token.split(".")[1]));

if (payload.role !== "admin") {
    alert("Access Denied");
    window.location.href = "employee_dashboard.html";
}

// ==========================
// SHOW ADMIN NAME
// ==========================
document.getElementById("adminName").innerText =
    localStorage.getItem("name");

// ==========================
// LOAD ALL EMPLOYEES
// ==========================
async function loadEmployees() {

    try {

        const employees = await apiRequest(
            "/employee/",
            "GET"
        );

        const table = document.getElementById("employeeTable");

        table.innerHTML = "";

        employees.forEach(emp => {

            table.innerHTML += `
                <tr>
                    <td>${emp.id}</td>
                    <td>${emp.employee_id}</td>
                    <td>${emp.name}</td>
                    <td>${emp.email}</td>
                    <td>${emp.department}</td>
                    <td>${emp.designation}</td>
                </tr>
            `;

        });

    } catch (err) {

        console.log(err);

    }

}

// ==========================
// LOGOUT
// ==========================
function logout() {

    localStorage.clear();

    window.location.href = "login.html";

}

// ==========================
// PAGE LOAD
// ==========================
loadEmployees();