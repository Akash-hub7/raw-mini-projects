function showForm() {
    document.getElementById("contactForm").style.display = "block";
}

// Hide Contact Form
function hideForm() {
    document.getElementById("contactForm").style.display = "none";
}

// Search Contacts
function searchContacts() {

    let input = document.getElementById("searchInput");
    let filter = input.value.toLowerCase();

    let contactList = document.getElementById("contactList");
    let contacts = contactList.getElementsByClassName("contact-card");

    for (let i = 0; i < contacts.length; i++) {

        let name = contacts[i]
            .querySelector(".contact-details h3")
            .textContent.toLowerCase();

        let phone = contacts[i]
            .querySelector(".contact-details p")
            .textContent.toLowerCase();

        let email = contacts[i]
            .querySelector(".contact-details small")
            .textContent.toLowerCase();

        if (
            name.includes(filter) ||
            phone.includes(filter) ||
            email.includes(filter)
        ) {
            contacts[i].style.display = "flex";
        } else {
            contacts[i].style.display = "none";
        }
    }
}
