const BASE_URL = "http://127.0.0.1:8000";

async function apiRequest(endpoint, method = "GET", body = null) {

    const token = localStorage.getItem("token");

    const options = {
        method: method,
        headers: {
            "Content-Type": "application/json"
        }
    };

    if (token) {
        options.headers["Authorization"] = "Bearer " + token;
    }

    if (body) {
        options.body = JSON.stringify(body);
    }

    const response = await fetch(BASE_URL + endpoint, options);

    const data = await response.json();

    if (!response.ok) {
        alert(data.detail || "Something went wrong");
        throw new Error(data.detail);
    }

    return data;
}