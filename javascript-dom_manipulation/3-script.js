const header = document.querySelector('header');
const toggle = document.querySelector('#toggle_header');

toggle.addEventListener('click', () => {
    if (header.classList.contains('red')){
      header.classList.replace('red', 'green');
    } else {
      header.classList.replace('green', 'red');
    }
});
