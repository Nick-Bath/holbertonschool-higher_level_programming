document.addEventListener('DOMContentLoaded', () => {

  const hello = document.querySelector('#hello');

  async function getData () {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    const data = await response.json();
    hello.textContent = data.hello;

  }

  getData();

});
