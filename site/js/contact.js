/**
 * contact.js — Form validation, submission via Formspree
 * Code House — Contact form handling
 */

(function () {
  'use strict';

  var form = document.getElementById('contact-form');
  if (!form) return;

  var nomeInput = document.getElementById('nome');
  var necessidadeInput = document.getElementById('necessidade');
  var errorNome = document.getElementById('nome-error');
  var errorNecessidade = document.getElementById('necessidade-error');
  var submitBtn = document.getElementById('submit-btn');
  var successMsg = document.getElementById('success-msg');
  var successName = document.getElementById('success-name');

  function showError(el, msgEl, message) {
    msgEl.textContent = message;
    el.setAttribute('aria-invalid', 'true');
  }

  function clearError(el, msgEl) {
    msgEl.textContent = '';
    el.removeAttribute('aria-invalid');
  }

  // Real-time validation
  nomeInput.addEventListener('input', function () {
    if (nomeInput.value.trim()) clearError(nomeInput, errorNome);
  });
  necessidadeInput.addEventListener('input', function () {
    if (necessidadeInput.value.trim()) clearError(necessidadeInput, errorNecessidade);
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var nome = nomeInput.value.trim();
    var necessidade = necessidadeInput.value.trim();
    var valid = true;

    if (!nome) {
      showError(nomeInput, errorNome, 'Por favor, informe seu nome.');
      valid = false;
    } else {
      clearError(nomeInput, errorNome);
    }

    if (!necessidade) {
      showError(necessidadeInput, errorNecessidade, 'Por favor, descreva o que você precisa.');
      valid = false;
    } else {
      clearError(necessidadeInput, errorNecessidade);
    }

    if (!valid) return;

    submitBtn.textContent = 'Enviando...';
    submitBtn.disabled = true;

    var formData = new FormData(form);
    var data = Object.fromEntries(formData.entries());

    fetch('https://formspree.io/f/xaewbejg', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    })
      .then(function (response) {
        if (response.ok) {
          form.style.display = 'none';
          successMsg.style.display = 'block';
          successMsg.removeAttribute('aria-hidden');
          if (successName) successName.textContent = nome;
        } else {
          submitBtn.textContent = 'Erro. Tente novamente.';
          submitBtn.disabled = false;
        }
      })
      .catch(function () {
        submitBtn.textContent = 'Erro de conexão.';
        submitBtn.disabled = false;
      });
  });
})();