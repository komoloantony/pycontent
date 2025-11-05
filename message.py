# secret_encryptor.py
"""
Secret Message Encryption & Decryption Tool (Tkinter GUI)

Features:
 - Ciphers: Caesar, Vigenere, XOR, Base64
 - Optional AES (requires `pycryptodome`): pip install pycryptodome
 - Encrypt / Decrypt buttons
 - Copy result to clipboard
 - Save to file / Load from file
 - Clear inputs and basic status messages

This is an educational tool. AES (when enabled) uses CBC with PKCS7 padding.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import base64
import sys

# Try to import AES from pycryptodome (optional)
HAS_AES = False
try:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes
    HAS_AES = True
except Exception:
    HAS_AES = False

# ----------------------
# Utility / Cipher code
# ----------------------

def caesar_encrypt(text: str, shift: int) -> str:
    """Simple Caesar cipher (letters only, preserves case; other chars unchanged)."""
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(plaintext: str, key: str) -> str:
    """Vigenere cipher - non-letter chars are left unchanged (key cycles over letters only)."""
    if not key:
        raise ValueError("Vigenere requires a non-empty key.")
    result = []
    key_idx = 0
    key = key
    for ch in plaintext:
        k = key[key_idx % len(key)]
        # make shift from letter (A/a => 0)
        if k.isalpha():
            shift = ord(k.lower()) - ord('a')
        else:
            # if key char non-alpha, treat as 0
            shift = 0
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
            key_idx += 1
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
            key_idx += 1
        else:
            result.append(ch)
    return ''.join(result)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    if not key:
        raise ValueError("Vigenere requires a non-empty key.")
    result = []
    key_idx = 0
    for ch in ciphertext:
        k = key[key_idx % len(key)]
        if k.isalpha():
            shift = ord(k.lower()) - ord('a')
        else:
            shift = 0
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') - shift) % 26 + ord('a')))
            key_idx += 1
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') - shift) % 26 + ord('A')))
            key_idx += 1
        else:
            result.append(ch)
    return ''.join(result)

def xor_encrypt_decrypt(text: str, key: str) -> str:
    """XOR cipher over bytes. Produces/accepts base64 encoded output for binary-safety."""
    if not key:
        raise ValueError("XOR requires a non-empty key.")
    tbytes = text.encode('utf-8')
    kbytes = key.encode('utf-8')
    out = bytearray()
    for i, b in enumerate(tbytes):
        out.append(b ^ kbytes[i % len(kbytes)])
    # return base64 so result can be displayed safely
    return base64.b64encode(bytes(out)).decode('utf-8')

def xor_decrypt_from_b64(b64text: str, key: str) -> str:
    if not key:
        raise ValueError("XOR requires a non-empty key.")
    try:
        data = base64.b64decode(b64text)
    except Exception:
        raise ValueError("Input is not valid base64 for XOR decrypted data.")
    kbytes = key.encode('utf-8')
    out = bytearray()
    for i, b in enumerate(data):
        out.append(b ^ kbytes[i % len(kbytes)])
    return bytes(out).decode('utf-8', errors='replace')

def base64_encrypt(text: str) -> str:
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def base64_decrypt(b64text: str) -> str:
    try:
        return base64.b64decode(b64text.encode('utf-8')).decode('utf-8')
    except Exception:
        raise ValueError("Input is not valid base64.")

# AES helpers (optional)
def pad_pkcs7(data: bytes, block_size=16) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len]) * pad_len

def unpad_pkcs7(data: bytes) -> bytes:
    if not data:
        raise ValueError("No data to unpad.")
    pad_len = data[-1]
    if pad_len <= 0 or pad_len > 16:
        raise ValueError("Invalid padding.")
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("Invalid padding bytes.")
    return data[:-pad_len]

def aes_encrypt(plaintext: str, key: str) -> str:
    """AES-CBC encrypt; returns base64 of IV + ciphertext. Key is hashed/truncated to 16/24/32 bytes."""
    if not HAS_AES:
        raise RuntimeError("AES requires pycryptodome. Install with: pip install pycryptodome")
    if not key:
        raise ValueError("AES requires a non-empty key.")
    # Create a key of 16/24/32 bytes from provided key (simple: pad/truncate)
    raw_key = key.encode('utf-8')
    if len(raw_key) not in (16, 24, 32):
        # pad or truncate to 32 bytes (most compatible)
        if len(raw_key) < 32:
            raw_key = raw_key.ljust(32, b'\0')
        else:
            raw_key = raw_key[:32]
    iv = get_random_bytes(16)
    cipher = AES.new(raw_key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad_pkcs7(plaintext.encode('utf-8')))
    return base64.b64encode(iv + ct).decode('utf-8')

def aes_decrypt(b64text: str, key: str) -> str:
    if not HAS_AES:
        raise RuntimeError("AES requires pycryptodome. Install with: pip install pycryptodome")
    if not key:
        raise ValueError("AES requires a non-empty key.")
    try:
        raw = base64.b64decode(b64text)
    except Exception:
        raise ValueError("Input is not valid base64 for AES.")
    if len(raw) < 16:
        raise ValueError("Invalid AES input (too short).")
    iv = raw[:16]
    ct = raw[16:]
    raw_key = key.encode('utf-8')
    if len(raw_key) not in (16, 24, 32):
        if len(raw_key) < 32:
            raw_key = raw_key.ljust(32, b'\0')
        else:
            raw_key = raw_key[:32]
    cipher = AES.new(raw_key, AES.MODE_CBC, iv)
    pt = unpad_pkcs7(cipher.decrypt(ct))
    return pt.decode('utf-8', errors='replace')

# ----------------------
# GUI
# ----------------------

class SecretApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secret Message Encryptor")
        self.geometry("700x520")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Top: instructions and cipher choice
        frame_top = ttk.Frame(self, padding=(10, 10, 10, 0))
        frame_top.pack(fill='x')

        ttk.Label(frame_top, text="Enter your message below:").pack(anchor='w')
        self.msg_text = tk.Text(frame_top, height=6, wrap='word')
        self.msg_text.pack(fill='x', pady=(5, 8))

        # Middle row: key and cipher selection
        mid = ttk.Frame(self, padding=(10, 5))
        mid.pack(fill='x')

        ttk.Label(mid, text="Key (if needed):").grid(row=0, column=0, sticky='w')
        self.key_entry = ttk.Entry(mid, width=40)
        self.key_entry.grid(row=0, column=1, sticky='w', padx=(5, 15))

        ttk.Label(mid, text="Cipher:").grid(row=0, column=2, sticky='w')
        self.cipher_var = tk.StringVar(value='Caesar')
        options = ['Caesar', 'Vigenere', 'XOR', 'Base64']
        if HAS_AES:
            options.append('AES (CBC)')
        self.cipher_menu = ttk.Combobox(mid, values=options, textvariable=self.cipher_var, state='readonly', width=20)
        self.cipher_menu.grid(row=0, column=3, sticky='w')

        ttk.Label(mid, text="Caesar shift (for Caesar only):").grid(row=1, column=0, sticky='w', pady=(8,0))
        self.shift_entry = ttk.Entry(mid, width=10)
        self.shift_entry.insert(0, "3")  # default shift
        self.shift_entry.grid(row=1, column=1, sticky='w', pady=(8,0))

        # Buttons: Encrypt / Decrypt / Clear
        btn_frame = ttk.Frame(self, padding=(10, 8))
        btn_frame.pack(fill='x')
        encrypt_btn = ttk.Button(btn_frame, text="Encrypt →", command=self.encrypt_action)
        encrypt_btn.pack(side='left', padx=4)
        decrypt_btn = ttk.Button(btn_frame, text="← Decrypt", command=self.decrypt_action)
        decrypt_btn.pack(side='left', padx=4)
        clear_btn = ttk.Button(btn_frame, text="Clear All", command=self.clear_all)
        clear_btn.pack(side='left', padx=4)

        # Bottom: output, copy, save, load
        out_frame = ttk.Frame(self, padding=(10, 5))
        out_frame.pack(fill='both', expand=True)

        ttk.Label(out_frame, text="Result:").pack(anchor='w')
        self.out_text = tk.Text(out_frame, height=10, wrap='word', background='#f7f7f7')
        self.out_text.pack(fill='both', expand=True, pady=(5, 8))

        action_row = ttk.Frame(out_frame)
        action_row.pack(fill='x', pady=(5, 5))
        copy_btn = ttk.Button(action_row, text="Copy to Clipboard", command=self.copy_result)
        copy_btn.pack(side='left', padx=4)
        save_btn = ttk.Button(action_row, text="Save Result...", command=self.save_result)
        save_btn.pack(side='left', padx=4)
        load_btn = ttk.Button(action_row, text="Load Message...", command=self.load_message)
        load_btn.pack(side='left', padx=4)

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status = ttk.Label(self, textvariable=self.status_var, relief='sunken', anchor='w', padding=5)
        status.pack(side='bottom', fill='x')

    # -----------------
    # Button handlers
    # -----------------
    def encrypt_action(self):
        cipher = self.cipher_var.get()
        msg = self.msg_text.get('1.0', 'end').rstrip('\n')
        key = self.key_entry.get()
        try:
            if cipher == 'Caesar':
                shift = int(self.shift_entry.get() or 0)
                out = caesar_encrypt(msg, shift)
            elif cipher == 'Vigenere':
                out = vigenere_encrypt(msg, key)
            elif cipher == 'XOR':
                out = xor_encrypt_decrypt(msg, key)
            elif cipher == 'Base64':
                out = base64_encrypt(msg)
            elif cipher.startswith('AES'):
                out = aes_encrypt(msg, key)
            else:
                raise ValueError("Unsupported cipher.")
            self.out_text.delete('1.0', 'end')
            self.out_text.insert('1.0', out)
            self.status_var.set(f"Encrypted with {cipher}")
        except Exception as e:
            messagebox.showerror("Encryption Error", str(e))
            self.status_var.set("Error during encryption")

    def decrypt_action(self):
        cipher = self.cipher_var.get()
        txt = self.out_text.get('1.0', 'end').rstrip('\n')
        key = self.key_entry.get()
        try:
            if cipher == 'Caesar':
                shift = int(self.shift_entry.get() or 0)
                out = caesar_decrypt(txt, shift)
            elif cipher == 'Vigenere':
                out = vigenere_decrypt(txt, key)
            elif cipher == 'XOR':
                out = xor_decrypt_from_b64(txt, key)
            elif cipher == 'Base64':
                out = base64_decrypt(txt)
            elif cipher.startswith('AES'):
                out = aes_decrypt(txt, key)
            else:
                raise ValueError("Unsupported cipher.")
            # Put decrypted text back into message area (so user can edit or re-encrypt)
            self.msg_text.delete('1.0', 'end')
            self.msg_text.insert('1.0', out)
            self.status_var.set(f"Decrypted with {cipher}")
        except Exception as e:
            messagebox.showerror("Decryption Error", str(e))
            self.status_var.set("Error during decryption")

    def copy_result(self):
        text = self.out_text.get('1.0', 'end').rstrip('\n')
        if not text:
            self.status_var.set("Nothing to copy")
            return
        self.clipboard_clear()
        self.clipboard_append(text)
        self.status_var.set("Result copied to clipboard")

    def save_result(self):
        text = self.out_text.get('1.0', 'end').rstrip('\n')
        if not text:
            self.status_var.set("Nothing to save")
            return
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not filepath:
            return
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
            self.status_var.set(f"Saved to {filepath}")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))
            self.status_var.set("Error saving file")

    def load_message(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not filepath:
            return
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # put loaded content into message area
            self.msg_text.delete('1.0', 'end')
            self.msg_text.insert('1.0', content)
            self.status_var.set(f"Loaded message from {filepath}")
        except Exception as e:
            messagebox.showerror("Load Error", str(e))
            self.status_var.set("Error loading file")

    def clear_all(self):
        self.msg_text.delete('1.0', 'end')
        self.out_text.delete('1.0', 'end')
        self.key_entry.delete(0, 'end')
        self.status_var.set("Cleared")

# ----------------------
# Run the app
# ----------------------
if __name__ == "__main__":
    if not HAS_AES:
        print("Note: AES support disabled (pycryptodome not installed). To enable AES run: pip install pycryptodome")
    app = SecretApp()
    app.mainloop()
