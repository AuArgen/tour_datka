let prev = document.querySelector('.prev');
let next = document.querySelector('.next');
let slider = document.querySelector('.slider');

next.addEventListener('click', function() {
    let sliders = document.querySelectorAll('.sliders');
    slider.appendChild(sliders[0]);
});

prev.addEventListener('click', function() {
    let sliders = document.querySelectorAll('.sliders');
    slider.prepend(sliders[sliders.length - 1]);
});

