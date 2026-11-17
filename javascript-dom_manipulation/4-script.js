const add_item = document.querySelector('#add_item');
const my_list = document.querySelector('.my_list');


add_item.addEventListener('click', () => {
  const item = document.createElement('li');
  item.textContent = 'Item';
  my_list.appendChild(item);
});
