window.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.getElementById("menuToggle");
    const mobileNav = document.getElementById("mobileNav");
    const closeMenu = document.getElementById("closeMenu");
  
    menuToggle.addEventListener("click", () => {
      mobileNav.classList.add("show");
    });
  
    closeMenu.addEventListener("click", () => {
      mobileNav.classList.remove("show");
    });
  
    // Simulate login state
    const loggedIn = true; // change to false to test
  
    const authSection = document.getElementById("authSection");
    const mobileAuth = document.getElementById("mobileAuth");
  
    if (loggedIn) {
      authSection.innerHTML = `
        <div class="profile-dropdown">
          <img src="../../local_static/images/user-profile.jpg" alt="User" class="profile-img" id="profileToggle">
          <div class="dropdown-menu" id="profileMenu">
            <a href="#">Profile</a>
            <a href="#">Logout</a>
          </div>
        </div>
        <a href="#" class="outline-btn">Let's Work</a>
      `;
  
      mobileAuth.innerHTML = `
        <a href="#">Profile</a>
        <a href="#">Logout</a>
      `;
  
      // Toggle profile dropdown
      document.addEventListener("click", (e) => {
        const profileToggle = document.getElementById("profileToggle");
        const profileMenu = document.getElementById("profileMenu");
  
        if (!profileToggle || !profileMenu) return;
  
        if (e.target === profileToggle) {
          profileMenu.style.display = profileMenu.style.display === "block" ? "none" : "block";
        } else {
          profileMenu.style.display = "none";
        }
      });
  
    } else {
      authSection.innerHTML = `
        <a href="#">Login</a>
        <a href="#" class="outline-btn">Let's Work</a>
      `;
  
      mobileAuth.innerHTML = `
        <a href="#">Login</a>
      `;
    }
  });


  const tabs = document.querySelectorAll('.tab');
  const contents = document.querySelectorAll('.package-content');
  
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      // Remove all active
      tabs.forEach(t => t.classList.remove('active'));
      contents.forEach(c => c.classList.add('hidden'));
  
      // Add current
      tab.classList.add('active');
      const current = document.getElementById(tab.dataset.package);
      current.classList.remove('hidden');
    });
  });
  