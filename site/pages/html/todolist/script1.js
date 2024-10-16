document.addEventListener('DOMContentLoaded', () => {
    
    (function() {
        const originalFetch = fetch;
        window.fetch = function() {
            arguments[1] = arguments[1] || {};
            arguments[1].headers = arguments[1].headers || {};
            arguments[1].headers['ngrok-skip-browser-warning'] = 'true';
            return originalFetch.apply(this, arguments);
        };
    })();

    const addTodoForm = document.getElementById('addTodoForm');
    const todoItem = document.getElementById('todoItem');
    const todoDate = document.getElementById('todoDate');
    let currentDate = new Date();

    function loadCalendars() {
        loadDayCalendar();
        loadWeekCalendar();
        loadMonthCalendar();
        loadYearCalendar();
    }

    function loadDayCalendar() {
        const calendarDiv = document.getElementById('dayCalendar');
        calendarDiv.innerHTML = '';

        const dayElement = document.createElement('div');
        dayElement.className = 'calendar-day selected';
        dayElement.textContent = formatDate(currentDate);
        dayElement.onclick = () => showAddTodoForm(currentDate);
        calendarDiv.appendChild(dayElement);

        loadTodos('day', currentDate);
    }

    function loadWeekCalendar() {
        const weekDiv = document.getElementById('weekCalendar');
        weekDiv.innerHTML = '';

        const startOfWeek = new Date(currentDate);
        startOfWeek.setDate(currentDate.getDate() - currentDate.getDay());

        for (let i = 0; i < 7; i++) {
            const date = new Date(startOfWeek);
            date.setDate(startOfWeek.getDate() + i);

            const weekElement = document.createElement('div');
            weekElement.className = 'calendar-week-day';
            weekElement.textContent = date.getDate(); // Display only the day
            weekElement.onclick = () => {
                currentDate = new Date(date);
                loadDayCalendar();
            };
            weekDiv.appendChild(weekElement);
        }
    }

    function loadMonthCalendar() {
        const calendarDiv = document.getElementById('monthCalendar');
        calendarDiv.innerHTML = '';

        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        for (let i = 1; i <= daysInMonth; i++) {
            const dayElement = document.createElement('div');
            dayElement.className = 'calendar-day';
            dayElement.textContent = i;
            if (i === currentDate.getDate()) {
                dayElement.classList.add('selected');
            }
            const day = new Date(year, month, i);
            dayElement.onclick = () => {
                selectDate(day);
                showAddTodoForm(day);
            };
            calendarDiv.appendChild(dayElement);
        }

        loadTodos('month', currentDate);
    }

    function loadYearCalendar() {
        const calendarDiv = document.getElementById('yearCalendar');
        calendarDiv.innerHTML = '';

        const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

        monthNames.forEach((month, index) => {
            const monthElement = document.createElement('div');
            monthElement.className = 'calendar-day';
            monthElement.textContent = month;
            if (index === currentDate.getMonth()) {
                monthElement.classList.add('selected');
            }
            const firstDayOfMonth = new Date(currentDate.getFullYear(), index, 1);
            monthElement.onclick = () => {
                selectDate(firstDayOfMonth);
                showAddTodoForm(firstDayOfMonth);
            };
            calendarDiv.appendChild(monthElement);
        });

        loadTodos('year', currentDate);
    }

    function selectDate(date) {
        currentDate = date;
        loadCalendars();
    }

    function loadTodos(view, date) {
        let startDate, endDate;

        if (view === 'day') {
            startDate = endDate = date;
        } else if (view === 'week') {
            startDate = new Date(date.getFullYear(), date.getMonth(), date.getDate() - date.getDay());
            endDate = new Date(startDate.getFullYear(), startDate.getMonth(), startDate.getDate() + 6);
        } else if (view === 'month') {
            startDate = new Date(date.getFullYear(), date.getMonth(), 1);
            endDate = new Date(date.getFullYear(), date.getMonth() + 1, 0);
        } else if (view === 'year') {
            startDate = new Date(date.getFullYear(), 0, 1);
            endDate = new Date(date.getFullYear(), 11, 31);
        }

        const todos = getTodos(formatDate(startDate), formatDate(endDate));
        const todosDiv = document.getElementById(`${view}Todos`);
        todosDiv.innerHTML = '';
        todos.forEach(todo => {
            const todoElement = document.createElement('div');
            todoElement.className = 'todo-item';
            const [todoDate, todoContent] = todo.split(': - ');
            const isDone = todoContent.startsWith('[x]');
            todoElement.textContent = `${todoDate}: ${todoContent.substring(4)}`;
            if (isDone) {
                todoElement.classList.add('done');
            }
            todoElement.onclick = () => toggleTodo(todoDate, todoContent.substring(4), isDone);
            todosDiv.appendChild(todoElement);
        });
    }

    function toggleTodo(date, content, currentStatus) {
        const todos = JSON.parse(localStorage.getItem('todos') || '[]');
        const index = todos.findIndex(todo => todo.startsWith(`${date}: - `));
        if (index !== -1) {
            const newStatus = currentStatus ? '[ ]' : '[x]';
            todos[index] = `${date}: - ${newStatus} ${content}`;
            localStorage.setItem('todos', JSON.stringify(todos));
            loadCalendars();
        }
    }

    function showAddTodoForm(date) {
        todoDate.value = formatDate(date);
        todoItem.focus();
    }

    addTodoForm.onsubmit = (e) => {
        e.preventDefault();
        addTodo(todoDate.value, todoItem.value);
        loadCalendars();
        todoItem.value = '';
    };

    function formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    function addTodo(date, item) {
        const todos = JSON.parse(localStorage.getItem('todos') || '[]');
        todos.push(`${date}: - [ ] ${item}`);
        localStorage.setItem('todos', JSON.stringify(todos));
    }

    function getTodos(startDate, endDate) {
        const todos = JSON.parse(localStorage.getItem('todos') || '[]');
        return todos.filter(todo => {
            const todoDate = new Date(todo.split(':')[0]);
            return todoDate >= new Date(startDate) && todoDate <= new Date(endDate);
        });
    }

    document.addEventListener("DOMContentLoaded", function() {
        loadCalendars();
    });

});