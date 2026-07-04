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
// LOAD ALL ATTENDANCE
// ==========================
async function loadAttendance() {

    try {

        const records = await apiRequest(
            "/attendance/",
            "GET"
        );

        const table = document.getElementById("attendanceTable");

        table.innerHTML = "";

        records.forEach(record => {

            table.innerHTML += `
                <tr>
                    <td>${record.id}</td>
                    <td>${record.employee_id}</td>
                    <td>${record.date}</td>
                    <td>${record.check_in}</td>
                    <td>${record.check_out}</td>
                    <td>${record.status}</td>
                    <td>
                        <button onclick="deleteAttendance(${record.id})">
                            Delete
                        </button>
                    </td>
                </tr>
            `;

        });

    } catch (err) {

        console.log(err);
        alert("Failed to load attendance");

    }

}


// ==========================
// DELETE ATTENDANCE
// ==========================
async function deleteAttendance(id) {

    if (!confirm("Delete this attendance record?")) {
        return;
    }

    try {

        const response = await apiRequest(
            "/attendance/" + id,
            "DELETE"
        );

        alert(response.message);

        loadAttendance();

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
loadAttendance();