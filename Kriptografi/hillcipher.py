import numpy as np

def mod_inv(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % mod) % mod
    return matrix_modulus_inv

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    while len(plaintext) % key_matrix.shape[0] != 0:
        plaintext += "X"
    plaintext_vector = [ord(char) - 65 for char in plaintext]
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, key_matrix.shape[0])
    encrypted_matrix = (np.dot(plaintext_matrix, key_matrix) % 26)
    encrypted_text = ''.join([chr(num + 65) for row in encrypted_matrix for num in row])
    return encrypted_text

def hill_decrypt(ciphertext, key_matrix):
    ciphertext_vector = [ord(char) - 65 for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, key_matrix.shape[0])
    inverse_key_matrix = mod_inv(key_matrix, 26)
    decrypted_matrix = (np.dot(ciphertext_matrix, inverse_key_matrix) % 26)
    decrypted_text = ''.join([chr(num + 65) for row in decrypted_matrix for num in row])
    decrypted_text = decrypted_text.rstrip("X")
    return decrypted_text

key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

plaintext = "HELLO"
ciphertext = hill_encrypt(plaintext, key_matrix)
print(f"Ciphertext: {ciphertext}")

decrypted_text = hill_decrypt(ciphertext, key_matrix)
print(f"Decrypted Text: {decrypted_text}")
