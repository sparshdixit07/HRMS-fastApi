const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "login.html";
}

const payload = JSON.parse(atob(token.split(".")[1]));
const employeeId = payload.id;


// ==========================
// LOAD PAYROLL
// ==========================
async function loadPayroll() {

    try {

        const payrolls = await apiRequest(
            "/payroll/employee/" + employeeId,
            "GET"
        );

        const table = document.getElementById("payrollTable");

        table.innerHTML = "";

        if (payrolls.length === 0) {

            table.innerHTML = `
                <tr>
                    <td colspan="5" style="text-align:center;">
                        No Payroll Records Found
                    </td>
                </tr>
            `;

            return;
        }

        payrolls.forEach(payroll => {

            table.innerHTML += `
                <tr>
                    <td>${payroll.month}</td>
                    <td>₹${payroll.basic_salary}</td>
                    <td>₹${payroll.bonus}</td>
                    <td>₹${payroll.deduction}</td>
                    <td>₹${payroll.net_salary}</td>
                </tr>
            `;

        });

    } catch (err) {

        console.error(err);

        alert("Failed to load payroll.");

    }

}


// ==========================
// PAGE LOAD
// ==========================
loadPayroll();