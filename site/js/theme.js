/* theme.js */
(function(){
  'use strict';
  var btn = document.getElementById('themeBtn');
  
  // Apenas dark mode (sem light)
  function applyTheme() {
    document.documentElement.setAttribute('data-theme', 'dark');
  }
  
  applyTheme();
  
  // Toggle (para futuro light mode ou remover)
  if(btn) {
    btn.addEventListener('click', function() {
      // Feedback visual apenas
      btn.style.transform = 'scale(0.95)';
      setTimeout(function(){ btn.style.transform = ''; }, 150);
    });
  }
})();
