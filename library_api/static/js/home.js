const bookLinks = document.querySelectorAll('.book-link');
bookLinks.forEach(book => {
    book.addEventListener('mouseover', () => {
       book.parentNode.style.backgroundColor = '#000000d7';
    })
    book.addEventListener('mouseout', () => {
        book.parentNode.style.backgroundColor = '#00000071';
    })
});