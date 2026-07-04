const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "login.html";
}

const payload = JSON.parse(atob(token.split(".")[1]));
const employeeId = payload.id;


// ==========================
// APPLY LEAVE
// ==========================
async function applyLeave() {

    const leave_type = document.getElementById("leave_type").value;
    const start_date = document.getElementById("start_date").value;
    const end_date = document.getElementById("end_date").value;
    const remarks = document.getElementById("remarks").value.trim();

    if (start_date === "" || end_date === "") {
        alert("Please select dates");
        return;
    }

    try {

        const response = await apiRequest(
            "/leave/",
            "POST",
            {
                employee_id: employeeId,
                leave_type: leave_type,
                start_date: start_date,
                end_date: end_date,
                remarks: remarks
            }
        );

        alert(response.message);

        document.getElementById("remarks").value = "";

        loadLeaves();

    } catch (err) {

        console.log(err);

    }

}


// ==========================
// LOAD MY LEAVES
// ==========================
async function loadLeaves() {

    try {

        const leaves = await apiRequest(
            "/leave/employee/" + employeeId,
            "GET"
        );

        const table = document.getElementById("leaveTable");

        table.innerHTML = "";

        leaves.forEach(leave => {

            table.innerHTML += `
                <tr>
                    <td>${leave.leave_type}</td>
                    <td>${leave.start_date}</td>
                    <td>${leave.end_date}</td>
                    <td>${leave.remarks}</td>
                    <td>${leave.status}</td>
                    <td>${leave.admin_comment}</td>
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
loadLeaves();