const csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

const formWrapper = document.getElementById("form-wrapper");
const form = document.getElementById("form");

const title = document.querySelector("#title-input-wrapper > .search-bar > input");
const author = document.querySelector("#author-input-wrapper > .search-bar > input");
const genre = document.querySelector("#genre-input-wrapper > .search-bar > input");
const year = document.querySelector("#year-input-wrapper > .search-bar > input");
const pages = document.querySelector("#pages-input-wrapper > .search-bar > input");
const chapters = document.querySelector("#chapters-input-wrapper > .search-bar > input");

form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (year.value && (isNaN(year.value) || year.value < 1800 || year.value > 2023)) {
        alert("Please enter a valid year. (1800-2023)");
        return;
    }
    const url = "http://127.0.0.1:8000/api/books/add/";
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf_token,
        },
        body: JSON.stringify({
            title: title.value,
            author: author.value,
            genre: genre.value,
            publishing_year: year.value,
            pages: pages.value,
            chapters: chapters.value,
        }),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("Success:", data);
            formWrapper.innerHTML = `<h3>Book added successfully!</h3>`;
        }
    );
});

window.onload = () => {
    form.reset();
}

