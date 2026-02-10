const todoForm = document.getElementById('todo-form');
const taskInput = document.getElementById('task-input');
const todoList = document.getElementById('todo-list');

const createTodoItem = (taskText) => {
  const listItem = document.createElement('li');
  listItem.className = 'todo-item';

  const leftContainer = document.createElement('div');
  leftContainer.className = 'todo-left';

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';

  const textSpan = document.createElement('span');
  textSpan.textContent = taskText;

  checkbox.addEventListener('change', () => {
    listItem.classList.toggle('completed', checkbox.checked);
  });

  const deleteButton = document.createElement('button');
  deleteButton.className = 'delete-btn';
  deleteButton.innerHTML = '🗑';

  deleteButton.addEventListener('click', () => {
    todoList.removeChild(listItem);
  });

  leftContainer.appendChild(checkbox);
  leftContainer.appendChild(textSpan);

  listItem.appendChild(leftContainer);
  listItem.appendChild(deleteButton);

  return listItem;
};

todoForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const taskText = taskInput.value.trim();
  if (taskText === '') {
    return;
  }
 
  const todoItem = createTodoItem(taskText);
  todoList.appendChild(todoItem);

  taskInput.value = '';
});
