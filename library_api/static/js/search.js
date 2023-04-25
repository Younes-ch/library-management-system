const csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

const selectElement = document.getElementById("slct");
const formElement = document.getElementById("form");
const searchWrapper = document.getElementById("search-wrapper");
const searchBarWrapper = document.getElementsByClassName("search-bar")[0];
const searchResultsWrapper = document.getElementById("search-results-wrapper");

selectElement.addEventListener("change", (event) => {
    searchWrapper.style.display = "block";
    switch (event.target.value) {
        case "title":
        case "author":
        case "genre":
            searchBarWrapper.innerHTML = `
            <ion-icon name="search-outline"></ion-icon> <input class="search-bar-input" required>
            <label>Search</label>`;
            var searchBarInput = document.getElementsByClassName("search-bar-input")[0];
            searchBarInput.setAttribute("placeholder", `Search by ${selectElement.value}`);
            break;
        case "year":
            searchBarWrapper.innerHTML = `
            <select id="select-year" required>
                <option value="" disabled selected>Choose a year</option>
            </select>`;
            var selectYear = document.getElementById("select-year");
            url = "http://127.0.0.1:8000/api/getAllYears/"
            fetch(url)
                .then((response) => response.json())
                .then((data) => {
                    data.forEach((year) => {
                        var option = document.createElement("option");
                        option.value = year;
                        option.text = year;
                        selectYear.appendChild(option);
                    });
                });
            break;
        }
    if (searchBarInput)
        searchBarInput.value="";
});

formElement.addEventListener("submit", (event) => {
    event.preventDefault();
    let searchValue;
    let searchBy;
    const searchBarInput = document.getElementsByClassName("search-bar-input")[0];
    const selectYear = document.getElementById("select-year");
    if (selectYear) {
        searchValue = selectYear.value;
        searchBy = selectElement.value;
    } else if (searchBarInput.value) {
        searchValue = searchBarInput.value;
        searchBy = selectElement.value;
    }
    const url = `http://127.0.0.1:8000/api/books/search/${searchBy}/${searchValue}`;
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            if (data.length === 0) {
                console.log("No results found.");
                const noResultsFound = document.createElement("h3");
                searchResultsWrapper.appendChild(noResultsFound);
                noResultsFound.innerHTML = "No results found.";
            } else {
                const searchResults = document.createElement("div");
                searchResults.id = "search-results";
                searchResultsWrapper.appendChild(searchResults);
                console.log(data);
                data.forEach((book) => {
                const link = document.createElement("a");
                link.className = "book-link";
                link.href = book.link;
                link.target = "_blank";
                const bookDiv = document.createElement("div");
                link.appendChild(bookDiv);
                bookDiv.className = "card";
                const bookTitleDiv = document.createElement("div");
                bookTitleDiv.className = "book-title";
                bookTitleDiv.innerHTML = book.title;
                bookDiv.appendChild(bookTitleDiv);
                const bookAuthorDiv = document.createElement("div");
                bookAuthorDiv.className = "book-info";
                bookAuthorDiv.innerHTML = book.author;
                bookDiv.appendChild(bookAuthorDiv);
                const bookGenreDiv = document.createElement("div");
                bookGenreDiv.className = "book-info";
                bookGenreDiv.innerHTML = book.genre;
                bookDiv.appendChild(bookGenreDiv);
                const bookYearDiv = document.createElement("div");
                bookYearDiv.className = "book-info";
                bookYearDiv.innerHTML = book.publishing_year;
                bookDiv.appendChild(bookYearDiv);
                const bookPagesDiv = document.createElement("div");
                bookPagesDiv.className = "book-info";
                bookPagesDiv.innerHTML = book.pages + " Pages";
                bookDiv.appendChild(bookPagesDiv);
                const bookChaptersDiv = document.createElement("div");
                bookChaptersDiv.className = "book-info";
                bookChaptersDiv.innerHTML = book.chapters + " Chapters";
                bookDiv.appendChild(bookChaptersDiv);
                searchResults.appendChild(link);
            })}
        })
        searchResultsWrapper.innerHTML = "";
});

function scrollToResults() {
    const searchBarInput = document.getElementsByClassName("search-bar-input")[0];
    const selectYear = document.getElementById("select-year");
    const resultsDiv = document.getElementById("search-results-wrapper");
    if (selectYear) {
        if (selectYear.value) {
            resultsDiv.scrollIntoView({behavior: "smooth"});
        }
    } else if (searchBarInput.value) {
        resultsDiv.scrollIntoView({behavior: "smooth"});
    }
}

window.onload = () => {
    formElement.reset();
};


