function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


async function loadBooks() {
    const res = await fetch('/api/books/');
    const books = await res.json();
    const list = document.getElementById('bookList');
    list.innerHTML = '';

    books.forEach(b => {
        const li = document.createElement('li');
        li.innerHTML = `
            ID: ${b.id} |
            Title: <input type="text" id="title-${b.id}" value="${b.title}"> |
            Author: <input type="text" id="author-${b.id}" value="${b.author}"> |
            ISBN: <input type="text" id="isbn-${b.id}" value="${b.isbn}"> |
            Quantity: <input type="number" id="quantity-${b.id}" value="${b.quantity}"> 
            <button onclick="updateBook(${b.id})">Save</button>
            <button onclick="deleteBook(${b.id})">Delete</button>
        `;
        list.appendChild(li);
    });
}

async function addBook() {
    await fetch('/api/books/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
            title: title.value,
            author: author.value,
            isbn: isbn.value,
            quantity: quantity.value
        })
    });
    loadBooks();
}

async function updateBook(bookId) {
    const newTitle = document.getElementById(`title-${bookId}`).value;
    const newAuthor = document.getElementById(`author-${bookId}`).value;
    const newIsbn = document.getElementById(`isbn-${bookId}`).value;
    const newQuantity = document.getElementById(`quantity-${bookId}`).value;

    await fetch(`/api/books/${bookId}/`, {
        method: 'PATCH', 
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            title: newTitle,
            author: newAuthor,
            isbn: newIsbn,
            quantity: newQuantity
        })
    });
    loadBooks();
}

async function borrowBook(id) {
    await fetch('/api/loans/borrow/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({book_id: id})
    });
    loadBooks();
}

async function deleteBook(id) {
    await fetch(`/api/books/${id}/`, {method: 'DELETE'});
    loadBooks();
}

loadBooks();

async function register() {
    await fetch('/api/accounts/register/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    });
}

async function updateUser() {
    await fetch(`/api/accounts/${userid.value}/`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json',
        },
        body: JSON.stringify({username: newusername.value})
    });
}

async function deleteUser() {
    await fetch(`/api/accounts/${userid.value}/`, {method: 'DELETE'});
}

async function loadLoans() {
    const res = await fetch('/api/loans/');
    const loans = await res.json();
    const list = document.getElementById('loanList');
    list.innerHTML = '';

    loans.forEach(l => {
        const li = document.createElement('li');
        li.innerHTML = `
            Loan #${l.id} — Book ${l.book} — User ${l.user}
            <button onclick="deleteLoan(${l.id})">Delete</button>
        `;
        list.appendChild(li);
    });
}

async function deleteLoan(id) {
    await fetch(`/api/loans/${id}/`, {method: 'DELETE'});
    loadLoans();
}

async function loadUsers() {
    const res = await fetch('/api/accounts/');
    const users = await res.json();
    const list = document.getElementById('userList');
    list.innerHTML = '';

    users.forEach(u => {
        const li = document.createElement('li');
        li.innerHTML = `
            ${u.id} — ${u.username}
            <button onclick="deleteUserById(${u.id})">Delete</button>
        `;
        list.appendChild(li);
    });
}

async function deleteUserById(id) {
    await fetch(`/api/accounts/${id}/`, {method: 'DELETE'});
    loadUsers();
}

