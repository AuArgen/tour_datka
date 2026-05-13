

document.addEventListener('DOMContentLoaded', function () {
    setTimeout(() => {        
        const mainContainer = document.querySelector('.maincontainer');
    
        window.addEventListener('scroll', function () {
            const scrollTop = window.scrollY || document.documentElement.scrollTop;
    
            if (scrollTop > 100) {
                mainContainer.classList.add('hed');
            } else {
                mainContainer.classList.remove('hed');
            }
        });
    
        document.querySelector('.Mobile__menu').addEventListener('click', function () {
            const absolitElement = document.querySelector('.modal__content');
            absolitElement.classList.toggle('show');
        });
    
        document.querySelector('.Mobile__menu').addEventListener('click', function () {
            const absolitElement = document.querySelector('.Mobile__menu');
            absolitElement.classList.toggle('activ__buton');
        });
    
        const links = document.querySelectorAll('.list a');
        const sections = document.querySelectorAll('section');
    
        window.addEventListener('scroll', function () {
            let current = '';
    
            sections.forEach(section => {
                const sectionTop = section.getBoundingClientRect().top;
                const sectionHeight = section.clientHeight;
    
                // Проверяем, находится ли секция в видимой области
                if (sectionTop <= window.innerHeight / 2 && sectionTop + sectionHeight > window.innerHeight / 2) {
                    current = section.getAttribute('id');
                }
            });
    
            // Удаляем класс у всех ссылок и добавляем только к текущей
            links.forEach(link => {
                link.classList.remove('lis');
                if (link.getAttribute('href') === `#${current}`) {
                    link.classList.add('lis');
                }
            });
        });
    }, 1000);
});

