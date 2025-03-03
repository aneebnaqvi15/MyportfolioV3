// Counter Animation with Easing
const animateCounter = (element, target) => {
    const counter = element;
    const duration = 2000; // 2 seconds
    const startTime = performance.now();
    let currentCount = 0;

    const easeOutQuart = (x) => {
        return 1 - Math.pow(1 - x, 4);
    };

    const updateCounter = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        if (progress < 1) {
            currentCount = Math.floor(easeOutQuart(progress) * target);
            counter.textContent = currentCount;
            requestAnimationFrame(updateCounter);
        } else {
            counter.textContent = target;
            // Add final animation class
            counter.style.transform = 'scale(1.1)';
            setTimeout(() => {
                counter.style.transform = 'scale(1)';
            }, 200);
        }
    };

    requestAnimationFrame(updateCounter);
};

// Progress Bar Animation with Loading Effect
const animateProgressBar = (progressBar, targetPercentage) => {
    const progress = progressBar.querySelector('.progress');
    const duration = 1500; // 1.5 seconds
    const startTime = performance.now();
    
    const easeOutExpo = (x) => {
        return x === 1 ? 1 : 1 - Math.pow(2, -10 * x);
    };

    const updateProgress = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progressRatio = Math.min(elapsed / duration, 1);
        
        if (progressRatio < 1) {
            const easedProgress = easeOutExpo(progressRatio);
            const currentWidth = easedProgress * parseInt(targetPercentage);
            progress.style.width = `${currentWidth}%`;
            requestAnimationFrame(updateProgress);
        } else {
            progress.style.width = targetPercentage;
        }
    };

    // Add loading effect
    progress.style.width = '5%';
    setTimeout(() => {
        requestAnimationFrame(updateProgress);
    }, 200);
};

// Intersection Observer for counter animation
const observeCounters = () => {
    const counters = document.querySelectorAll('.counter-value');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.getAttribute('data-target'));
                entry.target.style.transform = 'translateY(20px)';
                entry.target.style.opacity = '0';
                
                setTimeout(() => {
                    entry.target.style.transition = 'transform 0.5s ease, opacity 0.5s ease';
                    entry.target.style.transform = 'translateY(0)';
                    entry.target.style.opacity = '1';
                    animateCounter(entry.target, target);
                }, 200);
                
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => observer.observe(counter));
};

// Progress bar observer
const observeProgressBars = () => {
    const progressBars = document.querySelectorAll('.progress-bar');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const targetPercentage = entry.target.parentElement.querySelector('.percentage').textContent;
                animateProgressBar(entry.target, targetPercentage);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    progressBars.forEach(bar => observer.observe(bar));
};

// Initialize animations when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    observeCounters();
    observeProgressBars();
});
