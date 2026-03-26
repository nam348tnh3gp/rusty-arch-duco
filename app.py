from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)

# Đường dẫn thư mục chứa file tĩnh (CSS, JS, favicon)
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
# Đường dẫn thư mục gốc chứa ads.txt và .well-known
ROOT_DIR = os.path.dirname(__file__)

# Đảm bảo thư mục static tồn tại
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(os.path.join(ROOT_DIR, '.well-known'), exist_ok=True)

# === NỘI DUNG HTML ===
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Rusty Arch Duco - Custom Arch Linux image with built-in Duino-Coin miner. Download and start mining DUCO in minutes!">
    <meta name="keywords" content="Arch Linux, Duino-Coin, DUCO, mining, Rust, cryptocurrency">
    <title>Rusty Arch Duco | Arch Linux + DUCO Miner</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">
                <a href="/">🐧 Rusty Arch Duco</a>
            </div>
            <div class="nav-links">
                <a href="/">Home</a>
                <a href="/docs/install.html">Install</a>
                <a href="/blog/">Blog</a>
                <a href="https://duco-faucet-wgha.onrender.com" target="_blank">Faucet</a>
                <a href="https://github.com/nam348tnh3gp/rusty-arch-duco" target="_blank">GitHub</a>
            </div>
        </div>
    </nav>

    <header class="hero">
        <div class="container">
            <h1>🐧 Rusty Arch Duco</h1>
            <p class="tagline">Arch Linux image with built-in Duino-Coin miner</p>
            <p class="description">Download, boot, and start mining DUCO in minutes. No manual setup required!</p>
            <div class="hero-buttons">
                <a href="#download" class="btn btn-primary">Download Now</a>
                <a href="https://github.com/nam348tnh3gp/rusty-arch-duco" class="btn btn-secondary">GitHub</a>
            </div>
        </div>
    </header>

    <section class="features">
        <div class="container">
            <h2>✨ Features</h2>
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">🚀</div>
                    <h3>Ready to Mine</h3>
                    <p>Pre-installed DUCO miner, auto-start on login. Just boot and go!</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>CI/CD Built</h3>
                    <p>Automatically built with GitHub Actions. Always up-to-date.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🦀</div>
                    <h3>Rust Miner</h3>
                    <p>High-performance miner written in Rust. Optimized for speed.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💾</div>
                    <h3>Complete System</h3>
                    <p>Full Arch Linux system with everything pre-configured. Image size: 1.85GB</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔧</div>
                    <h3>Customizable</h3>
                    <p>Fork the repo and build your own image with custom config.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🖥️</div>
                    <h3>UEFI Ready</h3>
                    <p>Supports both UEFI and legacy BIOS boot modes.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="download" class="download">
        <div class="container">
            <h2>📦 Download</h2>
            <div class="download-card">
                <div class="download-info">
                    <p class="version">Latest build: <span id="build-date">Build #23412082693 (March 22, 2026)</span></p>
                    <p class="size">Size: <strong>1.85 GB</strong> (compressed .xz)</p>
                    <p class="checksum">SHA256: <code id="checksum">6da3682...</code></p>
                </div>
                <div class="download-buttons">
                    <a href="https://github.com/nam348tnh3gp/rusty-arch-duco/actions/runs/23412082693" class="btn btn-download" target="_blank">
                        <span>📥 Download Image (1.85GB)</span>
                        <small>from GitHub Actions Artifacts →</small>
                    </a>
                    <a href="/docs/install.html" class="btn btn-outline">Install Guide</a>
                </div>
                <p class="download-note">💡 <strong>Note:</strong> Click the link above, then scroll down to the "Artifacts" section and download <code>arch-duco-img</code>.</p>
            </div>
        </div>
    </section>

    <section class="how-it-works">
        <div class="container">
            <h2>⚙️ How It Works</h2>
            <div class="steps">
                <div class="step">
                    <div class="step-number">1</div>
                    <h3>Download Image</h3>
                    <p>Get the latest <code>arch-duco.img.xz</code> (1.85GB) from the run's Artifacts section.</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h3>Extract & Flash</h3>
                    <p><code>xz -d arch-duco.img.xz</code> then <code>dd if=arch-duco.img of=/dev/sdX bs=4M</code></p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h3>Boot & Mine</h3>
                    <p>Boot from USB, login with <code>miner/miner</code>, and watch it mine!</p>
                </div>
            </div>
        </div>
    </section>

    <section class="faucet-redirect">
        <div class="container">
            <h2>💰 Free DUCO Faucet</h2>
            <p class="section-desc">Claim free DUCO every day to support your mining journey!</p>
            <div class="faucet-card">
                <a href="https://duco-faucet-wgha.onrender.com" class="btn btn-primary" target="_blank">
                    🎁 Visit DUCO Faucet →
                </a>
                <p class="faucet-info">🎲 Random amount: 1-20 DUCO | 1 claim per 24h | 70% (1-10) | 20% (10-15) | 10% (15-20)</p>
            </div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-section">
                    <h4>Rusty Arch Duco</h4>
                    <p>Open-source Arch Linux image with built-in Duino-Coin miner.</p>
                </div>
                <div class="footer-section">
                    <h4>Links</h4>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/docs/install.html">Install Guide</a></li>
                        <li><a href="/blog/">Blog</a></li>
                        <li><a href="https://duco-faucet-wgha.onrender.com" target="_blank">Faucet</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Community</h4>
                    <ul>
                        <li><a href="https://github.com/nam348tnh3gp/rusty-arch-duco" target="_blank">GitHub</a></li>
                        <li><a href="https://discord.gg/duinocoin" target="_blank">Discord</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Support</h4>
                    <p>⭐ Star on GitHub if you find this useful!</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2026 Rusty Arch Duco. MIT License.</p>
            </div>
        </div>
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>'''


# === ROUTES ===
@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

# Phục vụ file tĩnh (CSS, JS, favicon)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

# Phục vụ ads.txt
@app.route('/ads.txt')
def serve_ads_txt():
    ads_path = os.path.join(ROOT_DIR, 'ads.txt')
    if os.path.exists(ads_path):
        return send_from_directory(ROOT_DIR, 'ads.txt', mimetype='text/plain')
    return 'ads.txt not found', 404

# Phục vụ Discord verification
@app.route('/.well-known/discord')
def serve_discord_verification():
    discord_path = os.path.join(ROOT_DIR, '.well-known', 'discord')
    if os.path.exists(discord_path):
        with open(discord_path, 'r') as f:
            content = f.read().strip()
        return content, 200, {'Content-Type': 'text/plain'}
    return 'Discord verification file not found', 404

# Phục vụ các file HTML tĩnh (docs, blog)
@app.route('/<path:filename>')
def serve_html(filename):
    file_path = os.path.join(ROOT_DIR, filename)
    if os.path.exists(file_path) and filename.endswith('.html'):
        return send_from_directory(ROOT_DIR, filename, mimetype='text/html')
    return 'File not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
