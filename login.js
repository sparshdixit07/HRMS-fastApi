async function login() {

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (email === "" || password === "") {
        alert("Please fill all fields");
        return;
    }

    try {

        const response = await apiRequest(
            "/auth/login",
            "POST",
            {
                email: email,
                password: password
            }
        );

        localStorage.setItem("token", response.token);
        localStorage.setItem("role", response.role);
        localStorage.setItem("name", response.name);

        alert(response.message);

        if (response.role === "admin") {
            window.location.href = "admin_dashboard.html";
        } else {
            window.location.href = "employee_dashboard.html";
        }

    } catch (error) {
        console.log(error);
    }

}
