/* animations.js — Scroll reveal, counters, parallax, tabs, FAQ */

(function () {
  'use strict';

  /* ═══════════════════════════════════════════
     SCROLL REVEAL
     ═══════════════════════════════════════════ */
  var revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length && 'IntersectionObserver' in window) {
    revealEls.forEach(function (el) { el.classList.add('will-animate'); });

    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(function (el) { revealObserver.observe(el); });

    setTimeout(function () {
      revealEls.forEach(function (el) {
        var rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
          el.classList.add('revealed');
        }
      });
    }, 150);
  } else if (revealEls.length) {
    revealEls.forEach(function (el) { el.classList.add('revealed'); });
  }

  /* ═══════════════════════════════════════════
     PARALLAX HERO
     ═══════════════════════════════════════════ */
  var heroMockup = document.querySelector('.hero-mockup');
  if (heroMockup && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    var heroRaf = null;
    document.addEventListener('mousemove', function (e) {
      if (heroRaf) return;
      heroRaf = requestAnimationFrame(function () {
        var x = (window.innerWidth / 2 - e.clientX) / 60;
        var y = (window.innerHeight / 2 - e.clientY) / 60;
        heroMockup.style.transform = 'perspective(1000px) rotateY(' + x + 'deg) rotateX(' + (-y) + 'deg)';
        heroRaf = null;
      });
    });
  }

  /* ═══════════════════════════════════════════
     TABS (EXAMPLES)
     ═══════════════════════════════════════════ */
  var tabBtns = document.querySelectorAll('.tab-btn');
  var tabPanels = document.querySelectorAll('.tab-panel');
  if (tabBtns.length && tabPanels.length) {
    tabBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var target = btn.getAttribute('data-tab');

        tabBtns.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');

        tabPanels.forEach(function (panel) {
          if (panel.getAttribute('id') === 'tab-' + target) {
            panel.classList.add('active');
          } else {
            panel.classList.remove('active');
          }
        });
      });
    });
  }

  /* ═══════════════════════════════════════════
     FAQ ACCORDION
     ═══════════════════════════════════════════ */
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var btn = item.querySelector('.faq-q');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');

      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        openItem.classList.remove('open');
      });

      if (!isOpen) {
        item.classList.add('open');
      }
    });
  });

  /* ═══════════════════════════════════════════
     SMOOTH SCROLL FOR ANCHOR LINKS
     ═══════════════════════════════════════════ */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(link.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();
