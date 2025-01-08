// typewriter.js
function typeWriter(elementId, text, speed, callback = null) {
    const element = document.getElementById(elementId);
    let i = 0;
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        } else if (callback) {
            callback(); // Trigger the callback after typing completes
        }
    }
    type();
}

document.addEventListener('DOMContentLoaded', () => {
    typeWriter(
        "introTypewriter",
        "Hi, I am Philemon Victor, Software Developer & Engineer ...",
        100,
        () => {
            typeWriter("welcomeTypewriter", "Welcome to My Portfolio", 100, () => {
                if (typeof startCounting === "function") {
                    startCounting(); // Trigger counting when typing finishes
                }
            });
        }
    );
});
