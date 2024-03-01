// script.js
function generateKey() {
    // Generate random keys (you can customize this logic)
    const key1 = Math.random().toString(36).substr(2, 8); // Example: abc12345
    const key2 = Math.random().toString(36).substr(2, 8); // Example: xyz98765

    // Display generated keys in the input fields
    document.getElementById('key1').value = key1;
    document.getElementById('key2').value = key2;
}

function checkLogin() {
    const userId = document.getElementById('userId').value;
    const key1 = document.getElementById('key1').value;
    const key2 = document.getElementById('key2').value;

    // Check if keys match (you can implement your own logic here)
    if (key1 === 'correctKey1' && key2 === 'correctKey2') {
        document.getElementById('loginMessage').textContent = 'Login Successful';
    } else {
        document.getElementById('loginMessage').textContent = 'Wrong credentials';
    }
}

function registerUser() {
    const newUserId = document.getElementById('newUserId').value;
    const newEmail = document.getElementById('newEmail').value;

    // Save new user to database (you can use backend APIs for this)
    // Display registration success message
    document.getElementById('registrationMessage').textContent = 'You are now registered';
}
