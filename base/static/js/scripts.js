// Search filter input
const searchInput = document.getElementById('search');

const searchFormOnSubmit = event => {
    // Prevents form from being submitted to the server if search filter is empty
    if (searchInput.value === "") event.preventDefault();
}