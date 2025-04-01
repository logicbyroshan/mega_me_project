
// Function to toggle the active category within its container
function toggleCategory(element) {
    const container = element.closest('.cards-categories'); // Get the parent container
    const categories = container.querySelectorAll('.category'); // Scope to this container
  
    // Remove active class from all categories in this container
    categories.forEach(category => category.classList.remove('active'));
  
    // Add active class to clicked category
    element.classList.add('active');
  }
  
  
  // sort button sort items
  document.addEventListener("DOMContentLoaded", () => {
      // Get all buttons and dropdowns
      const sortButtons = document.querySelectorAll(".cards-sort .view-btn");
    
      sortButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
          const parent = event.target.closest(".cards-sort");
          const dropdown = parent.querySelector(".sort-items");
    
          // Close other open dropdowns
          document.querySelectorAll(".sort-items").forEach((menu) => {
            if (menu !== dropdown) {
              menu.style.display = "none";
            }
          });
    
          // Toggle the visibility of the current dropdown
          dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
        });
      });
    
      // Close dropdowns when clicking outside
      document.addEventListener("click", (event) => {
        if (!event.target.closest(".cards-sort")) {
          document.querySelectorAll(".sort-items").forEach((menu) => {
            menu.style.display = "none";
          });
        }
      });
    });
    