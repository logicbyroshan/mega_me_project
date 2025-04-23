document.addEventListener("DOMContentLoaded", function () {
  // Menu-tab toggle for each section
  const blogLinks = document.querySelectorAll(".blog-profile-header ul li a");
  const blogCards = document.querySelectorAll(".your-blogs, .your-freelance, .start-new-work, .post-reviews, .latest-fromme");

  blogLinks.forEach(link => {
      link.addEventListener("click", (e) => {
          e.preventDefault();
          const target = link.getAttribute("href").replace("#", "");

          blogCards.forEach(card => {
              if (card.closest(".blog-content") && card.classList.contains(target)) {
                  card.style.display = "block";
              } else {
                  card.style.display = "none";
              }
          });
      });
  });


  // Edit sidebar details inline
  const editButtons = document.querySelectorAll(".profile-details button");

  editButtons.forEach((btn) => {
      btn.addEventListener("click", () => {
          const parent = btn.parentElement;
          const currentText = parent.childNodes[0].nodeValue.trim();
          const input = document.createElement("input");
          input.value = currentText;
          parent.insertBefore(input, btn);
          parent.removeChild(parent.childNodes[0]);

          btn.textContent = "Save";
          btn.addEventListener("click", () => {
              const newVal = input.value;
              parent.insertBefore(document.createTextNode(newVal + " "), input);
              parent.removeChild(input);
              btn.textContent = "Edit";
          }, { once: true });
      });
  });
});


// Function to handle the "Profile"
document.querySelectorAll('.edit-btn').forEach(button => {
    button.addEventListener('click', () => {
      const item = button.closest('.profile-item');
      const field = item.dataset.field;
      const left = item.querySelector('.left');
      const span = item.querySelector('.editable');

      // If input already exists, do nothing
      if (left.querySelector('.edit-input')) return;

      const input = document.createElement('input');
      input.className = 'edit-input';
      input.type = 'text';
      input.value = span.textContent.trim();

      left.appendChild(input);
      input.focus();

      // Update button text temporarily
      button.textContent = 'Save';

      input.addEventListener('keydown', async (e) => {
        if (e.key === 'Enter') {
          const newValue = input.value.trim();
          
          // Send to backend (adjust URL and method as needed)
          try {
            const response = await fetch('/update-profile', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ field, value: newValue }),
            });

            if (response.ok) {
              // Optionally: you can keep the old span text OR update it
              // span.textContent = newValue;
              input.remove();
              button.textContent = 'Edit';
            } else {
              alert('Failed to save. Try again.');
            }
          } catch (error) {
            alert('Error contacting backend.');
          }
        }
      });

      // Optional: handle focus out (clicking away)
      input.addEventListener('blur', () => {
        input.remove();
        button.textContent = 'Edit';
      });
    });
  });

  const uploadTrigger = document.getElementById("uploadTrigger");
  const fileInput = document.getElementById("fileInput");

  uploadTrigger.addEventListener("click", () => {
    fileInput.click();
  });

  fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    if (file) {
      // 👇 Upload logic here or preview
      console.log("Selected file:", file);

      // Optional preview
      const reader = new FileReader();
      reader.onload = function (e) {
        document.querySelector(".image-container img").src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });
