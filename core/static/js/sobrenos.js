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