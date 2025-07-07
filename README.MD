# Roblox Account Automation (Educational)

> ⚠️ **DISCLAIMER**  
> This project is for **educational purposes only**.  
> Do **not** use this to violate Roblox’s [Terms of Use](https://en.help.roblox.com/hc/en-us/articles/115004647846) or perform unauthorized actions.  
> You are solely responsible for your actions. The creators of this code take **no responsibility** for any misuse.

---

## 📌 What This Project Does

This script demonstrates how to simulate secure client-side generation for Roblox signup using:

- Reverse-engineered SAI (Secure Authentication Intent)
- Roblox CSRF token fetching
- Cookie handling
- (Optional) captcha challenge handling

It’s primarily intended to show how SAI-based authentication flows work, using Python and HTTPS requests.

---

## 🛠️ Requirements

- Python 3.8+
- pip packages:
  ```bash
  pip install -r requirements.txt
  ```

### Required Packages

- `requests`
- `beautifulsoup4`
- `cryptography`
- `tls-client`
- `pytermx`

---

## 🚀 How to Use

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:

   ```bash
   python test.py
   ```

3. You will see output like:

   ```
   [*] Get Server Nonce...
   [*] Get Client Public Key...
   [*] CSRF Token: ...
   [*] Cookies: ...
   [*] Secure Auth Block: ...
   ```

---

## ⚠️ Legal Note

This repository is a **reverse engineering proof of concept** for educational and research use only. It does not bypass CAPTCHA, and does not perform actual account creation unless you modify it to do so.

We **do not condone or encourage** botting, spamming, or automated account creation on Roblox or any other platform. Use responsibly.

If you're a developer from Roblox and wish something to be removed, open an issue or contact us.

---

## 📄 License

MIT — Use freely, but **don’t abuse**.
