// Task 4: adds a li element to a list when the user clicks on
//the element with id add_item

const add_item = document.querySelector("#add_item")
const list = document.querySelector("ul.my_list")
add_item.addEventListener("click", function () {
    const li_item = document.createElement("li");
    li_item.innerHTML = "item";
    list.appendChild(li_item)
})
