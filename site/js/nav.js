/* nav.js */
(function(){
  'use strict';
  const ham = document.getElementById('hamburger');
  const menu = document.getElementById('navMenu');
  if(!ham || !menu) return;
  
  const focusableElements = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
  let firstFocusableElement;
  let lastFocusableElement;

  function updateFocusables() {
    const focusableContent = menu.querySelectorAll(focusableElements);
    if(focusableContent.length === 0) return;
    firstFocusableElement = focusableContent[0];
    lastFocusableElement = focusableContent[focusableContent.length - 1];
  }

  function closeMenu() {
    ham.classList.remove('active');
    menu.classList.remove('open');
    ham.setAttribute('aria-expanded', 'false');
    ham.focus();
  }

  function openMenu() {
    ham.classList.add('active');
    menu.classList.add('open');
    ham.setAttribute('aria-expanded', 'true');
    updateFocusables();
    if(firstFocusableElement) firstFocusableElement.focus();
  }
  
  ham.addEventListener('click', function(){
    if (menu.classList.contains('open')) {
      closeMenu();
    } else {
      openMenu();
    }
  });
  
  menu.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', closeMenu);
  });
  
  document.addEventListener('click', function(e){
    if(menu.classList.contains('open') && !menu.contains(e.target) && !ham.contains(e.target)){
      closeMenu();
    }
  });
  
  document.addEventListener('keydown', function(e){
    if(!menu.classList.contains('open')) return;

    if(e.key === 'Escape'){
      closeMenu();
      return;
    }

    if (e.key === 'Tab') {
      updateFocusables();
      if (!firstFocusableElement) return;

      if (e.shiftKey) { // Se Shift + Tab
        if (document.activeElement === firstFocusableElement) {
          lastFocusableElement.focus();
          e.preventDefault();
        }
      } else { // Se apenas Tab
        if (document.activeElement === lastFocusableElement) {
          firstFocusableElement.focus();
          e.preventDefault();
        }
      }
    }
  });
})();
