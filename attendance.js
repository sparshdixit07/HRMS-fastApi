const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "login.html";
}

const payload = JSON.parse(atob(token.split(".")[1]));
const employeeId = payload.id;


// ==========================
// MARK ATTENDANCE
// ==========================
async function markAttendance() {

    const date = document.getElementById("date").value;
    const check_in = document.getElementById("check_in").value;
    const check_out = document.getElementById("check_out").value;
    const status = document.getElementById("status").value;

    if (
        date === "" ||
        check_in === "" ||
        check_out === ""
    ) {
        alert("Please fill all fields");
        return;
    }

    try {

        const response = await apiRequest(
            "/attendance/",
            "POST",
            {
                employee_id: employeeId,
                date: date,
                check_in: check_in,
                check_out: check_out,
                status: status
            }
        );

        alert(response.message);

        loadAttendance();

    } catch (err) {

        console.log(err);

    }

}


// ==========================
// LOAD ATTENDANCE
// ==========================
async function loadAttendance() {

    try {

        const records = await apiRequest(
            "/attendance/employee/" + employeeId,
            "GET"
        );

        const table = document.getElementById("attendanceTable");

        table.innerHTML = "";

        records.forEach(record => {

            table.innerHTML += `
                <tr>
                    <td>${record.date}</td>
                    <td>${record.check_in}</td>
                    <td>${record.check_out}</td>
                    <td>${record.status}</td>
                </tr>
            `;

        });

    } catch (err) {

        console.log(err);

    }

}


// ==========================
// PAGE LOAD
// ==========================
loadAttendance();