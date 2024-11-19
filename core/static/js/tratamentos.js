document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle'); // Ícone do menu
    const menu = document.querySelector('ul'); // A lista de itens do menu
    const image = document.querySelector('.imagem'); // Selecione a imagem (ajuste a classe ou id conforme necessário)
    const retangulo = document.querySelector('.retangulo-um'); // Seletor para o retângulo

    // Quando o ícone de hambúrguer for clicado
    menuToggle.addEventListener('click', function() {
        menu.classList.toggle('active'); // Alterna a exibição do menu

        // Verifica se o menu está aberto ou fechado e ajusta a posição da imagem
        if (menu.classList.contains('active')) {
            // Ajusta a posição da imagem (ajuste conforme necessário)
            image.style.top = '266px'; 
        } else {
            // Reseta a posição da imagem
            image.style.top = '0'; 
        }

        // Ajuste do retângulo quando o menu está aberto ou fechado
        if (menu.classList.contains('active')) {
            retangulo.style.height = '82vh'; // Ajuste a altura conforme necessário
        } else {
            retangulo.style.height = '35vh'; // Valor padrão do retângulo
        }
    });
});

