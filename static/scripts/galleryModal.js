document.querySelectorAll('.gallery-img').forEach(img => {
    img.addEventListener('click', function () {
      const modalImage = document.getElementById('modalImage');
      const modalCaption = document.getElementById('modalCaption');
      modalImage.src = this.src;
      modalCaption.textContent = this.dataset.bsCaption;
    });
  });


   // Increment animation script
   function animateNumbers() {
    const numbers = document.querySelectorAll('.number');
    numbers.forEach((num) => {
      const target = +num.getAttribute('data-target');
      let count = 0;
      const increment = Math.ceil(target / 50); // Controls the speed of animation
      const updateNumber = () => {
        if (count < target) {
          count += increment;
          num.textContent = count > target ? target : count;
          setTimeout(updateNumber, 20); // Animation speed
        } else {
          num.textContent = target;
        }
      };
      updateNumber();
    });
  }

  // Detecting when the numbers come into view
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          animateNumbers();
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  // Applying observer to all numbers
  document.querySelectorAll('.number').forEach((num) => {
    observer.observe(num);
  });