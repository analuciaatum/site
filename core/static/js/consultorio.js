




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

//Fim do efeito de visualização aumentada



document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.querySelector('.ul'); // Corrigi a seleção para a classe correta
    
    menuToggle.addEventListener('click', function() {
        menu.classList.toggle('active'); // Alterna a exibição do menu
    });
  });