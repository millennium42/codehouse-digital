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
     ───────────────────────────────────────────── */
  var counters = document.querySelectorAll('[data-counter]');
  if (counters.length && 'IntersectionObserver' in window) {
    function animateCounter(el, target, duration) {
      var start = 0;
      var startTime = null;
      var isFloat = target % 1 !== 0;

      function step(timestamp) {
        if (!startTime) startTime = timestamp;
        var progress = Math.min((timestamp - startTime) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
        var current = start + (target - start) * eased;
        el.textContent = isFloat ? current.toFixed(1) : Math.floor(current);
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = target;
        }
      }
      requestAnimationFrame(step);
    }

    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var target = parseFloat(entry.target.dataset.counter);
          animateCounter(entry.target, target, 1500);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(function (c) { counterObserver.observe(c); });
  }

  /* ─────────────────────────────────────────────
     PARALLAX HERO
     ───────────────────────────────────────────── */
  var heroMockup = document.querySelector('.hero-mockup');
  if (heroMockup) {
    document.addEventListener('mousemove', function (e) {
      var x = (window.innerWidth / 2 - e.clientX) / 50;
      var y = (window.innerHeight / 2 - e.clientY) / 50;
      heroMockup.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
    });
  }

})();