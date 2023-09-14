// Task 5: updates the text of the header element to New Header!!!
// when the user clicks on the element with id update_header
const update_header = document.querySelector("#update_header")

update_header.addEventListener("click", function () {
    const header = document.querySelector("header")
    header.replaceWith("New Header!!!")
})
