function submitForm(event) {
    event.preventDefault();

    // Get form values
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var age = document.getElementById("age").value;

    // Validate data
    if (!validateName() || !validateEmail() || age === "") {
        alert("Please fix the errors before submitting.");
        return;
    }

    // Display submitted data
    alert("Submitted Data:\nName: " + name + "\nEmail: " + email + "\nAge: " + age);

    // You can send the data to the server or perform additional actions here
}

function validateName() {
    var nameInput = document.getElementById("name");
    var nameError = document.getElementById("nameError");
    var isValid = /^[a-zA-Z]+$/.test(nameInput.value);

    if (isValid) {
        nameError.innerHTML = "";
    } else {
        nameError.innerHTML = "Name should contain only alphabets";
    }

    return isValid;
}

function validateEmail() {
    var emailInput = document.getElementById("email");
    var emailError = document.getElementById("emailError");
    var isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value);

    if (isValid) {
        emailError.innerHTML = "";
    } else {
        // emailError.innerHTML = "Invalid email address";
    }

    return isValid;
}
function validateEmail() {
    var emailInput = document.getElementById("email");
    var emailError = document.getElementById("emailError");
    var isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value);

    if (isValid) {
        emailError.innerHTML = "";
    } else {
        // emailError.innerHTML = "Invalid email address";
    }

    return isValid;
}
