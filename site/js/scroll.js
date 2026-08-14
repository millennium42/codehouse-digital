/* scroll.js */
(function(){
  'use strict';
  var els = document.querySelectorAll('.reveal');
  if(!els.length) return;
  
  els.forEach(function(el){ el.classList.add('will-animate'); });
  
  if('IntersectionObserver' in window){
    var obs = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(e.isIntersecting){
          e.target.classList.add('revealed');
          obs.unobserve(e.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });
    
    els.forEach(function(el){ obs.observe(el); });
    
    setTimeout(function(){
      els.forEach(function(el){
        var r = el.getBoundingClientRect();
        if(r.top < window.innerHeight && r.bottom > 0){
          el.classList.add('revealed');
        }
      });
    }, 150);
  } else {
    els.forEach(function(el){ el.classList.add('revealed'); });
  }
  
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click', function(e){
      var id = a.getAttribute('href');
      if(id && id.length > 1){
        var t = document.querySelector(id);
        if(t){ e.preventDefault(); t.scrollIntoView({behavior:'smooth', block:'start'}); }
      }
    });
  });
})();
