/**
 * animations.js — Scroll reveal, counters, parallax effects
 * Code House — Interactive animations & transitions
 */

(function () {
  'use strict';

  /* ─────────────────────────────────────────────
     FADE IN (HERO MOCKUP)
     ───────────────────────────────────────────── */
  var fadeEls = document.querySelectorAll('.fade');
  if (fadeEls.length && 'IntersectionObserver' in window) {
    var fadeObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
        }
      });
    }, { threshold: 0.1 });
    fadeEls.forEach(function (el) { fadeObserver.observe(el); });
  } else if (fadeEls.length) {
    fadeEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* ─────────────────────────────────────────────
     SCROLL REVEAL (.reveal elements)
     ───────────────────────────────────────────── */
  var revealEls = document.querySelectorAll('.reveal');
  if (revealEls.length && 'IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });
    revealEls.forEach(function (el) { revealObserver.observe(el); });
  } else if (revealEls.length) {
    revealEls.forEach(function (el) { el.classList.add('revealed'); });
  }

  /* ─────────────────────────────────────────────
     ANIMATED COUNTERS (credibility section)
     Uses data-counter="XX" and optional data-suffix=""
     ───────────────────────────────────────────── */
  var counters = document.querySelectorAll('[data-counter]');
  if (counters.length) {
    function animateCounter(el, target, suffix, duration) {
      var start = 0;
      var startTime = null;
      var isFloat = target % 1 !== 0;

      function step(timestamp) {
        if (!startTime) startTime = timestamp;
        var progress = Math.min((timestamp - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
        var current = start + (target - start) * eased;
        var display = isFloat ? current.toFixed(1) : Math.floor(current);
        el.textContent = display + (suffix || '');
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = target + (suffix || '');
        }
      }
      requestAnimationFrame(step);
    }

    if ('IntersectionObserver' in window) {
      var counterObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var target = parseFloat(entry.target.dataset.counter);
            var suffix = entry.target.dataset.suffix || '';
            animateCounter(entry.target, target, suffix, 1500);
            counterObserver.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });

      counters.forEach(function (c) { counterObserver.observe(c); });
    } else {
      counters.forEach(function (c) {
        animateCounter(c, parseFloat(c.dataset.counter), c.dataset.suffix || '', 1500);
      });
    }
  }

  /* ─────────────────────────────────────────────
     PARALLAX HERO
     ───────────────────────────────────────────── */
  var heroMockup = document.querySelector('.hero-mockup');
  if (heroMockup && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    document.addEventListener('mousemove', function (e) {
      var x = (window.innerWidth / 2 - e.clientX) / 50;
      var y = (window.innerHeight / 2 - e.clientY) / 50;
      heroMockup.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
    });
  }

})();