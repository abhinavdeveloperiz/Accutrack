
function checkFadeUp() {
    const elements = document.querySelectorAll('.fade-up');
    elements.forEach(function (element) {
        const rect = element.getBoundingClientRect();
        if (rect.top <= window.innerHeight + 50 && rect.bottom >= -50) {
            element.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', checkFadeUp, { passive: true });
window.addEventListener('resize', checkFadeUp, { passive: true });
document.addEventListener('DOMContentLoaded', checkFadeUp);
setTimeout(checkFadeUp, 100);
setTimeout(checkFadeUp, 500);

