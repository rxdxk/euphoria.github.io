const slides = document.querySelectorAll('.hero-bg-slider .slide');
let currentSlide = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.remove('active');
    if (i === index) slide.classList.add('active');
  });
}

// Инициализация
showSlide(currentSlide);

// Авто-переключение каждые 6 секунд
setInterval(() => {
  currentSlide = (currentSlide + 1) % slides.length;
  showSlide(currentSlide);
}, 6000);