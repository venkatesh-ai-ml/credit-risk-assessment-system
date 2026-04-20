document.addEventListener("DOMContentLoaded", function () {
    console.log("Credit Risk App Loaded");

    const form = document.querySelector("form");
    const button = document.querySelector("button");

    if (form) {
        form.addEventListener("submit", function () {
            button.innerText = "Predicting...";
            button.disabled = true;
        });
    }
});