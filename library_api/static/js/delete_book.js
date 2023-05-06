const deleteButtons = document.querySelectorAll('.delete-button');

deleteButtons.forEach(button => {
    button.addEventListener('click', () => {
        response = confirm("Are you sure you want to delete this book?");
        if (response) {
            const bookID = button.id.split('-')[2];
            const url = `http://127.0.0.1:8000/api/books/delete/${bookID}`;
            fetch(url, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                }})
                .then((response) => response.json())
                .then((data) => {
                    console.log("Success:", data);
                    window.location.href = "http://127.0.0.1:8000/";
                });
        }})
})