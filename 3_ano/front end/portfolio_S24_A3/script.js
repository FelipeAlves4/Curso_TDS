// script.js para Portfólio de Fotografia
// Alternar cor de fundo ao clicar nas imagens + Modal de visualização

document.querySelectorAll('.image').forEach(image => {
    image.addEventListener('click', () => {
        // Alterna cor de fundo
        image.style.backgroundColor =
            image.style.backgroundColor === 'rgb(255, 99, 71)'
                ? '#ddd'
                : 'rgb(255, 99, 71)';

        // Modal: abre imagem ampliada
        const modal = document.createElement('div');
        modal.style.position = 'fixed';
        modal.style.top = 0;
        modal.style.left = 0;
        modal.style.width = '100vw';
        modal.style.height = '100vh';
        modal.style.backgroundColor = 'rgba(0,0,0,0.8)';
        modal.style.display = 'flex';
        modal.style.justifyContent = 'center';
        modal.style.alignItems = 'center';
        modal.style.zIndex = 1000;
        modal.style.cursor = 'pointer';

        const img = document.createElement('div');
        img.style.width = '70vw';
        img.style.height = '70vh';
        img.style.backgroundImage = getComputedStyle(image).backgroundImage;
        img.style.backgroundSize = 'contain';
        img.style.backgroundRepeat = 'no-repeat';
        img.style.backgroundPosition = 'center';
        img.style.borderRadius = '18px';
        img.style.boxShadow = '0 5px 32px 0 rgba(0,0,0,0.4)';

        // Título da foto
        const caption = document.createElement('span');
        caption.textContent = image.getAttribute('data-title');
        caption.style.display = 'block';
        caption.style.color = 'white';
        caption.style.marginTop = '18px';
        caption.style.fontSize = '1.5em';
        caption.style.textAlign = 'center';
        caption.style.textShadow = '0 1px 4px #222';

        const content = document.createElement('div');
        content.appendChild(img);
        content.appendChild(caption);
        content.style.textAlign = 'center';

        modal.appendChild(content);
        modal.addEventListener('click', () => modal.remove());
        document.body.appendChild(modal);
    });
});

// Rolagem suave ao clicar em links do menu
const navLinks = document.querySelectorAll('nav ul li a');
navLinks.forEach(link => {
    link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href.startsWith("#")) {
            e.preventDefault();
            const section = document.querySelector(href);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    });
});

// "Voltar ao topo"
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', function () {
    if (window.scrollY > 350) {
        backToTop.style.display = 'block';
    } else {
        backToTop.style.display = 'none';
    }
});
backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// Validação simples do formulário de contato (exemplo)
document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
    document.getElementById('formMessage').textContent = "Mensagem enviada com sucesso! Em breve entrarei em contato.";
    this.reset();
});