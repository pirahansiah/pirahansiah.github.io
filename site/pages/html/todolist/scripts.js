const todoSections = ['day', 'week', 'month', 'year'];
let todos = {};
let selectedDate = new Date();

function saveToLocalStorage() {
    localStorage.setItem('todos', JSON.stringify(todos));
}

function loadFromLocalStorage() {
    const storedTodos = localStorage.getItem('todos');
    if (storedTodos) {
        todos = JSON.parse(storedTodos);
    } else {
        todoSections.forEach(section => {
            todos[section] = [];
        });
    }
    updateCalendars();
}

function updateCalendars() {
    // Day
    document.getElementById('dayCalendar').textContent = selectedDate.toLocaleDateString();

    // Week
    const weekStart = new Date(selectedDate);
    weekStart.setDate(weekStart.getDate() - weekStart.getDay());
    const weekDays = document.getElementById('weekDays');
    weekDays.innerHTML = '';
    for (let i = 0; i < 7; i++) {
        const day = new Date(weekStart);
        day.setDate(day.getDate() + i);
        const dayElement = document.createElement('div');
        dayElement.className = 'week-day';
        dayElement.textContent = `${day.toLocaleString('default', { weekday: 'short' })} ${day.getDate()}`;
        if (day.toDateString() === selectedDate.toDateString()) {
            dayElement.classList.add('selected');
        }
        dayElement.addEventListener('click', () => {
            selectedDate = new Date(day);
            updateCalendars();
            renderTodos('day');
        });
        weekDays.appendChild(dayElement);
    }
    document.getElementById('weekCalendar').textContent = `Week ${getWeekNumber(selectedDate)}, ${selectedDate.getFullYear()}`;

    // Month
    const monthDays = document.getElementById('monthDays');
    monthDays.innerHTML = '';
    const firstDay = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), 1);
    const lastDay = new Date(selectedDate.getFullYear(), selectedDate.getMonth() + 1, 0);
    for (let i = 1; i <= lastDay.getDate(); i++) {
        const dayElement = document.createElement('div');
        dayElement.className = 'month-day';
        dayElement.textContent = i;
        if (i === selectedDate.getDate()) {
            dayElement.classList.add('selected');
        }
        dayElement.addEventListener('click', () => {
            selectedDate = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), i);
            updateCalendars();
            renderTodos('day');
        });
        monthDays.appendChild(dayElement);
    }
    document.getElementById('monthCalendar').textContent = selectedDate.toLocaleString('default', { month: 'long', year: 'numeric' });

    // Year
    const yearMonths = document.getElementById('yearMonths');
    yearMonths.innerHTML = '';
    for (let i = 0; i < 12; i++) {
        const monthElement = document.createElement('div');
        monthElement.className = 'year-month';
        monthElement.textContent = new Date(selectedDate.getFullYear(), i, 1).toLocaleString('default', { month: 'long' });
        if (i === selectedDate.getMonth()) {
            monthElement.classList.add('selected');
        }
        monthElement.addEventListener('click', () => {
            selectedDate = new Date(selectedDate.getFullYear(), i, 1);
            updateCalendars();
            renderTodos('month');
        });
        yearMonths.appendChild(monthElement);
    }
    document.getElementById('yearCalendar').textContent = selectedDate.getFullYear();
}

function getWeekNumber(d) {
    d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
    d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
    const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
    return Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
}

function addTodoItem(section, text) {
    const todo = {
        id: Date.now(),
        text: text,
        done: false,
        date: selectedDate.toISOString()
    };
    todos[section].push(todo);
    saveToLocalStorage();
    renderTodos(section);
}

function toggleTodo(section, id) {
    const todo = todos[section].find(t => t.id === id);
    if (todo) {
        todo.done = !todo.done;
        saveToLocalStorage();
        renderTodos(section);
    }
}

function deleteTodo(section, id) {
    todos[section] = todos[section].filter(t => t.id !== id);
    saveToLocalStorage();
    renderTodos(section);
}

function renderTodos(section) {
    const list = document.getElementById(`${section}Todos`);
    list.innerHTML = '';
    todos[section].forEach(todo => {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.done ? 'done' : ''}`;
        li.innerHTML = `
            <span>${todo.text}</span>
            <button class="delete-btn">Delete</button>
        `;
        li.querySelector('span').addEventListener('click', () => toggleTodo(section, todo.id));
        li.querySelector('.delete-btn').addEventListener('click', (e) => {
            e.stopPropagation();
            deleteTodo(section, todo.id);
        });
        list.appendChild(li);
    });
}

function exportTodos() {
    const dataStr = JSON.stringify(todos);
    const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);
    const exportFileDefaultName = 'todos.json';
    let linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
}

function importTodos() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            todos = JSON.parse(e.target.result);
            saveToLocalStorage();
            todoSections.forEach(section => renderTodos(section));
        };
        reader.readAsText(file);
    }
}

document.getElementById('exportBtn').addEventListener('click', exportTodos);
document.getElementById('importBtn').addEventListener('click', () => {
    document.getElementById('fileInput').click();
});
document.getElementById('fileInput').addEventListener('change', importTodos);


function initApp() {
    loadFromLocalStorage();
    updateCalendars();
    todoSections.forEach(section => renderTodos(section));
}


initApp();
