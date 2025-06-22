import numpy as np

# ==================================================
# STEP 1: LOAD DATA
# ==================================================
data = np.loadtxt("fruit.csv", delimiter=",", skiprows=1)

X = data[:, 0:3]  # Features
y = data[:, 3]    # Labels
n_samples, n_features = X.shape


# ==================================================
# STEP 2: INITIALIZE WEIGHTS & BIAS
# ==================================================
np.random.seed(42)           # Makes results reproducible
weights = np.random.randn(n_features) * 0.01  # Small random numbers
bias = 0.0


# ==================================================
# UTILITY FUNCTIONS
# ==================================================
def sigmoid(z):
    """Activation function for the neuron"""
    return 1 / (1 + np.exp(-z))


def compute_loss(y_true, y_pred):
    """Binary Cross-Entropy loss"""
    epsilon = 1e-15  # Avoid log(0) error
    return -np.mean(y_true * np.log(y_pred + epsilon) + (1 - y_true) * np.log(1 - y_pred + epsilon))


# ==================================================
# STEP 3: TRAIN LOOP
# ==================================================
learning_rate = 0.01
epochs = 500
losses = []
accuracies = []

for epoch in range(1, epochs + 1):

    # Forward Pass
    z = np.dot(X, weights) + bias
    y_pred = sigmoid(z)

    # Compute loss
    loss = compute_loss(y, y_pred)

    # Compute accuracy
    accuracy = np.mean((y_pred >= 0.5) == y)

    losses.append(loss)
    accuracies.append(accuracy)

    # Backward Pass (Gradients)
    error = y_pred - y
    dW = np.dot(X.T, error) / n_samples
    dB = np.sum(error) / n_samples

    # Update Parameters
    weights -= learning_rate * dW
    bias -= learning_rate * dB

    # Optional: Print status every 100 epochs
    if epoch % 100 == 0:
        print(f"Epoch [{epoch}/{epochs}], Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

    # Early stopping if loss is low
    if loss < 0.05:
        print(f"Early stopping at epoch {epoch} as loss dropped below 0.05.")
        break


# ==================================================
# STEP 4: Final Results
# ==================================================
print("\nFinal Weights:", weights)
print("Final Bias:", bias)

# ==================================================
# NEXT STEP: Plot Results
# ==================================================
import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))

# Plot the loss
plt.subplot(1,2,1)
plt.plot(range(1, len(losses)+1), losses, '-o')
plt.title("Loss per Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")

# Plot the accuracy
plt.subplot(1,2,2)
plt.plot(range(1, len(accuracies)+1), accuracies, '-o', color='green')
plt.title("Accuracy per Epoch")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.show()
