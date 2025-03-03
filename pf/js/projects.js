const API_URL = `${BASE_URL}/api/firebase/`;

document.addEventListener('DOMContentLoaded', () => {
    console.log('Page loaded, initializing...');
    const addProjectForm = document.getElementById('addProjectForm');
    if (addProjectForm) {
        addProjectForm.addEventListener('submit', handleProjectSubmission);
    }
    loadProjects();
});

async function loadProjects() {
    try {
        console.log('Fetching projects...');
        const response = await fetch('http://127.0.0.1:8000/api/firebase/', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            }
        });
        
        console.log('Response status:', response.status);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        console.log('Projects data:', result); // Debug log
        
        const projects = Array.isArray(result) ? result : (result.data || []);
        console.log('Processed projects:', projects); // Debug log

        const projectsContainer = document.getElementById('projectsContainer');
        if (!projectsContainer) {
            throw new Error('Projects container not found');
        }

        projectsContainer.innerHTML = '';
        
        if (projects.length === 0) {
            projectsContainer.innerHTML = '<p class="no-projects">No projects available.</p>';
            return;
        }

        // Create and append all project elements
        projects.forEach((project, index) => {
            const projectElement = createProjectElement(project, index);
            projectsContainer.appendChild(projectElement);
        });

        // Show first group of projects
        const projectElements = document.querySelectorAll('.project-bubble');
        projectElements.forEach((project, index) => {
            if (index < 3) {
                project.classList.remove('hidden');
                project.classList.add('active');
            } else {
                project.classList.add('hidden');
                project.classList.remove('active');
            }
        });

        // Setup navigation
        setupProjectNavigation();
        
        // Initialize indicators
        const totalGroups = Math.ceil(projects.length / 3);
        updateNavigationIndicators(0, totalGroups);

    } catch (error) {
        console.error('Error loading projects:', error);
        const projectsContainer = document.getElementById('projectsContainer');
        if (projectsContainer) {
            projectsContainer.innerHTML = `
                <p class="error-message">Failed to load projects: ${error.message}</p>
            `;
        }
    }
}

function createProjectElement(project, index) {
    const div = document.createElement('div');
    div.className = `project-bubble ${index < 3 ? 'active' : 'hidden'}`;
    div.setAttribute('data-project', Math.floor(index / 3) + 1);
    
    // Handle both image_url and image_file paths
    let imageUrl = project.image_url || project.image_file || project.image;
    
    // Check if the image is from media folder
    if (imageUrl && imageUrl.startsWith('/media/')) {
        imageUrl = `http://127.0.0.1:8000${imageUrl}`;
    }
    // Check if the image is from local images folder
    else if (imageUrl && imageUrl.startsWith('./images/')) {
        imageUrl = imageUrl.replace('./', '../');
    }
    
    console.log('Project image URL:', imageUrl); // Debug log
    
    const defaultImage = '../images/default-project.jpg';
    
    div.innerHTML = `
        <div class="project-content">
            <div class="project-image">
                <img src="${imageUrl || defaultImage}" 
                     alt="${project.title}" 
                     onerror="this.src='${defaultImage}'; console.log('Image failed to load:', imageUrl);">
                <div class="project-overlay">
                    <a href="${project.github}" class="github-link" target="_blank">
                        <i class="fas fa-code"></i>
                        View Code
                    </a>
                </div>
            </div>
            <div class="project-info">
                <h3>${project.title || 'Untitled Project'}</h3>
                <p class="project-description">${project.description || ''}</p>
                <div class="project-tech">
                    ${(project.technologies || '').split(',')
                        .map(tech => `<span class="tech-tag">${tech.trim()}</span>`)
                        .join('')}
                </div>
            </div>
        </div>
    `;
    
    return div;
}

function updateNavigationButtons(currentGroup, totalGroups) {
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if (prevBtn && nextBtn) {
        // Remove disabled attribute and update styles
        prevBtn.removeAttribute('disabled');
        nextBtn.removeAttribute('disabled');
        prevBtn.style.opacity = '1';
        nextBtn.style.opacity = '1';
        
        // Remove any inline styles
        prevBtn.removeAttribute('style');
        nextBtn.removeAttribute('style');
        
        // Remove and re-add event listeners
        const newPrevBtn = prevBtn.cloneNode(true);
        const newNextBtn = nextBtn.cloneNode(true);
        
        prevBtn.parentNode.replaceChild(newPrevBtn, prevBtn);
        nextBtn.parentNode.replaceChild(newNextBtn, nextBtn);
        
        newPrevBtn.addEventListener('click', (e) => {
            e.preventDefault();
            navigateProjects('prev');
        });
        
        newNextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            navigateProjects('next');
        });
    }
}

