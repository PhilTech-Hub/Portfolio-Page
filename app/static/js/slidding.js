let currentSlide = 0;
const cardsToShow = 3;
const totalCards = 6; // 6 blog cards in total
const cards = document.querySelectorAll('.blog-card');
const prevArrow = document.querySelector('.prev-arrow');
const nextArrow = document.querySelector('.next-arrow');
const blogCardsContainer = document.querySelector('.blog-cards-container');

function showSlide(index) {
    if (index < 0) {
        currentSlide = totalCards - cardsToShow; // Loop back to last 3 cards
    } else if (index >= totalCards - cardsToShow) {
        currentSlide = 0; // Loop back to first 3 cards
    } else {
        currentSlide = index;
    }
    updateSlider();
}

function updateSlider() {
    // Apply the transform to show only 3 cards at a time
    const offset = -currentSlide * (cards[0].offsetWidth + 20); // Card width + gap (20px)
    blogCardsContainer.style.transform = `translateX(${offset}px)`;
}

// Initialize the first set of slides
updateSlider();

// Add event listeners for the arrows
prevArrow.addEventListener('click', () => showSlide(currentSlide - 1));
nextArrow.addEventListener('click', () => showSlide(currentSlide + 1));
