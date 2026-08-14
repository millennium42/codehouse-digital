/* theme.js */
(function(){
  var btn = document.getElementById('themeBtn');
  var saved = localStorage.getItem('ch-theme');
  var prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
  var theme = saved || (prefersLight ? 'light' : 'dark');
  document.documentElement.setAttribute('data-theme', theme);
  if(btn) btn.addEventListener('click', function(){
    var cur = document.documentElement.getAttribute('data-theme');
    var next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('ch-theme', next);
  });
})();
