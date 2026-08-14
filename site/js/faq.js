/* faq.js — Accordion acessível */
(function() {
  'use strict';

  document.querySelectorAll('.faq-q').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      var targetId = btn.getAttribute('aria-controls');
      var target = document.getElementById(targetId);

      // Fecha todos os outros itens (modo acordeão)
      document.querySelectorAll('.faq-q').forEach(function(otherBtn) {
        if (otherBtn !== btn) {
          otherBtn.setAttribute('aria-expanded', 'false');
          var otherId = otherBtn.getAttribute('aria-controls');
          var otherTarget = document.getElementById(otherId);
          if (otherTarget) otherTarget.hidden = true;
        }
      });

      // Toggle atual
      btn.setAttribute('aria-expanded', String(!expanded));
      if (target) target.hidden = expanded;
    });

    // Keyboard: Enter e Space já são nativos de <button>, mas garantir
    btn.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        btn.click();
      }
    });
  });
})();
