// Dummy credentials
const dummyEmail = "test@fruit.ai";
const dummyPassword = "password123";

// Get form and error message elements
const form = document.getElementById('loginForm');
const errorMessage = document.getElementById('errorMessage');

// Add event listener for form submission
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way

    // Get user input
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Check if the credentials match
    if (email === dummyEmail && password === dummyPassword) {
        // Redirect to homepage (replace 'homepage.html' with your actual page)
        window.location.href = 'home.html';
    } else {
        // Show error message
        errorMessage.style.display = 'block';
    }
});
