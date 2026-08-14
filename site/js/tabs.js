/**
 * tabs.js — Interactive tabs for #exemplos section
 * Code House — Tab switching between CRM, ERP, E-shop, Site mockups
 */

(function () {
  'use strict';

  var tabsNav = document.querySelector('.tabs-nav');
  if (!tabsNav) return;

  var tabs = tabsNav.querySelectorAll('.tab-btn');
  var panels = document.querySelectorAll('.tab-panel');

  function activateTab(index) {
    tabs.forEach(function (tab, i) {
      if (i === index) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
    });
    panels.forEach(function (panel, i) {
      if (i === index) {
        panel.classList.add('active');
      } else {
        panel.classList.remove('active');
      }
    });
  }

  tabs.forEach(function (tab, index) {
    tab.addEventListener('click', function () {
      activateTab(index);
    });
  });

  // Initialize first tab
  activateTab(0);
})();