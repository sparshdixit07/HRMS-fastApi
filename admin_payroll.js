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
// LOAD ALL PAYROLL
// ==========================
async function loadPayroll() {

    try {

        const payrolls = await apiRequest(
            "/payroll/",
            "GET"
        );

        const table = document.getElementById("payrollTable");

        table.innerHTML = "";

        payrolls.forEach(payroll => {

            table.innerHTML += `
                <tr>
                    <td>${payroll.id}</td>
                    <td>${payroll.employee_id}</td>
                    <td>${payroll.month}</td>
                    <td>₹${payroll.basic_salary}</td>
                    <td>₹${payroll.bonus}</td>
                    <td>₹${payroll.deduction}</td>
                    <td>₹${payroll.net_salary}</td>
                    <td>
                        <button onclick="deletePayroll(${payroll.id})">
                            Delete
                        </button>
                    </td>
                </tr>
            `;

        });

    } catch (err) {

        console.log(err);
        alert("Unable to load payroll records.");

    }

}


// ==========================
// ADD PAYROLL
// ==========================
async function addPayroll() {

    const employee_id = document.getElementById("employee_id").value;
    const month = document.getElementById("month").value;
    const basic_salary = document.getElementById("basic_salary").value;
    const bonus = document.getElementById("bonus").value;
    const deduction = document.getElementById("deduction").value;
    const net_salary = document.getElementById("net_salary").value;

    if (
        employee_id === "" ||
        month === "" ||
        basic_salary === "" ||
        bonus === "" ||
        deduction === "" ||
        net_salary === ""
    ) {
        alert("Please fill all fields");
        return;
    }

    try {

        const response = await apiRequest(
            "/payroll/",
            "POST",
            {
                employee_id: Number(employee_id),
                month: month,
                basic_salary: Number(basic_salary),
                bonus: Number(bonus),
                deduction: Number(deduction),
                net_salary: Number(net_salary)
            }
        );

        alert(response.message);

        document.getElementById("employee_id").value = "";
        document.getElementById("month").value = "";
        document.getElementById("basic_salary").value = "";
        document.getElementById("bonus").value = "";
        document.getElementById("deduction").value = "";
        document.getElementById("net_salary").value = "";

        loadPayroll();

    } catch (err) {

        console.log(err);

    }

}


// ==========================
// DELETE PAYROLL
// ==========================
async function deletePayroll(id) {

    if (!confirm("Delete this payroll record?")) {
        return;
    }

    try {

        const response = await apiRequest(
            "/payroll/" + id,
            "DELETE"
        );

        alert(response.message);

        loadPayroll();

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
loadPayroll();