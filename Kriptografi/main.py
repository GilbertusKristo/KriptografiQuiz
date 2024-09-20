import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from vigenere import vigenere_encrypt, vigenere_decrypt
from playfair import playfair_encrypt, playfair_decrypt
from hillcipher import hill_encrypt, hill_decrypt
import numpy as np

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r') as file:
                data = file.read()
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, data)
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membuka file: {e}")
    else:
        messagebox.showwarning("Warning", "Tidak ada file yang dipilih!")

def save_file(data):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(data)

def encrypt_message():
    plaintext = input_text.get("1.0", tk.END).rstrip()
    key = key_entry.get().strip()
    if not plaintext:
        messagebox.showwarning("Warning", "Input pesan tidak boleh kosong!")
        return
    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter")
        return
    if cipher_var.get() == "Vigenere":
        result = vigenere_encrypt(plaintext, key)
    elif cipher_var.get() == "Playfair":
        result = playfair_encrypt(plaintext, key)
    elif cipher_var.get() == "Hill":
        key_matrix = np.array([[2, 4, 5], [9, 2, 1], [3, 17, 7]])
        result = hill_encrypt(plaintext, key_matrix)
    print(f"Encrypted result: {result}")
    if result:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    else:
        messagebox.showerror("Error", "Enkripsi gagal, tidak ada hasil yang dihasilkan.")

def decrypt_message():
    ciphertext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    if len(key) < 12:
        messagebox.showerror("Error", "Kunci harus minimal 12 karakter")
        return
    if cipher_var.get() == "Vigenere":
        result = vigenere_decrypt(ciphertext, key)
    elif cipher_var.get() == "Playfair":
        result = playfair_decrypt(ciphertext, key)
    elif cipher_var.get() == "Hill":
        key_matrix = np.array([[2, 4, 5], [9, 2, 1], [3, 17, 7]])
        result = hill_decrypt(ciphertext, key_matrix)
    print(f"Decrypted result: {result}")
    if result:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    else:
        messagebox.showerror("Error", "Dekripsi gagal, tidak ada hasil yang dihasilkan.")

window = tk.Tk()
window.title("Kriptografi")
window.geometry("500x400")
window.resizable(False, False)

style = ttk.Style()
style.configure('TButton', font=('Arial', 10))
style.configure('TLabel', font=('Arial', 10))
style.configure('TEntry', font=('Arial', 10))

ttk.Label(window, text="Input Pesan:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
input_text = tk.Text(window, height=6, width=50)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

ttk.Label(window, text="Input Kunci (min 12 karakter):").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
key_entry = ttk.Entry(window)
key_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

ttk.Label(window, text="Pilih Cipher:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
cipher_var = tk.StringVar(value="Vigenere")
ttk.Radiobutton(window, text="Vigenere", variable=cipher_var, value="Vigenere").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
ttk.Radiobutton(window, text="Playfair", variable=cipher_var, value="Playfair").grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
ttk.Radiobutton(window, text="Hill", variable=cipher_var, value="Hill").grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

ttk.Button(window, text="Encrypt", command=encrypt_message).grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
ttk.Button(window, text="Decrypt", command=decrypt_message).grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

ttk.Label(window, text="Output Pesan:").grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)
output_text = tk.Text(window, height=6, width=50)
output_text.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

ttk.Button(window, text="Buka File", command=open_file).grid(row=10, column=0, padx=10, pady=5, sticky=tk.W)
ttk.Button(window, text="Simpan File", command=lambda: save_file(output_text.get("1.0", tk.END))).grid(row=10, column=1, padx=10, pady=5, sticky=tk.W)

window.mainloop()
