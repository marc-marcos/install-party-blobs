let countMint = 0;
let countUbuntu = 0;
let countDebian = 0;
let countManjaro = 0;
let countArch = 0;
let sum = 0;
let username;

function sentToBackend(username, os) {
    const url = 'http://127.0.0.1:5000/create';
    const data = { "username": username, "os": os };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function addMint() {
    if((username = prompt("Afegir nom de l'estudiant"))) {
        ++countMint;
        ++sum;
        document.getElementById("mint").innerHTML = countMint;
        document.getElementById("total").innerHTML = sum;
        sentToBackend(username, "Linux Mint");
    } 
}
function addUbuntu() {
    if((username = prompt("Afegir nom de l'estudiant"))) {
        ++countUbuntu;
        ++sum;
        document.getElementById("ubuntu").innerHTML = countUbuntu;
        document.getElementById("total").innerHTML = sum;
        sentToBackend(username, "Ubuntu");
    }
}
function addDebian() {
    if((username = prompt("Afegir nom de l'estudiant"))) {
        ++countDebian;
        ++sum;
        document.getElementById("debian").innerHTML = countDebian;
        document.getElementById("total").innerHTML = sum;
        sentToBackend(username, "Debian");
    }
}
function addManjaro() {
    if((username = prompt("Afegir nom de l'estudiant"))) {
        ++countManjaro;
        ++sum;
        document.getElementById("manjaro").innerHTML = countManjaro;
        document.getElementById("total").innerHTML = sum;
        sentToBackend(username, "Manjaro");
    }
}
function addArch() {
    if((username = prompt("Afegir nom de l'estudiant"))) {
        ++countArch;
        ++sum;
        document.getElementById("arch").innerHTML = countArch;
        document.getElementById("total").innerHTML = sum;
        sentToBackend(username, "Arch");
    }
}

