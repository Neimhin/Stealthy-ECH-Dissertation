
import numpy as np
import matplotlib.pyplot as plt
from cryptography.hazmat.primitives.asymmetric import x25519

def generate_public_keys(num_keys):
    public_keys = np.zeros(num_keys, dtype=np.uint64)
    
    for i in range(num_keys):
        # Generate a new private key
        private_key = x25519.X25519PrivateKey.generate()
        # Obtain the public key
        public_key = private_key.public_key()
        # Convert public key to bytes
        public_key_bytes = public_key.public_bytes(
            encoding=None,  # No encoding option is necessary
            format=x25519.PublicFormat.Raw  # Use Raw format
        )
        
        # Convert the bytes to an integer
        public_key_int = int.from_bytes(public_key_bytes, byteorder='little')
        # Store the integer value (taking the lower 64 bits for visualization)
        public_keys[i] = public_key_int & 0xFFFFFFFFFFFFFFFF  # Mask to 64 bits
    
    return public_keys

def plot_histogram(public_keys):
    plt.figure(figsize=(12, 6))
    plt.hist(public_keys, bins=100, range=(0, 2**64), color='blue', edgecolor='black')
    plt.title('Histogram of Curve25519 Public Key Values')
    plt.xlabel('Public Key Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    num_keys = 1000000
    public_keys = generate_public_keys(num_keys)
    plot_histogram(public_keys)
