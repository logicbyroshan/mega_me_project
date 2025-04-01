//Home skills typing 
document.addEventListener("DOMContentLoaded", () => {
    const skillText = document.getElementById("skill-text");
    const skills = ["Python Developer", "Web Developer", "Full Stack Developer", "AI-ML Enthusiast"]; // Add more skills here
    let currentSkill = 0;
    let charIndex = 0;
    let typingSpeed = 100; // Typing speed in milliseconds
    let erasingSpeed = 50; // Erasing speed in milliseconds
    let delayBetweenSkills = 1500; // Delay before typing the next skill
    
    function typeSkill() {
      if (charIndex < skills[currentSkill].length) {
        skillText.textContent += skills[currentSkill].charAt(charIndex);
        charIndex++;
        setTimeout(typeSkill, typingSpeed);
      } else {
        setTimeout(eraseSkill, delayBetweenSkills);
      }
    }
  
    function eraseSkill() {
      if (charIndex > 0) {
        skillText.textContent = skills[currentSkill].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(eraseSkill, erasingSpeed);
      } else {
        currentSkill = (currentSkill + 1) % skills.length; // Loop through the skills array
        setTimeout(typeSkill, typingSpeed);
      }
    }
  
    // Start the typing effect
    setTimeout(typeSkill, delayBetweenSkills);
  });
  


document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("popup-modal");
    const previewContainer = modal.querySelector(".preview-container");
    const closeButton = modal.querySelector(".close-btn");

    function openModal(content) {
        previewContainer.innerHTML = content;
        modal.style.display = "block";
    }

    // Handle "View Certificate" Button Click
    document.querySelectorAll(".view-certificate-btn").forEach(button => {
        button.addEventListener("click", function () {
            const certificate = this.getAttribute("data-certificate");
            let content = "";

            if (certificate.endsWith(".pdf")) {
                content = `<iframe src="${certificate}" width="100%" height="400px"></iframe>`;
            } else {
                content = `<img src="${certificate}" alt="Certificate Preview">`;
            }
            content += `<br><a href="${certificate}" download>Download Certificate</a>`;

            openModal(content);
        });
    });

    // Handle "View Resources" Button Click
    document.querySelectorAll(".view-resources-btn").forEach(button => {
        button.addEventListener("click", function () {
            const resources = JSON.parse(this.getAttribute("data-resources"));
            let content = "<h3>Resources</h3>";

            resources.forEach(resource => {
                if (resource.type === "image") {
                    content += `<img src="${resource.url}" alt="Resource Image"><br>`;
                } else if (resource.type === "pdf") {
                    content += `<iframe src="${resource.url}" width="100%" height="400px"></iframe><br>`;
                } else if (resource.type === "video") {
                    content += `<iframe width="100%" height="300px" src="${resource.url}" frameborder="0" allowfullscreen></iframe><br>`;
                } else if (resource.type === "link") {
                    content += `<a href="${resource.url}" target="_blank">${resource.url}</a><br>`;
                }
            });

            openModal(content);
        });
    });

    // Close Button
    closeButton.addEventListener("click", function () {
        modal.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("popup-modal");

    modal.addEventListener("wheel", function (event) {
        event.stopPropagation(); // Prevents background scroll when scrolling inside popup
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const faqs = document.querySelectorAll(".faq-card");

    faqs.forEach((faq) => {
        faq.addEventListener("click", function () {
            const answer = faq.querySelector(".faq-answer");
            const icon = faq.querySelector(".faq-icon");

            // Get the icons from the HTML attributes
            const openIcon = faq.getAttribute("data-open-icon");
            const closeIcon = faq.getAttribute("data-close-icon");

            if (faq.classList.contains("active")) {
                faq.classList.remove("active");
                answer.style.display = "none";
                icon.src = openIcon; // Switch to plus icon
            } else {
                faq.classList.add("active");
                answer.style.display = "block";
                icon.src = closeIcon; // Switch to minus icon
            }
        });
    });
});


// Slider functionality
let sliderIndex = 0;
const slides = document.querySelectorAll(".slide");
const slider = document.querySelector(".slider");
const totalSlides = slides.length;

// Function to get the current slide width dynamically
function getSlideWidth() {
    return document.querySelector(".hero-image-slider").offsetWidth; 
}

// Function to update the slider width dynamically
function updateSliderWidth() {
    const slideWidth = getSlideWidth();
    slider.style.width = `${totalSlides * slideWidth}px`;
    showSliderSlide(sliderIndex); // Adjust position when resized
}

// Function to show the correct slide
function showSliderSlide(index) {
    sliderIndex = (index + totalSlides) % totalSlides; // Loop back correctly
    slider.style.transform = `translateX(-${sliderIndex * getSlideWidth()}px)`;
}

// Add event listeners for buttons (Only if buttons exist)
document.querySelector(".next")?.addEventListener("click", () => showSliderSlide(sliderIndex + 1));
document.querySelector(".prev")?.addEventListener("click", () => showSliderSlide(sliderIndex - 1));

// Auto-slide every 5 seconds
let sliderInterval = setInterval(() => showSliderSlide(sliderIndex + 1), 5000);

// Pause slider when hovering over buttons to prevent accidental skips
document.querySelectorAll(".prev, .next").forEach(button => {
    button.addEventListener("mouseenter", () => clearInterval(sliderInterval));
    button.addEventListener("mouseleave", () => {
        sliderInterval = setInterval(() => showSliderSlide(sliderIndex + 1), 5000);
    });
});

// Update slider width on window resize
window.addEventListener("resize", updateSliderWidth);

// Initialize slider with correct width
updateSliderWidth();

