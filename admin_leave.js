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
// LOAD ALL LEAVES
// ==========================
async function loadLeaves() {

    try {

        const leaves = await apiRequest(
            "/leave/",
            "GET"
        );

        const table = document.getElementById("leaveTable");

        table.innerHTML = "";

        leaves.forEach(leave => {

            table.innerHTML += `
                <tr>
                    <td>${leave.id}</td>
                    <td>${leave.employee_id}</td>
                    <td>${leave.leave_type}</td>
                    <td>${leave.start_date}</td>
                    <td>${leave.end_date}</td>
                    <td>${leave.remarks}</td>
                    <td>${leave.status}</td>
                    <td>
                        <input
                            type="text"
                            id="comment${leave.id}"
                            placeholder="Admin Comment"
                            value="${leave.admin_comment || ""}"
                        >
                    </td>
                    <td>
                        <button onclick="updateLeave(${leave.id}, 'Approved')">
                            Approve
                        </button>

                        <button onclick="updateLeave(${leave.id}, 'Rejected')">
                            Reject
                        </button>
                    </td>
                </tr>
            `;

        });

    } catch (err) {

        console.log(err);
        alert("Failed to load leave requests");

    }

}


// ==========================
// APPROVE / REJECT LEAVE
// ==========================
async function updateLeave(id, status) {

    const comment = document.getElementById(
        "comment" + id
    ).value;

    try {

        const response = await apiRequest(
            "/leave/" + id,
            "PUT",
            {
                status: status,
                admin_comment: comment
            }
        );

        alert(response.message);

        loadLeaves();

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
loadLeaves();