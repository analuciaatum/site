// Selecionar os ícones e os campos de senha
const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');
const toggleConfirmPassword = document.querySelector('#toggleConfirmPassword');
const confirmPassword = document.querySelector('#confirmPassword');
const continueButton = document.querySelector('#continueButton'); // Selecionar o botão de continuar

// Alternar a visibilidade da senha ao clicar no ícone de olho
togglePassword.addEventListener('click', function () {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});

toggleConfirmPassword.addEventListener('click', function () {
    const type = confirmPassword.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmPassword.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});

// Verificar se as senhas coincidem e habilitar/desabilitar o botão de continuar
function validatePasswords() {
    if (password.value && confirmPassword.value) {
        if (password.value === confirmPassword.value) {
            continueButton.disabled = false; // Habilitar o botão de continuar
        } else {
            continueButton.disabled = true; // Desabilitar o botão de continuar
        }
    } else {
        continueButton.disabled = true; // Desabilitar se um dos campos estiver vazio
    }
}

// Adicionar eventos de input para verificar as senhas ao digitar
password.addEventListener('input', validatePasswords);
confirmPassword.addEventListener('input', validatePasswords);

// Função para formatar e validar o número de celular
const celularInput = document.getElementById('number');
celularInput.addEventListener('input', function(event) {
    let valor = this.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos

    if (valor.length > 2) {
        valor = valor.replace(/^(\d{2})(\d+)/, '($1) $2'); // Adiciona o formato (xx) 
    }
    if (valor.length > 8) {
        valor = valor.replace(/(\d{4})(\d+)/, '$1-$2'); // Adiciona o formato xxxx-xxxx
    }

    this.value = valor.slice(0, 14); // Limita o total de caracteres a 14
});

// Validação final no envio do formulário
const form = document.querySelector('form');
form.addEventListener('submit', function (e) {
    e.preventDefault(); // Impede o envio do formulário padrão

    // Validações
    if (password.value === '' || confirmPassword.value === '') {
        alert('Por favor, preencha todos os campos de senha.');
    } else if (password.value !== confirmPassword.value) {
        alert('As senhas não coincidem. Por favor, verifique.');
    } else if (celularInput.value.replace(/\D/g, '').length !== 10) { // Verifica se o celular tem 10 dígitos
        alert('O número de celular deve ter 10 dígitos.');
    } else {
        // Se todas as validações passarem, redireciona para a próxima página
        window.location.href = 'proxima_pagina.html'; // Altere para a URL da próxima página
    }
});