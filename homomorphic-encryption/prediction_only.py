import seaborn as sns
import pandas as pd
import numpy as np
import json
import tenseal as ts
import matplotlib.pyplot as plt
# Encryption Keys
PRIVATE_KEY = r"public_key.tenseal"
ENCRYPTED_DATA = r"enc_data.csv"
MODEL =r"encrypted_model.json"

# Load private key for decryption
with open(PRIVATE_KEY, "rb") as f:
    private_context = ts.context_from(f.read())

# Vector generation
def vector_from(encrypted_hex):
    return ts.ckks_vector_from(private_context, bytes.fromhex(encrypted_hex))

def encrypt_numbers(nums):
    return [ts.ckks_vector(private_context, [num]) for num in nums]

# Decryption function
def decrypt_number(encrypted_hex):
    return vector_from(encrypted_hex).decrypt()[0]

# Load encrypted data
with open(MODEL, "r") as f:
    encrypted_training_result = json.load(f)

# Load test data
test_data_encrypted = pd.read_csv(ENCRYPTED_DATA)
X = test_data_encrypted.drop(columns=["Threat_Level"])
y = test_data_encrypted["Threat_Level"]

# ======== LINEAR REGRESSION PREDICTION ========
lin_reg_coef_enc = [vector_from(coef) for coef in encrypted_training_result["lin_reg_coef"]]
lin_reg_intercept_enc = vector_from(encrypted_training_result["lin_reg_intercept"])
encrypted_predictions = []
for _, row in X.iterrows():
    encrypted_row = [vector_from(cell) for cell in row]
    encrypted_pred = sum(coef * cell for coef, cell in zip(lin_reg_coef_enc, encrypted_row)) + lin_reg_intercept_enc
    encrypted_predictions.append(encrypted_pred.serialize().hex())

# Decrypt predictions
lin_decrypted_predictions = np.array([decrypt_number(pred) for pred in encrypted_predictions])
lin_decrypted_act = np.array([decrypt_number(act) for act in y])

# ======== LOGISTIC REGRESSION PREDICTION ========
# Convert stored encrypted logistic regression coefficients and intercept
log_reg_coef_enc = [vector_from(coef) for coef in encrypted_training_result["log_reg_coef"]]
log_reg_intercept_enc = vector_from(encrypted_training_result["log_reg_intercept"])

# Perform encrypted dot product for logistic regression
encrypted_logit = []
for _, row in X.iterrows():
    encrypted_row = [vector_from(cell) for cell in row]
    encrypted_dot_product = sum(coef * cell for coef, cell in zip(log_reg_coef_enc, encrypted_row)) + log_reg_intercept_enc
    encrypted_logit.append(encrypted_dot_product.serialize().hex())

# Decrypt logit values
decrypted_logit = np.array([decrypt_number(logit) for logit in encrypted_logit])

# Apply sigmoid function: sigmoid(x) = 1 / (1 + exp(-x))
y_pred_logistic = 1 / (1 + np.exp(-decrypted_logit))

# Convert probabilities to binary classification (0 or 1)
log_decrypted_predictions = (y_pred_logistic > 0.5).astype(int)
log_decrypted_longitude = np.array([decrypt_number(act) for act in X["Longitude"]])
log_decrypted_latitude = np.array([decrypt_number(act) for act in X["Latitude"]])

# Function to generate all plots
def generate_plots():
    fig, ax = plt.subplots(figsize=(8, 6))

    fig, axes = plt.subplots(1, 2, figsize=(15, 8))

    # Linear Regression Plot
    axes[ 0].scatter(lin_decrypted_act, lin_decrypted_predictions, color='blue', alpha=0.6, label='Predicted vs Actual')
    axes[0].plot([lin_decrypted_act.min(), lin_decrypted_act.max()], [lin_decrypted_act.min(), lin_decrypted_act.max()], 'r--', lw=2)
    axes[0].set_xlabel("Actual Threat Level")
    axes[0].set_ylabel("Predicted Threat Level")
    axes[0].set_title("Linear Regression Results")
    axes[0].legend()

    # # Logistic Regression Scatter Plot
    # bg_img = plt.imread("map_rect.png") 
    # axes[1].imshow(bg_img, extent=[min(log_decrypted_longitude), max(log_decrypted_longitude), 
    #                       min(log_decrypted_latitude), max(log_decrypted_latitude)], aspect='auto')

    axes[1].scatter(log_decrypted_longitude, log_decrypted_latitude, 
                        c=log_decrypted_predictions, cmap='coolwarm', alpha=0.6)
    axes[1].set_xlabel("Longitude")
    axes[1].set_ylabel("Latitude")
    axes[1].set_title("Logistic Regression Scatter Plot")
    fig.colorbar(plt.cm.ScalarMappable(cmap="coolwarm"), ax=axes[1], label="Predicted Threat Level (Binary)")


    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    generate_plots()
