import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import numpy as np
from cipher import caesar_cipher_encrypt

def read_preprocessed_data(preprocessed_file, max_length=1000000):
    with open(preprocessed_file, 'r', encoding='utf-8') as f:
        text_data = f.read(max_length)
    return text_data

def generate_sample_data(text, ciphers, num_samples=1000):
    X, y = [], []
    cipher_count = len(ciphers)
    for i in range(num_samples):
        idx = np.random.randint(cipher_count)
        cipher_func, shift = ciphers[idx]
        encrypted_text = [ord(c) for c in cipher_func(text, shift)]
        X.append(encrypted_text[:100])  # Use the first 100 characters for training
        y.append(shift - 1)  # Adjust label to be in range [0, 24]
    return np.array(X), np.array(y)

# Paths
preprocessed_file = "/Users/raunakraj/Documents/rapid_decrypt/preprocessed_gutenberg.txt"

# Read preprocessed data
text_data = read_preprocessed_data(preprocessed_file)

# Define your ciphers and their corresponding labels
ciphers = [(caesar_cipher_encrypt, shift) for shift in range(1, 26)]  # Example: Caesar ciphers with shifts 1 to 25

# Generate sample data
X_train, y_train = generate_sample_data(text_data, ciphers)
X_test, y_test = generate_sample_data(text_data, ciphers)

# Define the model
model = Sequential([
    Flatten(input_shape=(100,)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(len(ciphers), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save the model
model.save('cipher_identifier_model.h5')