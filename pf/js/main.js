import { loadSkills } from './skills.js';
import { loadProjects } from './projects.js';

// Initialize GSAP ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Navbar scroll effect
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(15, 23, 42, 0.95)';
    } else {
        navbar.style.background = 'rgba(15, 23, 42, 0.9)';
    }
});

// Back to Top Button
const backToTopButton = document.getElementById('backToTop');
if (backToTopButton) {  // Check if button exists
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopButton.classList.add('visible');
        } else {
            backToTopButton.classList.remove('visible');
        }
    });

    backToTopButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Populate Skills
document.addEventListener('DOMContentLoaded', function() {
    // Contact form handling
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            console.log('Form submitted');
        });
    }

    // Back to Top Button
    const backToTopButton = document.getElementById('backToTop');
    if (backToTopButton) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });

        backToTopButton.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Skills Data
    const skillsData = {
        'Frontend Development': [
            { name: 'HTML5', level: 90 },
            { name: 'CSS3', level: 85 },
            { name: 'JavaScript', level: 80 },
            { name: 'React', level: 75 },
        ],
        'Backend Development': [
            { name: 'Python', level: 85 },
            { name: 'Django', level: 80 },
            { name: 'Node.js', level: 70 },
            { name: 'SQL', level: 75 },
        ],
        'Tools & Technologies': [
            { name: 'Git', level: 85 },
            { name: 'Docker', level: 70 },
            { name: 'AWS', level: 65 },
            { name: 'Linux', level: 75 },
        ]
    };

    // Populate Skills
    Object.entries(skillsData).forEach(([category, skills]) => {
        const categoryElements = document.querySelectorAll('.skill-category h3');
        const categoryElement = Array.from(categoryElements)
            .find(el => el.textContent.trim() === category)
            ?.parentElement;

        if (categoryElement) {
            const skillItems = categoryElement.querySelector('.skill-items');
            if (skillItems) {
                skills.forEach(skill => {
                    const skillElement = document.createElement('div');
                    skillElement.className = 'skill-item';
                    skillElement.innerHTML = `
                        <div class="skill-info">
                            <span>${skill.name}</span>
                            <span>${skill.level}%</span>
                        </div>
                        <div class="progress-bar">
                            <div class="progress" style="width: ${skill.level}%"></div>
                        </div>
                    `;
                    skillItems.appendChild(skillElement);
                });
            }
        }
    });

    // Create particle effect
    function createParticles() {
        const particlesContainer = document.querySelector('.particles');
        if (particlesContainer) {
            for (let i = 0; i < 50; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.top = Math.random() * 100 + '%';
                particle.style.animationDelay = Math.random() * 20 + 's';
                particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
                particlesContainer.appendChild(particle);
            }
        }
    }

    // Initialize particles
    createParticles();
});

// Project Slider Functionality
document.addEventListener('DOMContentLoaded', function() {
    const projectBubbles = document.querySelectorAll('.project-bubble');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    let currentIndex = 0;

    function showProject(index) {
        projectBubbles.forEach((bubble, i) => {
            if (i === index) {
                bubble.classList.remove('hidden');
                bubble.classList.add('active');
                // Add entrance animation
                gsap.fromTo(bubble, 
                    { opacity: 0, scale: 0.8 }, 
                    { opacity: 1, scale: 1, duration: 0.5, ease: "back.out" }
                );
            } else {
                bubble.classList.add('hidden');
                bubble.classList.remove('active');
            }
        });
        updateButtonStates();
    }

    // Next button click handler
    nextBtn.addEventListener('click', () => {
        if (currentIndex < projectBubbles.length - 1) {
            currentIndex++;
            showProject(currentIndex);
        }
    });

    // Previous button click handler
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            showProject(currentIndex);
        }
    });

    function updateButtonStates() {
        prevBtn.disabled = currentIndex === 0;
        nextBtn.disabled = currentIndex === projectBubbles.length - 1;
        
        // Update button opacity based on state
        prevBtn.style.opacity = currentIndex === 0 ? "0.5" : "1";
        nextBtn.style.opacity = currentIndex === projectBubbles.length - 1 ? "0.5" : "1";
    }

    // Initialize first project
    showProject(0);

    // Make sure links are clickable
    const githubLinks = document.querySelectorAll('.github-link');
    githubLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent the click from affecting the slider
            window.open(link.href, '_blank'); // Open link in new tab
        });
    });
});

// Enhanced GSAP Animations
gsap.registerPlugin(ScrollTrigger);

// Hero Section Animation
gsap.from('.hero-text', {
    duration: 1.5,
    y: 100,
    opacity: 0,
    ease: 'power4.out',
    stagger: 0.2
});

gsap.from('.hero-image', {
    duration: 1.5,
    x: 100,
    opacity: 0,
    ease: 'power4.out',
    delay: 0.5
});

// Scroll Animations for Projects
gsap.utils.toArray('.project-card').forEach((card, i) => {
    gsap.from(card, {
        scrollTrigger: {
            trigger: card,
            start: 'top bottom-=100',
            toggleActions: 'play none none reverse'
        },
        y: 100,
        opacity: 0,
        duration: 0.8,
        delay: i * 0.1
    });
});

// Skills Animation
gsap.utils.toArray('.skill-category').forEach((category, i) => {
    gsap.from(category, {
        scrollTrigger: {
            trigger: category,
            start: 'top bottom-=100',
            toggleActions: 'play none none reverse'
        },
        y: 50,
        opacity: 0,
        duration: 0.6,
        delay: i * 0.1
    });
});

// Progress bar animation
gsap.utils.toArray('.progress').forEach(progress => {
    const width = progress.style.width;
    progress.style.width = 0;
    
    ScrollTrigger.create({
        trigger: progress,
        start: 'top bottom-=100',
        onEnter: () => {
            gsap.to(progress, {
                width: width,
                duration: 1.5,
                ease: 'power2.out'
            });
        }
    });
});

// Smooth scroll implementation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            gsap.to(window, {
                duration: 1,
                scrollTo: {
                    y: target,
                    offsetY: 70
                },
                ease: 'power3.inOut'
            });
        }
    });
});

// GSAP Animations
// Hero Section Animation
gsap.from('.hero-text', {
    duration: 1,
    y: 100,
    opacity: 0,
    ease: 'power4.out'
});

// Scroll Animations
const sections = document.querySelectorAll('section');
sections.forEach(section => {
    gsap.from(section, {
        scrollTrigger: {
            trigger: section,
            start: 'top 80%',
            end: 'top 20%',
            toggleActions: 'play none none reverse'
        },
        y: 50,
        opacity: 0,
        duration: 1,
        ease: 'power3.out'
    });
});

// Remove or comment out any addProject related scroll handlers
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', e => {
        if (link.getAttribute('href') !== '#addProject') { // Add this condition
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        }
    });
});

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  loadSkills();
  loadProjects();
  // other initializations
});
