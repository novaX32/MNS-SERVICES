function showToast(message, type = "success", keep = false) {
    const toast = document.getElementById("toast");

    toast.textContent = message;

    toast.className = "toast";
    toast.classList.add(type);

    // show
    setTimeout(() => {
        toast.classList.add("show");
    }, 10);

    // auto hide only if NOT loading
    if (!keep) {
        setTimeout(() => {
            toast.classList.remove("show");
        }, 4000);
    }
}


document.getElementById("serviceForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const name = document.getElementById("userName").value.trim();
    const phone = document.getElementById("userPhone").value.trim();
    const email = document.getElementById("userEmail").value.trim();
    const service = document.getElementById("service").value;

    const button = this.querySelector("button");

    if (phone.length < 10) {
        showToast("Please enter a valid 10-digit phone number", "error");
        return;
    }

    try {
        // 🔥 KEEP TOAST ON SCREEN
        showToast("Sending request...", "loading", true);

        // disable button
        button.disabled = true;
        button.textContent = "Sending...";

        const response = await fetch("http://127.0.0.1:8000/api/contact", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name,
                phone,
                email,
                service
            })
        });

        const result = await response.json();

        if (response.ok && result.success) {

            // 🔥 UPDATE SAME TOAST (NO DISAPPEAR)
            showToast(
                "Thanks for connecting. Email sent successfully. Please check your inbox.",
                "success",
                false
            );

            document.getElementById("serviceForm").reset();

        } else {
            showToast("Something went wrong. Please try again.", "error");
        }

    } catch (error) {
        showToast("Server error. Please try again later.", "error");
    } finally {
        button.disabled = false;
        button.textContent = "Submit Request";
    }
});