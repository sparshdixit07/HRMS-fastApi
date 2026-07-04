// ==========================
// CHECK LOGIN
// ==========================
const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "login.html";
}


// ==========================
// LOAD PROFILE
// ==========================
async function loadProfile() {

    try {

        const payload = JSON.parse(atob(token.split(".")[1]));

        const employeeId = payload.id;

        const user = await apiRequest(
            "/employee/" + employeeId,
            "GET"
        );

        document.getElementById("employeeName").innerText = user.name;

        document.getElementById("name").innerText = user.name;

        document.getElementById("employee_id").innerText = user.employee_id;

        document.getElementById("email").innerText = user.email;

        document.getElementById("department").innerText = user.department;

        document.getElementById("designation").innerText = user.designation;

        document.getElementById("phone").innerText = user.phone;

        document.getElementById("address").innerText = user.address;

        document.getElementById("salary").innerText = user.salary;

    } catch (error) {

        console.log(error);

        alert("Session Expired");

        logout();

    }

}


// ==========================
// LOGOUT
// ==========================
function logout() {

    // localStorage.removeItem("token");
    // localStorage.removeItem("role");
    // localStorage.removeItem("name");
       localStorage.clear();
       sessionStorage.clear();
    window.location.replace("index.html");

}


// ==========================
// PAGE LOAD
// ==========================
loadProfile();