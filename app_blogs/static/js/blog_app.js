document.addEventListener("DOMContentLoaded", function () {
    const categoryNavItem = document.querySelector(".nav-list li:nth-child(3)"); // Assuming "Categories" is the 3rd item
    const dropdownMenu = document.querySelector(".dropdown-menu");

    categoryNavItem.addEventListener("mouseenter", () => {
        dropdownMenu.style.display = "flex";
    });

    categoryNavItem.addEventListener("mouseleave", () => {
        setTimeout(() => {
            if (!dropdownMenu.matches(":hover")) {
                dropdownMenu.style.display = "none";
            }
        }, 300);
    });

    dropdownMenu.addEventListener("mouseleave", () => {
        dropdownMenu.style.display = "none";
    });
});
