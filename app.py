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
    <meta name="description" content="Rusty Arch Duco - Custom Arch Linux image with built-in Duino-Coin miner. Choose between GUI or terminal-only version.">
    <meta name="keywords" content="Arch Linux, Duino-Coin, DUCO, mining, Rust, cryptocurrency, GUI, Xfce">
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
                    <h3>Two Versions</h3>
                    <p>Choose between <strong>Terminal-only</strong> (~1.6GB) or <strong>Xfce GUI</strong> (~2.1GB) version.</p>
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
            
            <!-- Terminal Version (No GUI) -->
            <div class="download-card terminal-version">
                <div class="version-badge">💻 Terminal Only</div>
                <h3>Rusty Arch Duco - Terminal Edition</h3>
                <div class="download-info">
                    <p class="version">Latest build: <span id="build-date-terminal">Build #23796788057 (March 2026)</span></p>
                    <p class="size">Download size: <strong>~1.6 GB</strong> (.xz compressed)</p>
                    <p class="description">Lightweight, terminal-only version. Perfect for servers, VPS, or minimal setups.</p>
                    <ul class="feature-list">
                        <li>✅ No GUI - pure terminal</li>
                        <li>✅ Tmux auto-start with miner</li>
                        <li>✅ SSH enabled by default</li>
                        <li>✅ Minimal resource usage</li>
                    </ul>
                </div>
                <div class="download-buttons">
                    <a href="https://github.com/nam348tnh3gp/rusty-arch-duco/actions/runs/23796788057/artifacts/6199345274" class="btn btn-download" target="_blank">
                        <span>📥 Download Terminal Edition (1.6GB)</span>
                        <small>Direct Link from GitHub →</small>
                    </a>
                    <a href="/docs/install-terminal.html" class="btn btn-outline">Install Guide</a>
                </div>
                <p class="download-note">💡 <strong>Note:</strong> After downloading, extract the <code>.xz</code> file to get <code>arch-duco.img</code> (~4GB). Flash to USB with Rufus or balenaEtcher.</p>
            </div>

            <!-- GUI Version (Xfce Desktop) -->
            <div class="download-card gui-version">
                <div class="version-badge">🖥️ Xfce GUI</div>
                <h3>Rusty Arch Duco - Xfce Edition</h3>
                <div class="download-info">
                    <p class="version">Latest build: <span id="build-date-gui">Build #23796295654 (March 2026)</span></p>
                    <p class="size">Download size: <strong>~2.1 GB</strong> (.xz compressed)</p>
                    <p class="description">Full desktop experience with Xfce. Perfect for daily use with miner running in background.</p>
                    <ul class="feature-list">
                        <li>✅ Xfce Desktop Environment</li>
                        <li>✅ Firefox pre-installed</li>
                        <li>✅ Desktop shortcut for miner</li>
                        <li>✅ LightDM login manager</li>
                    </ul>
                </div>
                <div class="download-buttons">
                    <a href="https://github.com/nam348tnh3gp/rusty-arch-duco/actions/runs/23796295654/artifacts/6199469659" class="btn btn-download" target="_blank">
                        <span>📥 Download Xfce Edition (2.1GB)</span>
                        <small>Direct Link from GitHub →</small>
                    </a>
                    <a href="/docs/install-gui.html" class="btn btn-outline">Install Guide</a>
                </div>
                <p class="download-note">💡 <strong>Note:</strong> After downloading, extract the <code>.xz</code> file to get <code>arch-duco.img</code> (~8GB). Flash to USB (minimum 16GB USB recommended).</p>
            </div>

            <div class="comparison-table">
                <h3>📊 Version Comparison</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Feature</th>
                            <th>Terminal Edition</th>
                            <th>Xfce GUI Edition</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>Desktop Environment</td><td>❌ None</td><td>✅ Xfce</td></tr>
                        <tr><td>Disk Space (extracted)</td><td>4GB</td><td>8GB</td></tr>
                        <tr><td>Download Size</td><td>~1.6GB</td><td>~2.1GB</td></tr>
                        <tr><td>USB Required</td><td>8GB+</td><td>16GB+</td></tr>
                        <tr><td>Browser Included</td><td>❌ No</td><td>✅ Firefox</td></tr>
                        <tr><td>RAM Usage (idle)</td><td>~150MB</td><td>~600MB</td></tr>
                        <tr><td>Best For</td><td>Servers, VPS, Mining Rigs</td><td>Desktop, Daily Use</td></tr>
                    </tbody>
                </table>
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
                    <p>Choose your preferred version above and download the file.</p>
                </div>
                <div class="step">
                    <div class="step-number">2</div>
                    <h3>Extract & Flash</h3>
                    <p>Extract the <code>.xz</code> file to get <code>.img</code>. Use <strong>Rufus</strong> or <strong>balenaEtcher</strong> to flash to USB.</p>
                </div>
                <div class="step">
                    <div class="step-number">3</div>
                    <h3>Boot & Mine</h3>
                    <p>Boot from USB, login with <code>miner/miner</code>. Miner starts automatically!</p>
                </div>
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
    app.run(debug=True, host='0.0.0.0', port=5000)
