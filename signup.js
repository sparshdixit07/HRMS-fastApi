async function signup() {

    const employee_id = document.getElementById("employee_id").value.trim();
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const role = document.getElementById("role").value;
    const phone = document.getElementById("phone").value.trim();
    const address = document.getElementById("address").value.trim();
    const department = document.getElementById("department").value.trim();
    const designation = document.getElementById("designation").value.trim();
    const salary = document.getElementById("salary").value;

    if (
        employee_id === "" ||
        name === "" ||
        email === "" ||
        password === ""
    ) {
        alert("Please fill all required fields");
        return;
    }

    try {

        const response = await apiRequest(
            "/auth/signup",
            "POST",
            {
                employee_id: employee_id,
                name: name,
                email: email,
                password: password,
                role: role,
                phone: phone,
                address: address,
                department: department,
                designation: designation,
                salary: Number(salary)
            }
        );

        alert(response.message);

        window.location.href = "login.html";

    } catch (error) {
        console.error(error);
    }

}