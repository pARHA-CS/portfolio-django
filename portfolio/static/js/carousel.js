let currentIndex = 0;
const items = document.querySelectorAll('.carousel-item');
const totalItems = items.length;
const visibleItems = 3; // Nombre d'images visibles à la fois

function updateCarouselPosition() {
    const carousel = document.querySelector('.carousel');
    const itemWidth = items[0].offsetWidth;
    const newPosition = -(currentIndex * itemWidth);
    carousel.style.transform = `translateX(${newPosition}px)`;
}

function nextSlide() {
    if (currentIndex < totalItems - visibleItems) {
        currentIndex++;
        updateCarouselPosition();
    }
}

function prevSlide() {
    if (currentIndex > 0) {
        currentIndex--;
        updateCarouselPosition();
    }
}

window.addEventListener('resize', updateCarouselPosition);
