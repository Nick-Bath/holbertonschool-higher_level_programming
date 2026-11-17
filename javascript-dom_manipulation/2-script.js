
const box = document.querySelector('#red_header');
const header = document.querySelector('header');

box.addEventListener('click', () => {
    header.classList.add('red');
});
