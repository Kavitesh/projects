import pandas as pd
import numpy as np
import tenseal as ts
import logging

def main():    
    # Generate synthetic data
    np.random.seed(42)
    n_samples = 100

    data = pd.DataFrame({
        "Longitude": np.random.randint(-180, 180, n_samples),
        "Latitude": np.random.randint(-90, 90, n_samples)
    })

    # Compute Zone_Threat_Level
    def compute_zone_threat(lon, lat):
        if lon * lat < 0:
            return np.random.randint(80, 100)
        else:
            return np.random.randint(0, 60)

    data["Zone_Threat_Level"] = [compute_zone_threat(lon, lat) for lon, lat in zip(data["Longitude"], data["Latitude"])]

    # Generate feature data
    data["Human_Density"] = np.random.randint(0, 100, n_samples)
    data["Young_Male_Density"] = np.random.randint(0, 100, n_samples)
    data["Suspicious_People_Density"] = np.random.randint(0, 100, n_samples)
    data["Minor_Density"] = np.random.randint(0, 100, n_samples)
    data["Heavy_Vehicle_Percentage"] = np.random.randint(0, 100, n_samples)

    # Define coefficients
    w0 = -10
    w1, w2, w3, w4, w5, w6 = 0.3, 0.1, 0.3, 0.5, -0.5, 0.4

    data["Threat_Level"] = np.clip(
        w0 +
        w1 * data["Zone_Threat_Level"] +
        w2 * data["Human_Density"] +
        w3 * data["Young_Male_Density"] +
        w4 * data["Suspicious_People_Density"] +
        w5 * data["Minor_Density"] +
        w6 * data["Heavy_Vehicle_Percentage"] +
        np.random.randint(0, 11, n_samples), 
        0, 100  
    ).astype(int)  

    # Load public key for encryption
    with open("public_key.tenseal", "rb") as f:
        public_context = ts.context_from(f.read())

    # Encryption function
    def encrypt_number(num):
        return ts.ckks_vector(public_context, [num]).serialize().hex()

    # Encrypt test data
    test_data_encrypted = data.map(encrypt_number)
    test_data_encrypted.to_csv("enc_data.csv", index=False)


    # Load private key for decryption
    with open("private_key.tenseal", "rb") as f:
        private_context = ts.context_from(f.read())

    # Decryption function
    def decrypt_number(encrypted_hex):
        encrypted_vector = ts.ckks_vector_from(private_context, bytes.fromhex(encrypted_hex))
        return encrypted_vector.decrypt()[0]

    # Read and decrypt test data
    test_data_encrypted = pd.read_csv("enc_data.csv")
    test_data_decrypted = test_data_encrypted.map(decrypt_number)
    
    logging.info(test_data_decrypted.head())
    
if __name__ == "__main__":
    main()
