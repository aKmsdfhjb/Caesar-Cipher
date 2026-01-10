# Caesar Cipher (Python)

A simple Python implementation of the **Caesar Cipher**, one of the oldest and simplest forms of encryption. This project allows users to take a string and shift its characters by a specified amount to encode or decode messages.



## 🚀 Features
* **Encryption:** Convert plain text into ciphertext using a numerical shift.
* **Decryption:** Reverse the process to reveal the original message.
* **Special Character Handling:** Maintains spaces and punctuation while only shifting alphabetic characters.
* **Customizable Shifts:** Supports any integer shift (e.g., ROT13).

## 🛠️ How it Works
The Caesar Cipher works by "shifting" each letter in the alphabet by a fixed number of positions. For example, with a shift of **3**:
* `A` becomes `D`
* `B` becomes `E`
* `C` becomes `F`

In this project, the `encrypt` and `decrypt` functions use Python's index-based list manipulation to handle these shifts efficiently.

## 💻 Usage
To run the cipher, simply call the functions within `main.py`:

```python
text = "Hello World"
shift = 13

# Encrypting
secret = encrypt(text, shift)
print(secret) # "Uryyb Jbeyq"

# Decrypting
original = decrypt(secret, shift)
print(original) # "Hello World"
