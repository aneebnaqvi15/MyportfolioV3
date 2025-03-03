# Modern Portfolio Website

A modern, responsive portfolio website built with HTML, CSS, and JavaScript. Features a sleek design, smooth animations, and interactive elements to showcase your professional work and skills.

## 🌟 Features

### 1. Modern UI/UX
- Responsive design that works on all devices
- Smooth scroll animations using GSAP
- Interactive hover effects and transitions
- Neon glow effects and modern glassmorphism design
- Particle effects in the hero section

### 2. Navigation
- Fixed navbar with smooth scrolling
- Mobile-responsive hamburger menu
- Active section highlighting
- Back to top button

### 3. Sections

#### Hero Section
- Animated text introduction
- Particle effect background
- Social media links
- Call-to-action buttons

#### About Section
- Professional introduction
- Key highlights
- Downloadable resume option

#### Education & Certifications
- Academic background with timeline
- Professional certifications
- Interactive certification cards with hover effects
- View certificate functionality

#### Skills Section
- Categorized skill display (Frontend, Backend, etc.)
- Progress bars with animations
- Technology icons with tooltips
- Skill cards with hover effects

#### Projects Section
- Project carousel/slider
- Interactive project cards
- GitHub links
- Live demo links
- Technology tags
- Project screenshots

#### Contact Section
- Contact form with EmailJS integration
- Social media links
- Toast notifications for form submission
- Form validation

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3 (with custom properties)
- JavaScript (ES6+)

### Libraries & APIs
- GSAP (animations)
- Font Awesome (icons)
- EmailJS (contact form)
- AOS (Animate On Scroll)

### Development Tools
- VS Code
- Git & GitHub
- Chrome DevTools

## 📥 Installation & Setup

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/yourusername/portfolio.git
   \`\`\`

2. Navigate to the project directory:
   \`\`\`bash
   cd portfolio
   \`\`\`

3. Install dependencies (if using a package manager):
   \`\`\`bash
   npm install
   \`\`\`

4. Configure EmailJS:
   - Sign up at [EmailJS](https://www.emailjs.com/)
   - Create a new email service
   - Get your public key
   - Update the key in \`main.js\`:
     \`\`\`javascript
     emailjs.init("YOUR_PUBLIC_KEY");
     \`\`\`

## 🚀 Deployment

### Option 1: GitHub Pages

1. Go to your repository settings
2. Navigate to "Pages"
3. Select your main branch as source
4. Save the changes
5. Your site will be live at \`https://yourusername.github.io/portfolio\`

### Option 2: Netlify

1. Sign up for a Netlify account
2. Connect your GitHub repository
3. Configure build settings:
   - Build command: (leave empty for static sites)
   - Publish directory: \`./\`
4. Deploy

### Option 3: Vercel

1. Sign up for a Vercel account
2. Import your GitHub repository
3. Configure project settings:
   - Framework Preset: Other
   - Build Command: (leave empty)
   - Output Directory: \`./\`
4. Deploy

## 💻 Usage & Customization

### Modifying Content

1. **Personal Information**
   - Edit text content in \`index.html\`
   - Update meta tags for SEO
   - Replace profile image in \`images/\` directory

2. **Projects**
   - Add new projects in the projects section
   - Update project images
   - Modify project descriptions and links

3. **Skills**
   - Update skill percentages in \`main.js\`
   - Add or remove skill categories
   - Modify skill icons

4. **Styling**
   - Colors: Edit CSS variables in \`style.css\`
   - Animations: Modify GSAP animations in \`main.js\`
   - Layout: Adjust CSS Grid/Flexbox properties

### Adding Features

1. **New Sections**
   - Create HTML markup
   - Add corresponding CSS
   - Implement JavaScript functionality if needed
   - Update navigation

2. **Custom Animations**
   - Add new GSAP animations in \`main.js\`
   - Create CSS keyframe animations
   - Modify AOS attributes

## 🔧 Troubleshooting

### Common Issues

1. **Email Form Not Working**
   - Verify EmailJS configuration
   - Check console for errors
   - Ensure proper template variables

2. **Animations Not Smooth**
   - Reduce animation complexity
   - Check browser compatibility
   - Optimize image sizes

3. **Mobile Menu Issues**
   - Clear browser cache
   - Check z-index conflicts
   - Verify event listeners

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Opera (latest)

## 🤝 Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request


## 📞 Support

For support, email syedaneebajk00786@.com or create an issue in the repository.

## 🙏 Acknowledgments

- Font Awesome for icons
- GSAP for animations
- EmailJS for email service
- Unsplash for stock images
- Google Fonts for typography
- 
