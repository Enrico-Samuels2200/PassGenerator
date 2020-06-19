load = () => {
    let active = document.getElementById("emailInput");
    active.disabled = true;
}

activateInput = () => {
    let active = document.getElementById("emailInput");
    let companyName = document.getElementById("emailTitle");

    if (active.disabled === false) {
        companyName.style.color = "rgb(255, 255, 255)";
        active.disabled = true;
    }
    else{
        active.disabled = false;
        companyName.style = "color: rgb(3, 169, 244); transition: 0.5s ease-in;";
    }
}

function get_password(val) {
    let password = val;
    console.log('Got this from Python: ' + password);

    let container = document.getElementById("passContainer");
    container.style = "display:block; transition: 0.5s ease-in;";
    document.getElementById("userPassword").value = password;
}

function activate_generator() {
    event.preventDefault();
    eel.generate_password()(get_password);
}