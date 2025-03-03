import CertificationsModel from './models/CertificationsModel.js';

const certModel = new CertificationsModel();

async function loadCertifications() {
    try {
        const certificates = await certModel.getAllCertifications();
        displayCertificates(certificates);
    } catch (error) {
        console.error('Error loading certifications:', error);
        showToast('Error loading certifications', 'error');
    }
}

function displayCertificates(certificates) {
    const certificatesContainer = document.getElementById('certificatesContainer');
    if (!certificatesContainer) return;

    certificatesContainer.innerHTML = '';
    
    certificates.forEach(cert => {
        const certElement = document.createElement('div');
        certElement.className = 'certificate-card';
        certElement.innerHTML = `
            <div class="cert-icon">
                <img src="${cert.icon_url}" alt="${cert.title}">
            </div>
            <div class="cert-content">
                <h3 class="cert-title">${cert.title}</h3>
                <p class="cert-issuer">${cert.issuer}</p>
                
                <ul class="cert-details">
                    ${cert.details.map(detail => `
                        <li>${detail}</li>
                    `).join('')}
                </ul>
                
                <div class="cert-footer">
                    <span class="cert-date">${cert.issue_date}</span>
                    <a href="${cert.credential_url}" class="view-cert-btn" target="_blank">
                        View Certificate
                        <i class="fas fa-external-link-alt"></i>
                    </a>
                </div>
            </div>
        `;
        certificatesContainer.appendChild(certElement);
    });
}

// Load certificates when the page loads
document.addEventListener('DOMContentLoaded', () => {
    const certButtons = document.querySelectorAll('.view-cert');
    
    certButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Find the closest certification card parent
            const certCard = button.closest('.certification-card');
            const pdfPath = certCard.getAttribute('data-pdf');
            
            if (pdfPath) {
                // If PDF exists, open it in a new tab
                window.open(pdfPath, '_blank');
            } else {
                // If no PDF, show the toast message
                showToast('Certificate not available yet. Please check back later!', 'warning');
            }
        });
    });

    // Add hover effect to show different tooltips based on PDF availability
    const certCards = document.querySelectorAll('.certification-card');
    
    certCards.forEach(card => {
        const viewButton = card.querySelector('.view-cert');
        const hasPdf = card.hasAttribute('data-pdf');
        
        viewButton.setAttribute('title', hasPdf ? 'Click to view certificate' : 'Certificate coming soon');
        
        if (hasPdf) {
            viewButton.classList.add('has-pdf');
        }
    });
}); 