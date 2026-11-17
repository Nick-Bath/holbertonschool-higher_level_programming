const list_movies = document.querySelector('#list_movies');
const ul = document.querySelector('ul');

async function getData () {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const data = await response.json();

  data.results.forEach(movie => {
    const item = document.createElement('li');
    item.textContent = movie.title;
    ul.appendChild(item);
  });
}

getData();
