def xor_cipher(text: str, key: str) -> str:
    if isinstance(text, str):
        text = text.encode()
    
    if len(key) < len(text):
        key = (key * (len(text) // len(key) + 1))
        key = key[:len(text)]
    
    encrypted_text = bytes([x ^ ord(y) for x, y in zip(text, key)])
    return encrypted_text.decode()

original_text = "Hello, World! How you doing? I hope you are doing well. I am doing good. Thank you for asking. Have a great day ahead. Bye! See you soon."

key = "key" 

encrypted_text = xor_cipher(original_text, key)

print(encrypted_text)

decrypted_text = xor_cipher(encrypted_text, key)
print(decrypted_text)