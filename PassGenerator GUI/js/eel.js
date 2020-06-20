// Makes sure the email function is disabled onload.
load = () => {
    let active = document.getElementById("emailInput");
    active.disabled = true;
}

// This is used to activate the email option.
// This acts as a toggle function. It can activate as well as deactivate the email option.
activateInput = () => {
    let active = document.getElementById("emailInput");
    let companyName = document.getElementById("emailTitle");

    // If the disabled value of the tag is false then it will make it true.
    if (active.disabled === false) {
        companyName.style.color = "rgb(255, 255, 255)";
        active.disabled = true;
    }
    // If the disabled value equal true this statement will make it false.
    else{
        active.disabled = false;
        companyName.style = "color: rgb(3, 169, 244); transition: 0.5s ease-in;";
    }
}

// This function is responsible for displaying the random password we receive from the Python code.
function get_password(val) {
    let password = val;

    // Unhides the block that will display the user password.
    let container = document.getElementById("passContainer");
    container.style = "display:block; transition: 0.5s ease-in;";
    document.getElementById("userPassword").value = password;
}

// Activates the Python code that is responsible for generating random password.
// Function also displays loading animation.
function activate_generator() {
    event.preventDefault();

    let animation = document.getElementById("loading");
    animation.style.display = "flex";

    setTimeout(() => {
        eel.generate_password()(get_password);
        animation.style.display = "none";
    }, 3000);

}