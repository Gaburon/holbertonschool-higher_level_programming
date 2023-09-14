// Task 2: Write a JavaScript script that adds the class red to the header
// element when the user clicks on the tag with id red_header
const redheader = document.getElementById("red_header")
redheader.addEventListener("click", add_class())

function add_class() {
    const header = document.querySelector("header")
    header.classList.add("red")
}
