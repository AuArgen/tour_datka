let lastScrollY = 0;

window.addEventListener('scroll', () => {
    const scrollTexts = document.querySelectorAll('.scroll-text');
    const currentScrollY = window.scrollY;

    scrollTexts.forEach(scrollText => {
        const rect = scrollText.getBoundingClientRect();
        const isInView = 
            rect.top + rect.height / 2 >= window.innerHeight / 2 - 15 && 
            rect.top + rect.height / 2 <= window.innerHeight / 2 + 15;

        let translateY = parseFloat(scrollText.dataset.translateY) || 0; // Используем data-атрибут для хранения значения

        if (isInView) { // Анимация только если элемент по центру экрана
            if (currentScrollY > lastScrollY) {
                translateY = Math.min(currentScrollY, 40);
            } else {
                translateY = Math.max(0, translateY - 10);
            }

            scrollText.style.transform = `translateY(-${translateY}px)`;
            scrollText.dataset.translateY = translateY; // Сохраняем новое значение
        }
    });

    lastScrollY = currentScrollY;
});

function smoothScroll(target, duration) {
    const targetElement = document.querySelector(target);
    const startPosition = window.scrollY;
    const targetPosition = targetElement.getBoundingClientRect().top + startPosition;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
    }

    function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(animation);
}

document.querySelector('your-button-selector').addEventListener('click', () => {
    smoothScroll('#your-target-element', 1000);
});


function smoothScroll(target, duration) {
    const targetElement = document.querySelector(target);
    const startPosition = window.scrollY;
    const targetPosition = targetElement.getBoundingClientRect().top + startPosition;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
    }

    function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(animation);
}

document.querySelector('your-button-selector').addEventListener('click', () => {
    smoothScroll('#your-target-element', 1000);
});