import tkinter as tk
from tkinter import ttk
import numpy as np
import tensorflow as tf
from cipher import preprocess_text

# Load the trained model
model = tf.keras.models.load_model('cipher_identifier_model.h5')

# List of cipher names corresponding to the model's output
cipher_names = [
    'Caesar Shift 1', 'Caesar Shift 2', 'Caesar Shift 3', 'Caesar Shift 4', 
    'Caesar Shift 5', 'Caesar Shift 6', 'Caesar Shift 7', 'Caesar Shift 8', 
    'Caesar Shift 9', 'Caesar Shift 10', 'Caesar Shift 11', 'Caesar Shift 12', 
    'Caesar Shift 13', 'Caesar Shift 14', 'Caesar Shift 15', 'Caesar Shift 16', 
    'Caesar Shift 17', 'Caesar Shift 18', 'Caesar Shift 19', 'Caesar Shift 20', 
    'Caesar Shift 21', 'Caesar Shift 22', 'Caesar Shift 23', 'Caesar Shift 24', 
    'Caesar Shift 25'
]

def identify_cipher():
    ciphertext = entry.get()
    processed_ciphertext = preprocess_text(ciphertext)
    # Ensure the processed text has exactly 100 characters
    if len(processed_ciphertext) > 100:
        processed_ciphertext = processed_ciphertext[:100]
    elif len(processed_ciphertext) < 100:
        processed_ciphertext = processed_ciphertext.ljust(100, ' ')
    
    encrypted_text = np.array([list(map(ord, processed_ciphertext))])
    prediction = model.predict(encrypted_text)[0]
    
    # Clear the previous results
    for item in tree.get_children():
        tree.delete(item)
    
    # Insert new results
    for i, (cipher_name, probability) in enumerate(zip(cipher_names, prediction)):
        tree.insert("", "end", values=(cipher_name, f"{probability * 100:.2f}%"))

root = tk.Tk()
root.title("Cipher Identifier")

label = tk.Label(root, text="Enter Ciphertext (alphabetical characters):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Identify Cipher", command=identify_cipher)
button.pack()

columns = ('Cipher', 'Probability')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('Cipher', text='Cipher')
tree.heading('Probability', text='Probability')
tree.pack()

root.mainloop()