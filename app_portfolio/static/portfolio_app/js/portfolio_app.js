// Typing effect for displaying skills like "Python Developer", "Web Developer", etc.
document.addEventListener("DOMContentLoaded", () => {
    const skillText = document.getElementById("skill-text");
    const skills = ["Python Developer", "Web Developer", "Full Stack Developer", "AI-ML Enthusiast"]; 
    let currentSkill = 0;
    let charIndex = 0;
    let typingSpeed = 100;
    let erasingSpeed = 50;
    let delayBetweenSkills = 1500;

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
            currentSkill = (currentSkill + 1) % skills.length;
            setTimeout(typeSkill, typingSpeed);
        }
    }

    // Start the typing effect on page load
    setTimeout(typeSkill, delayBetweenSkills);
});


// Handles opening and displaying modal content for certificate and resource buttons
document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("popup-modal");
    const previewContainer = modal.querySelector(".preview-container");
    const closeButton = modal.querySelector(".close-btn");

    function openModal(content) {
        previewContainer.innerHTML = content;
        modal.style.display = "block";
    }

    // Handle "View Certificate" button click to preview/download certificate
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

    // Handle "View Resources" button click to preview multiple resource types
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

    // Close the modal on close button click
    closeButton.addEventListener("click", function () {
        modal.style.display = "none";
    });
});


// Prevents background scrolling when using the modal's scroll area
document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("popup-modal");

    modal.addEventListener("wheel", function (event) {
        event.stopPropagation();
    });
});


// Toggles FAQ answers on card click and switches icons between open/close states
document.addEventListener("DOMContentLoaded", function () {
    const faqs = document.querySelectorAll(".faq-card");

    faqs.forEach((faq) => {
        faq.addEventListener("click", function () {
            const answer = faq.querySelector(".faq-answer");
            const icon = faq.querySelector(".faq-icon");

            const openIcon = faq.getAttribute("data-open-icon");
            const closeIcon = faq.getAttribute("data-close-icon");

            if (faq.classList.contains("active")) {
                faq.classList.remove("active");
                answer.style.display = "none";
                icon.src = openIcon;
            } else {
                faq.classList.add("active");
                answer.style.display = "block";
                icon.src = closeIcon;
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    let sliderIndex = 0;
    const slides = document.querySelectorAll(".slide");
    const slider = document.querySelector(".slider");
    const totalSlides = slides.length;

    function getSlideWidth() {
        return document.querySelector(".hero-image-slider").offsetWidth;
    }

    function updateSliderWidth() {
        const slideWidth = getSlideWidth();
        slider.style.width = `${totalSlides * slideWidth}px`;

        // Update each slide width to match container
        slides.forEach(slide => {
            slide.style.width = `${slideWidth}px`;
        });

        showSliderSlide(sliderIndex);
    }

    function showSliderSlide(index) {
        sliderIndex = (index + totalSlides) % totalSlides;
        slider.style.transform = `translateX(-${sliderIndex * getSlideWidth()}px)`;
    }

    document.querySelector(".next")?.addEventListener("click", () => showSliderSlide(sliderIndex + 1));
    document.querySelector(".prev")?.addEventListener("click", () => showSliderSlide(sliderIndex - 1));

    let sliderInterval = setInterval(() => showSliderSlide(sliderIndex + 1), 5000);

    document.querySelectorAll(".prev, .next").forEach(button => {
        button.addEventListener("mouseenter", () => clearInterval(sliderInterval));
        button.addEventListener("mouseleave", () => {
            sliderInterval = setInterval(() => showSliderSlide(sliderIndex + 1), 5000);
        });
    });

    window.addEventListener("resize", updateSliderWidth);

    updateSliderWidth();
});



// Fills progress bars in skill cards based on data-progress attribute
document.addEventListener("DOMContentLoaded", function () {
    const progressContainers = document.querySelectorAll('.progress-container');

    progressContainers.forEach(container => {
        const progressValue = container.getAttribute('data-progress');
        const progressBar = container.querySelector('.progress');
        progressBar.style.width = progressValue + '%';
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const openBtn = document.getElementById("open-btn");
    const closeBtn = document.getElementById("close-btn");
    const navItems = document.querySelector(".nav-items");
  
    openBtn.addEventListener("click", () => {
      navItems.classList.add("active");
    });
  
    closeBtn.addEventListener("click", () => {
      navItems.classList.remove("active");
    });
  });
