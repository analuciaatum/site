document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.querySelector('.ul'); // Seletor atualizado
    const retangulo = document.querySelector('.retangulo-um'); // Seletor para o retângulo
    
    menuToggle.addEventListener('click', function() {
        menu.classList.toggle('active'); // Alterna a exibição do menu

        // Ajusta a altura do retângulo conforme o menu está aberto ou fechado
        if (menu.classList.contains('active')) {
            retangulo.style.height = '82vh'; // Ajuste conforme necessário
        } else {
            retangulo.style.height = '35vh'; // Valor padrão ou ajuste conforme necessário
        }
    });
});

const carrossel = document.querySelector(".carrossel"),
    firstImg = carrossel.querySelectorAll("img")[0],
    arrowIcons = document.querySelectorAll(".wrapper i");

let isDragStart = false, prevPageX, prevScrollLeft;

const showHideIcons = () => {
    let scrollWidth = carrossel.scrollWidth - carrossel.clientWidth;
    arrowIcons[0].style.display = carrossel.scrollLeft === 0 ? "none" : "block";
    arrowIcons[1].style.display = carrossel.scrollLeft >= scrollWidth ? "none" : "block";
}

arrowIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        let firstImgWidth = firstImg.clientWidth + 14;
        carrossel.scrollLeft += icon.classList.contains("fa-angle-left") ? -firstImgWidth : firstImgWidth;
        setTimeout(showHideIcons, 60);
    });
}) 

const dragStart = (e) => {
    isDragStart = true;
    prevPageX = e.pageX || e.touches[0].pageX; // Corrigido para funcionar com toque e clique
    prevScrollLeft = carrossel.scrollLeft;
}

const dragging = (e) => {
    if (!isDragStart) return;
    e.preventDefault();
    carrossel.classList.add("dragging");
    let positionDiff = (e.pageX || e.touches[0].pageX) - prevPageX; // Corrigido para toque e clique
    carrossel.scrollLeft = prevScrollLeft - positionDiff;
    showHideIcons();
}

const dragStop = () => {
    isDragStart = false;
    carrossel.classList.remove("dragging");
}

carrossel.addEventListener("mousedown", dragStart);
carrossel.addEventListener("touchstart", dragStart);

carrossel.addEventListener("mousemove", dragging);
carrossel.addEventListener("touchmove", dragging);

carrossel.addEventListener("mouseup", dragStop);
carrossel.addEventListener("mouseleave", dragStop);
carrossel.addEventListener("touchend", dragStop);