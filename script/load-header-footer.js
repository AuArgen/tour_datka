import config from '../env.js';

document.addEventListener('DOMContentLoaded', () => {
    fetch(`${config.BASE_URL}/components/header.html`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.text();
      })
      .then(data => {
        document.getElementById('header-placeholder').innerHTML = data;
      })
      .catch(error => {
        console.error('Error loading header:', error);
      });

      fetch(`${config.BASE_URL}/components/footer.html`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.text();
      })
      .then(data => {
        document.getElementById('footer-placeholder').innerHTML = data;
      })
      .catch(error => {
        console.error('Error loading header:', error);
      });
  });
  