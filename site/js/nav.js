/* nav.js */
(function(){
  var ham = document.getElementById('hamburger');
  var menu = document.getElementById('navMenu');
  if(!ham || !menu) return;
  ham.addEventListener('click', function(){
    ham.classList.toggle('active');
    menu.classList.toggle('open');
  });
  menu.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', function(){
      ham.classList.remove('active');
      menu.classList.remove('open');
    });
  });
  document.addEventListener('click', function(e){
    if(!menu.contains(e.target) && !ham.contains(e.target)){
      ham.classList.remove('active');
      menu.classList.remove('open');
    }
  });
  document.addEventListener('keydown', function(e){
    if(e.key === 'Escape'){
      ham.classList.remove('active');
      menu.classList.remove('open');
    }
  });
})();
