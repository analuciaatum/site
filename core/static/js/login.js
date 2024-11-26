document.addEventListener('DOMContentLoaded', function() {
      const menuToggle = document.getElementById('menu-toggle');
      const menu = document.querySelector('.ul');
      const loginPanel = document.getElementById('loginPanel');
      
      menuToggle.addEventListener('click', function() {
          menu.classList.toggle('active'); // Alterna a exibição do menu
          
          // Alterna a visibilidade do painel de login
          if (menu.classList.contains('active')) {
              loginPanel.classList.add('visible');
          } else {
              loginPanel.classList.remove('visible');
          }
      });
  });
  
  function logar() {
    var login = document.getElementById('email').value.trim();
    var senha = document.getElementById('senha').value.trim();

    // Verifica se ambos os campos estão preenchidos
    if (!login || !senha) {
        alert('Por favor, preencha todos os campos.');
        return; // Interrompe a execução da função, impedindo o redirecionamento
    }

    // Verifica se as credenciais são válidas
    if (login === '' && senha === '') {
        location.href = 'home_logado.html';  // Redireciona apenas se as credenciais forem válidas
    } else {
        alert('Login ou senha incorretos. Tente novamente.'); // Alerta se as credenciais estiverem incorretas
    }
}

