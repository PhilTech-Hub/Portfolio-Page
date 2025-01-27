// Open CV Popup
function openCVPopup() {
    document.getElementById('cv-popup').style.display = 'flex';
}

// Close CV Popup
function closeCVPopup() {
    document.getElementById('cv-popup').style.display = 'none';
}

// Download CV
function downloadCV() {
    window.location.href = "{{ url_for('download_cv') }}";
}

// Navigate to More Certifications
function navigateToMoreCertifications() {
    window.location.href = '/certifications'; // Update with your actual route
}
