document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contactForm");
    const successMsg = document.getElementById("formSuccess");

    if (form) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            // Basic html5 validation is handled by 'required' attributes (Nome, Mensagem)
            
            // H-07: Show inline success message
            successMsg.classList.add("show");
            form.reset();
            
            // Hide message after 5 seconds
            setTimeout(() => {
                successMsg.classList.remove("show");
            }, 5000);
        });
    }
});
