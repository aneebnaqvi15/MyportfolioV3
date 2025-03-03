document.addEventListener('DOMContentLoaded', () => {
    const modelList = document.querySelector('.model-list');
    if (modelList) {  // Add null check
        const circles = document.querySelectorAll('.mask.full');
        
        circles.forEach(circle => {
            const percent = circle.getAttribute('data-percent');
            const rotation = (percent / 100) * 360;
            
            circle.style.transform = `rotate(${rotation}deg)`;
            circle.nextElementSibling.style.transform = `rotate(${rotation}deg)`;
            
            // Add dots
            const dots = [];
            for(let i = 0; i < 12; i++) {
                const dot = document.createElement('div');
                dot.className = 'dot';
                dot.style.transform = `rotate(${i * 30}deg)`;
                circle.closest('.circle').querySelector('.rotating-dots').appendChild(dot);
            }
        });

        // Animate on scroll
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.closest('.circle-wrap').classList.add('animate');
                }
            });
        }, { threshold: 0.5 });

        circles.forEach(circle => {
            observer.observe(circle);
        });
    }
});
