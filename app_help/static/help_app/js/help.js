document.addEventListener("DOMContentLoaded", () => {
    let selectedDate = "";
    let selectedTime = "";
  
    function updateSessionButton() {
      const btn = document.getElementById("bookSessionBtn");
      if (selectedDate && selectedTime) {
        btn.textContent = `Book Your Session On: ${selectedDate} at ${selectedTime}`;
      } else if (selectedDate) {
        btn.textContent = `Book Your Session On: ${selectedDate}`;
      } else if (selectedTime) {
        btn.textContent = `Book Your Session On: [Date?] at ${selectedTime}`;
      } else {
        btn.textContent = `Book Your Session On:`;
      }
    }
  
    function setupSlider(sliderId, prevBtnId, nextBtnId, type) {
      const slider = document.getElementById(sliderId);
      const cards = slider.querySelectorAll(".date-card");
      const cardWidth = 110;
      const visibleCards = 3;
      const maxScroll = cards.length - visibleCards;
      let currentIndex = 0;
  
      document.getElementById(nextBtnId).addEventListener("click", () => {
        if (currentIndex < maxScroll) {
          currentIndex++;
          updateSlider();
        }
      });
  
      document.getElementById(prevBtnId).addEventListener("click", () => {
        if (currentIndex > 0) {
          currentIndex--;
          updateSlider();
        }
      });
  
      function updateSlider() {
        slider.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
      }
  
      cards.forEach(card => {
        card.addEventListener("click", () => {
          cards.forEach(c => c.classList.remove("active"));
          card.classList.add("active");
  
          // Get h3 text (date or time depending on type)
          const value = card.querySelector("h3").textContent;
          if (type === "date") {
            selectedDate = value;
          } else if (type === "time") {
            selectedTime = value;
          }
  
          updateSessionButton();
        });
      });
    }
  
    // Setup sliders
    setupSlider("dateSlider", "prevBtn", "nextBtn", "date");
    setupSlider("timeSlider", "prevTimeBtn", "nextTimeBtn", "time");
  });
  