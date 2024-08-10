const todoSections = ['daily', 'weekly', 'monthly', 'yearly'];
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
}

function updateCalendars() {
    // Daily
    const dailyCalendar = document.getElementById('dailyCalendar');
    if (dailyCalendar) {
        dailyCalendar.textContent = selectedDate.toLocaleDateString();
    }

    // Weekly
    const weekDays = document.getElementById('weekDays');
    if (weekDays) {
        const weekStart = new Date(selectedDate);
        weekStart.setDate(weekStart.getDate() - weekStart.getDay());
        weekDays.innerHTML = '';
        for (let i = 0; i < 7; i++) {
            const day = new Date(weekStart);
            day.setDate(day.getDate() + i);
            const dayElement = document.createElement('div');
            dayElement.className = 'calendar-item';
            dayElement.textContent = `${day.toLocaleString('default', { weekday: 'short' })} ${day.getDate()}`;
            if (day.toDateString() === selectedDate.toDateString()) {
                dayElement.classList.add('selected');
            }
            dayElement.addEventListener('click', () => {
                selectedDate = new Date(day);
                updateCalendars();
                renderTodos('daily');
            });
            weekDays.appendChild(dayElement);
        }
        const weeklyCalendar = document.getElementById('weeklyCalendar');
        if (weeklyCalendar) {
            weeklyCalendar.textContent = `Week ${getWeekNumber(selectedDate)}, ${selectedDate.getFullYear()}`;
        }
    }

    // Monthly
    const monthDays = document.getElementById('monthDays');
    if (monthDays) {
        monthDays.innerHTML = '';
        const firstDay = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), 1);
        const lastDay = new Date(selectedDate.getFullYear(), selectedDate.getMonth() + 1, 0);
        for (let i = 1; i <= lastDay.getDate(); i++) {
            const dayElement = document.createElement('div');
            dayElement.className = 'calendar-item';
            dayElement.textContent = i;
            if (i === selectedDate.getDate()) {
                dayElement.classList.add('selected');
            }
            dayElement.addEventListener('click', () => {
                selectedDate = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), i);
                updateCalendars();
                renderTodos('daily');
            });
            monthDays.appendChild(dayElement);
        }
        const monthlyCalendar = document.getElementById('monthlyCalendar');
        if (monthlyCalendar) {
            monthlyCalendar.textContent = selectedDate.toLocaleString('default', { month: 'long', year: 'numeric' });
        }
    }

    // Yearly
    const yearMonths = document.getElementById('yearMonths');
    if (yearMonths) {
        yearMonths.innerHTML = '';
        for (let i = 0; i < 12; i++) {
            const monthElement = document.createElement('div');
            monthElement.className = 'calendar-item';
            monthElement.textContent = new Date(selectedDate.getFullYear(), i, 1).toLocaleString('default', { month: 'long' });
            if (i === selectedDate.getMonth()) {
                monthElement.classList.add('selected');
            }
            monthElement.addEventListener('click', () => {
                selectedDate = new Date(selectedDate.getFullYear(), i, 1);
                updateCalendars();
                renderTodos('monthly');
            });
            yearMonths.appendChild(monthElement);
        }
        const yearlyCalendar = document.getElementById('yearlyCalendar');
        if (yearlyCalendar) {
            yearlyCalendar.textContent = selectedDate.getFullYear();
        }
    }
}

function getWeekNumber(d) {
    d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
    d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
    const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
    return Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
}

function addTask(section) {
    const inputId = `${section}TaskInput`;
    const listId = `${section}TaskList`;

    const taskInput = document.getElementById(inputId);
    const taskList = document.getElementById(listId);

    if (taskInput && taskInput.value.trim()) {
        const todo = {
            id: Date.now(),
            text: taskInput.value.trim(),
            done: false,
            date: selectedDate.toISOString()
        };
        todos[section].push(todo);
        saveToLocalStorage();
        renderTodos(section);
        taskInput.value = '';
    }
}

function toggleTask(section, id) {
    const todo = todos[section].find(t => t.id === id);
    if (todo) {
        todo.done = !todo.done;
        saveToLocalStorage();
        renderTodos(section);
    }
}

function deleteTask(section, id) {
    todos[section] = todos[section].filter(t => t.id !== id);
    saveToLocalStorage();
    renderTodos(section);
}

function renderTodos(section) {
    const list = document.getElementById(`${section}TaskList`);
    if (list) {
        list.innerHTML = '';
        todos[section].forEach(todo => {
            const todoDate = new Date(todo.date);
            let showTodo = false;
            switch (section) {
                case 'daily':
                    showTodo = todoDate.toDateString() === selectedDate.toDateString();
                    break;
                case 'weekly':
                    const weekStart = new Date(selectedDate);
                    weekStart.setDate(weekStart.getDate() - weekStart.getDay());
                    const weekEnd = new Date(weekStart);
                    weekEnd.setDate(weekEnd.getDate() + 6);
                    showTodo = todoDate >= weekStart && todoDate <= weekEnd;
                    break;
                case 'monthly':
                    showTodo = todoDate.getMonth() === selectedDate.getMonth() && todoDate.getFullYear() === selectedDate.getFullYear();
                    break;
                case 'yearly':
                    showTodo = todoDate.getFullYear() === selectedDate.getFullYear();
                    break;
            }
            if (showTodo) {
                const li = document.createElement('li');
                li.className = `task-item ${todo.done ? 'done' : ''}`;
                li.innerHTML = `
                    <span>${todo.text}</span>
                    <button class="delete-button">Delete</button>
                `;
                li.querySelector('span').addEventListener('click', () => toggleTask(section, todo.id));
                li.querySelector('.delete-button').addEventListener('click', (e) => {
                    e.stopPropagation();
                    deleteTask(section, todo.id);
                });
                list.appendChild(li);
            }
        });
    }
}

document.querySelectorAll('.add-todo').forEach(addTodo => {
    const input = addTodo.querySelector('input');
    const button = addTodo.querySelector('button');
    const section = addTodo.parentElement.querySelector('.todo-list').id.replace('TaskList', '');

    button.addEventListener('click', () => {
        if (input.value.trim()) {
            addTask(section);
        }
    });

    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && input.value.trim()) {
            addTask(section);
        }
    });
});

function initApp() {
    loadFromLocalStorage();
    updateCalendars();
    todoSections.forEach(section => renderTodos(section));
}

initApp();
