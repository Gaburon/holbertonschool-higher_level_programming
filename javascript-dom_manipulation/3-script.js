// Task 3:  toggles the class of the header element when the user
// clicks on the tag id toggle_header
const toggle_header = document.querySelector("#toggle_header")

toggle_header.addEventListener("click", function () {
    const header = document.querySelector("header")
    if (header.classList == "green") {
        header.classList.replace("green", "red")
    }
    else {
        header.classList.replace("red", "green")
    }
})
