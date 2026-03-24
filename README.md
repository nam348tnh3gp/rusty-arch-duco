# 🐧 Rusty Arch Duco

**Automated Arch Linux image builder with integrated Duino-Coin miner using GitHub Actions**

---

## 🚀 Introduction

**Rusty Arch Duco** is a project that builds a custom image based on Arch Linux, automatically generated via CI/CD and preloaded with a miner for Duino-Coin.

👉 Key advantages:

* No manual build required
* No need to install the miner
* Just download → boot → run

---

## ⚙️ How It Works

The pipeline uses GitHub Actions to:

1. 🧱 Create a disk image (4GB)
2. 💽 Partition it (EFI + root)
3. 🐧 Bootstrap Arch Linux using Docker
4. 📦 Install:

   * Base system
   * Kernel + firmware
   * Rust toolchain
5. 🦀 Compile the miner from source (`cargo build --release`)
6. ⚡ Set up auto-run using `tmux`
7. 🧼 Clean up and compress the image (`.xz`)
8. 📤 Upload as an artifact

---

## ✨ Features

* 🐧 Minimal Arch Linux system
* 🦀 Prebuilt Rust-based DUCO miner
* ⚡ Auto-start miner on login (via `tmux`)
* 🔌 NetworkManager enabled
* 🔐 Default users:

  * `root / duco`
  * `miner / miner`
* 💾 Compressed `.xz` image (smaller size)

---

## 📦 Output

After the workflow completes, you will get:

* `arch-duco.img.xz` – disk image
* `arch-duco.img.xz.sha256` – checksum

Download from:
👉 **Actions → Artifacts**

---

## 🛠️ Usage

### 1. Download image

Extract:

```bash
xz -d arch-duco.img.xz
```

---

### 2. Flash to USB / VPS

```bash
sudo dd if=arch-duco.img of=/dev/sdX bs=4M status=progress
```

---

### 3. Boot

* Boot from USB or disk
* Login with:

  * `root / duco`
  * or `miner / miner`

---

## ⛏️ Miner

The miner is:

* Built from source at:

  ```
  /root/rust-miner
  ```

* Binary location:

  ```
  /root/rust-miner/target/release/duco_rust_miner
  ```

---

## 🧠 Auto Mining

On login, the system will:

* Automatically start `tmux`
* Create a session named `mining`
* Run the miner

```bash
tmux attach -t mining
```

---

## ⚙️ Customization

You can modify:

### 🔹 Miner source

```
miner/*
```

---

### 🔹 Workflow

File:

```
.github/workflows/build.yml
```

You can adjust:

* Image size
* Installed packages
* Kernel
* Bootloader
* Miner configuration

---

## 📈 Advantages

* 🔄 Reproducible builds (CI)
* 🚀 No manual setup required
* 🧪 Easy to test multiple miner versions
* 🧱 Full system control

---

## 🧪 TODO

* [ ] Auto-config miner (username)
* [ ] Replace `tmux` with systemd service
* [ ] Headless auto-login
* [ ] ARM build (Raspberry Pi)
* [ ] OTA updates

---

## 🔐 Security

After boot:

```bash
passwd
passwd miner
```

---

## 📄 License

MIT License

---

## 👤 Author

* GitHub: https://github.com/nam348tnh3gp

---

## ⭐ Support

If you find this project useful, please consider giving it a ⭐!
