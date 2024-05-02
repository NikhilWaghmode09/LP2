def encrypt(message, key):
    # Create a list to hold the encrypted text
    encrypted_text = [''] * key

    # Loop through each column in the transposition grid
    for col in range(key):
        pointer = col

        # Keep adding characters to the encrypted_text list until we reach the end of the message
        while pointer < len(message):
            encrypted_text[col] += message[pointer]
            pointer += key

    # Concatenate the encrypted_text list to form the encrypted message
    return ''.join(encrypted_text)

def decrypt(ciphertext, key):
    # Calculate the number of columns in the transposition grid
    num_cols = len(ciphertext) // key

    # Calculate the number of rows in the transposition grid
    num_rows = key

    # Calculate the number of "extra" characters at the end of the message
    num_extra_chars = len(ciphertext) % key

    # Initialize a list to hold the decrypted text
    decrypted_text = [''] * num_cols

    col = 0
    row = 0
    for symbol in ciphertext:
        # Add the symbol to the current column in the transposition grid
        decrypted_text[col] += symbol

        # Move to the next column
        col += 1

        # If we've reached the end of a row or there are no more characters left
        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_extra_chars):
            col = 0
            row += 1

    # Concatenate the decrypted_text list to form the decrypted message
    return ''.join(decrypted_text)

# Example usage
message = "helloworld"
key = 2

# Encrypt the message
encrypted_message = encrypt(message, key)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)