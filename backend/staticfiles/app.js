async function loadBooks() {
    const res = await fetch('/api/books/');
    const books = await res.json();
    const list = document.getElementById('bookList');
    list.innerHTML = '';

    books.forEach(b => {
        const li = document.createElement('li');
        li.innerHTML = `${b.title} — ${b.author} (${b.quantity})`;
        list.appendChild(li);
    });
}

async function addBook() {
    await fetch('/api/books/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            title: title.value,
            author: author.value,
            isbn: isbn.value,
            quantity: quantity.value
        })
    });
    loadBooks();
}

loadBooks();
