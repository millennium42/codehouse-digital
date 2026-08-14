/**
 * main.js — Theme toggle, initialization, WhatsApp links, current year
 * Code House — Main application entry point
 */

(function () {
  'use strict';

  /* ─────────────────────────────────────────────
     THEME TOGGLE
     ───────────────────────────────────────────── */
  const themeToggle = document.getElementById('theme-toggle');

  function getPreferredTheme() {
    const stored = localStorage.getItem('ch-theme');
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('ch-theme', theme);
  }

  // Apply theme immediately to prevent flash
  applyTheme(getPreferredTheme());

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const next = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
    });
  }

  /* ─────────────────────────────────────────────
     CURRENT YEAR IN FOOTER
     ───────────────────────────────────────────── */
  const yearEl = document.getElementById('current-year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  /* ─────────────────────────────────────────────
     WHATSAPP LINKS
     ───────────────────────────────────────────── */
  const WHATSAPP_NUMBER = '55559991441700';
  document.querySelectorAll('[data-whatsapp="true"]').forEach(function (link) {
    link.href = 'https://wa.me/' + WHATSAPP_NUMBER;
    link.setAttribute('target', '_blank');
    link.setAttribute('rel', 'noopener noreferrer');
  });

  /* ─────────────────────────────────────────────
     FAQ ACCORDION
     ───────────────────────────────────────────── */
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var btn = item.querySelector('.faq-q');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(function (openItem) {
        openItem.classList.remove('open');
        var a = openItem.querySelector('.faq-a');
        if (a) a.classList.add('hidden');
      });
      if (!isOpen) {
        item.classList.add('open');
        var answer = item.querySelector('.faq-a');
        if (answer) answer.classList.remove('hidden');
      }
    });
  });

})();