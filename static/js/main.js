/* B2B Sales Platform — Main JS */
document.addEventListener('DOMContentLoaded', () => {

  // Auto-dismiss alert messages after 6 seconds
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
      alert.style.opacity = '0';
      alert.style.transform = 'translateX(20px)';
      setTimeout(() => alert.remove(), 400);
    }, 6000);
  });

  // Form submit loading state
  const form = document.querySelector('.request-form');
  if (form) {
    form.addEventListener('submit', function () {
      const btn = this.querySelector('.submit-btn');
      if (btn) {
        btn.querySelector('.btn-text').textContent = 'Submitting...';
        btn.disabled = true;
        btn.style.opacity = '0.75';
      }
    });
  }

  // Fade-in product cards on scroll
  const cards = document.querySelectorAll('.product-card, .step');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.animationPlayState = 'running';
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    cards.forEach((card, i) => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      card.style.transition = `opacity 0.5s ease ${i * 0.06}s, transform 0.5s ease ${i * 0.06}s`;
      observer.observe(card);
    });

    // Trigger visible class
    document.addEventListener('scroll', () => {}, { passive: true });
  }

  // Add visible class for animated items already in view
  setTimeout(() => {
    cards.forEach(card => {
      const rect = card.getBoundingClientRect();
      if (rect.top < window.innerHeight) {
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
      }
    });
  }, 100);

});

// Intersection observer polyfill fallback
window.addEventListener('scroll', function () {
  document.querySelectorAll('.product-card, .step').forEach(card => {
    const rect = card.getBoundingClientRect();
    if (rect.top < window.innerHeight - 50) {
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    }
  });
}, { passive: true });
