// Load download stats (có thể dùng GitHub API)
async function loadDownloadStats() {
    try {
        // GitHub API để lấy số lần clone/download (ước lượng)
        const response = await fetch('https://api.github.com/repos/nam348tnh3gp/rusty-arch-duco');
        const data = await response.json();
        
        if (data && data.stargazers_count) {
            const stars = data.stargazers_count;
            const downloads = stars * 10; // ước lượng
            document.getElementById('total-downloads').textContent = formatNumber(downloads);
        }
    } catch (e) {
        console.log('Stats API not available');
    }
}

function formatNumber(num) {
    if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
    if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
    return num.toString();
}

// Animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.feature-card, .step, .download-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.5s ease';
    observer.observe(el);
});

// Load on page ready
document.addEventListener('DOMContentLoaded', () => {
    loadDownloadStats();
});
