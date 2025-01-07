document.addEventListener("DOMContentLoaded", () => {
    const textElement = document.querySelector(".typewriter");
    const text = "Welcome to My Portfolio";
    let index = 0;

    function typeEffect() {
        if (index < text.length) {
            textElement.textContent += text.charAt(index);
            index++;
            setTimeout(typeEffect, 100); // Adjust speed as needed
        }
    }

    typeEffect();
});
