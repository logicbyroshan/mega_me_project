document.addEventListener("DOMContentLoaded", function () {
    const decreaseButtons = document.querySelectorAll(".decrease");
    const increaseButtons = document.querySelectorAll(".increase");
    const removeButtons = document.querySelectorAll(".remove-item");
    const totalCost = document.getElementById("total-cost");

    function updateTotal() {
        let total = 0;
        document.querySelectorAll(".cart-item").forEach(item => {
            const price = parseFloat(item.querySelector(".price").textContent.replace("₹", ""));
            const quantity = parseInt(item.querySelector(".quantity-value").textContent);
            total += price * quantity;
        });
        totalCost.textContent = `₹${total.toFixed(2)}`;
    }

    decreaseButtons.forEach(button => {
        button.addEventListener("click", function () {
            let quantityElement = this.nextElementSibling;
            let quantity = parseInt(quantityElement.textContent);
            if (quantity > 1) {
                quantityElement.textContent = quantity - 1;
                updateTotal();
            }
        });
    });

    increaseButtons.forEach(button => {
        button.addEventListener("click", function () {
            let quantityElement = this.previousElementSibling;
            let quantity = parseInt(quantityElement.textContent);
            quantityElement.textContent = quantity + 1;
            updateTotal();
        });
    });

    updateTotal();
});


// Function for breadcrumbs

// Example JavaScript to allow clicking on a breadcrumb item to mark it as active.
document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll('.breadcrumb ul li');
  
    items.forEach(item => {
      item.addEventListener('click', function () {
        // Remove 'active' from all items
        items.forEach(i => i.classList.remove('active'));
        // Add 'active' class to the clicked item
        this.classList.add('active');
      });
    });
  });
  

  function goHome() {
    // You can replace this with your actual redirect logic
    window.location.href = "/dashboard"; // Replace with your desired route
  }
function goToCheckout() {
    // You can replace this with your actual redirect logic
    window.location.href = "/checkout"; // Replace with your desired route
  }  



  document.addEventListener('DOMContentLoaded', function() {
    const addressSelect = document.getElementById('addressSelect');
    const newAddressForm = document.getElementById('newAddressForm');
    const saveAddress = document.getElementById('saveAddress');
  
    // Toggle new address form based on selection
    addressSelect.addEventListener('change', function() {
      if (this.value === 'new') {
        newAddressForm.classList.remove('hidden');
      } else {
        newAddressForm.classList.add('hidden');
      }
    });
  
    // Save new address simulation
    saveAddress.addEventListener('click', function() {
      const addressName = document.getElementById('addressName').value.trim();
      if(addressName === '') {
        alert('Please provide a name for your address.');
        return;
      }
      
      const option = document.createElement('option');
      option.value = addressName.toLowerCase();
      option.textContent = addressName;
      addressSelect.appendChild(option);
      addressSelect.value = addressName.toLowerCase();
      
      newAddressForm.classList.add('hidden');
      document.getElementById('addressName').value = '';
      document.getElementById('addressLine').value = '';
      document.getElementById('city').value = '';
      document.getElementById('pincode').value = '';
      
      alert('Address saved successfully!');
    });
  
    const checkoutForm = document.getElementById('checkoutForm');
    checkoutForm.addEventListener('submit', function(e) {
      e.preventDefault();
      // Handle checkout form submission and payment process here.
      alert('Proceeding to payment...');
    });
  });
  