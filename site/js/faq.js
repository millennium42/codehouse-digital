/* faq.js — Accordion acessível */
(function() {
  'use strict';

  document.querySelectorAll('.faq-q').forEach(function(btn) {
    btn.addEventListener('click', function() {
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      const targetId = btn.getAttribute('aria-controls');
      const target = document.getElementById(targetId);

      // Fecha todos os outros itens (modo acordeão)
      document.querySelectorAll('.faq-q').forEach(function(otherBtn) {
        if (otherBtn !== btn) {
          otherBtn.setAttribute('aria-expanded', 'false');
          const otherId = otherBtn.getAttribute('aria-controls');
          const otherTarget = document.getElementById(otherId);
          if (otherTarget) {
            otherTarget.classList.remove('open');
            otherTarget.setAttribute('aria-hidden', 'true');
          }
        }
      });

      // Toggle atual
      btn.setAttribute('aria-expanded', String(!expanded));
      if (target) {
        if (expanded) {
          target.classList.remove('open');
          target.setAttribute('aria-hidden', 'true');
        } else {
          target.classList.add('open');
          target.setAttribute('aria-hidden', 'false');
        }
      }
    });

    // Keyboard
    btn.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        btn.click();
      }
    });
  });
})();