function setupProjectNavigation() {
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    
    if (prevBtn && nextBtn) {
        // Remove any existing attributes
        prevBtn.removeAttribute('disabled');
        prevBtn.removeAttribute('enabled');
        nextBtn.removeAttribute('disabled');
        nextBtn.removeAttribute('enabled');
        
        // Remove inline styles
        prevBtn.removeAttribute('style');
        nextBtn.removeAttribute('style');
        
        // Add event listeners
        prevBtn.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Previous button clicked');
            navigateProjects('prev');
        });
        
        nextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('Next button clicked');
            navigateProjects('next');
        });
        
        // Initialize indicators and buttons
        const projects = document.querySelectorAll('.project-bubble');
        const totalGroups = Math.ceil(projects.length / 3);
        updateNavigationIndicators(0, totalGroups);
        updateNavigationButtons(0, totalGroups);
    }
}

function navigateProjects(direction) {
    const projects = document.querySelectorAll('.project-bubble');
    const totalGroups = Math.ceil(projects.length / 3);
    let currentGroup = 0;

    // Find current group
    projects.forEach((project, index) => {
        if (project.classList.contains('active')) {
            currentGroup = Math.floor(index / 3);
        }
    });

    // Calculate next group with proper backward navigation
    let nextGroup;
    if (direction === 'next') {
        nextGroup = (currentGroup + 1) % totalGroups;
    } else {
        // Ensure proper backward wrapping
        nextGroup = currentGroup - 1;
        if (nextGroup < 0) {
            nextGroup = totalGroups - 1;
        }
    }

    console.log(`Navigation: Current Group ${currentGroup}, Next Group ${nextGroup}, Direction ${direction}`);

    // Hide all projects first
    projects.forEach(project => {
        project.classList.add('hidden');
        project.classList.remove('active');
    });

    // Show projects for the next group
    const startIndex = nextGroup * 3;
    const endIndex = Math.min(startIndex + 3, projects.length);
    
    console.log(`Showing projects from index ${startIndex} to ${endIndex - 1}`);
    
    for (let i = startIndex; i < endIndex; i++) {
        projects[i].classList.remove('hidden');
        projects[i].classList.add('active');
    }

    // Update navigation indicators
    updateNavigationIndicators(nextGroup, totalGroups);
}

function updateNavigationIndicators(currentGroup, totalGroups) {
    const nav = document.querySelector('.projects-nav');
    if (!nav) return;

    // Clear existing indicators
    const existingIndicators = nav.querySelector('.nav-indicators');
    if (existingIndicators) {
        existingIndicators.remove();
    }

    // Create new indicators
    const indicators = document.createElement('div');
    indicators.className = 'nav-indicators';
    
    for (let i = 0; i < totalGroups; i++) {
        const dot = document.createElement('span');
        dot.className = `nav-dot ${i === currentGroup ? 'active' : ''}`;
        dot.addEventListener('click', () => {
            const diff = i - currentGroup;
            if (diff > 0) {
                for (let j = 0; j < diff; j++) {
                    setTimeout(() => navigateProjects('next'), j * 300);
                }
            } else if (diff < 0) {
                for (let j = 0; j < Math.abs(diff); j++) {
                    setTimeout(() => navigateProjects('prev'), j * 300);
                }
            }
        });
        indicators.appendChild(dot);
    }

    // Insert indicators between navigation buttons
    const nextBtn = nav.querySelector('.next-btn');
    nav.insertBefore(indicators, nextBtn);
}

// Add keyboard navigation
document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') {
        event.preventDefault();
        navigateProjects('prev');
    } else if (event.key === 'ArrowRight') {
        event.preventDefault();
        navigateProjects('next');
    }
});

// Add this function to test the API endpoint
function testAPI() {
    fetch('/api/projects/')
        .then(response => {
            console.log('API Response:', response);
            return response.json();
        })
        .then(data => {
            console.log('API Data:', data);
        })
        .catch(error => {
            console.error('API Error:', error);
        });
}

async function handleProjectSubmission(event) {
    event.preventDefault();
    
    try {
        const formData = new FormData(event.target);
        const projectData = {
            title: formData.get('title'),
            description: formData.get('description'),
            image_url: formData.get('image_url'),
            github: formData.get('github'),
            technologies: formData.get('technologies'),
        };

        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(projectData)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Refresh projects list
        await loadProjects();
        
        // Clear form
        event.target.reset();
        
        alert('Project added successfully!');
    } catch (error) {
        console.error('Error adding project:', error);
        alert('Failed to add project: ' + error.message);
    }
}

// Add project form handling
async function handleProjectSubmit(event) {
    event.preventDefault();
    
    try {
        const form = event.target;
        const formData = new FormData(form);
        
        // Log form data for debugging
        for (let [key, value] of formData.entries()) {
            console.log(key + ':', value);
        }

        const response = await fetch(`${BASE_URL}/api/firebase/`, {
            method: 'POST',
            body: formData
        });

        console.log('Response status:', response.status);
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Server response:', result);
        
        showToast('Project added successfully!', 'success');
        form.reset();
        await loadProjects();
        
    } catch (error) {
        console.error('Error adding project:', error);
        showToast('Failed to add project: ' + error.message, 'error');
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing projects...');
    loadProjects();
    
    // Set up project form
    const projectForm = document.getElementById('projectForm');
    if (projectForm) {
        projectForm.addEventListener('submit', handleProjectSubmit);
    }
});
