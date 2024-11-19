//cabeçalho

document.addEventListener('DOMContentLoaded', function() {
      const menuToggle = document.getElementById('menu-toggle');
      const menu = document.querySelector('ul');
      
      menuToggle.addEventListener('click', function() {
          menu.classList.toggle('active'); // Alterna a exibição do menu
          
          // Verifica a classe ativa do menu para ajustar a posição da imagem
          if (menu.classList.contains('active')) {
              image.style.top = '266px'; 
          } else {
              image.style.top = '0'; 
          }
      });
  });
  
  //Fim do Cabeçalho
  
  
  //Efeito de visualização aumentada
  
  function openModal(element) {
      const modal = document.getElementById("imageModal");
      const modalImg = document.getElementById("modalImage");
      const captionText = document.getElementById("caption");
      
      modal.style.display = "block";
      modalImg.src = element.querySelector("img").src; 
      captionText.innerHTML = element.querySelector("img").alt; 
  }
  
  function closeModal() {
      document.getElementById("imageModal").style.display = "none";
  }

  // Adição da lógica para o menu hambúrguer
  const menuToggleHamburguer = document.getElementById('menu-toggle');
  const menuHamburguer = document.querySelector('.ul'); // A classe que contém os itens do menu

  // Quando o botão hamburguer é clicado
  menuToggleHamburguer.addEventListener('click', function() {
      menuHamburguer.classList.toggle('active'); // Alterna a visibilidade do menu

      // Se o menu está aberto, ajustar a altura do retângulo (se necessário)
      if (menuHamburguer.classList.contains('active')) {
          retangulo.style.height = '82vh'; // Ajuste para a altura desejada
      } else {
          retangulo.style.height = '35vh'; // Valor padrão ou ajustado conforme a necessidade
      }
  });
  
  //Fim do efeito de visualização aumentada