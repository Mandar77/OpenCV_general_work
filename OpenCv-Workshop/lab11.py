import os
import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# Create a directory to save results
output_dir = "lab11_results"
os.makedirs(output_dir, exist_ok=True)

# Read and preprocess the image
image = cv2.imread('xiao.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("Image 'xiao.jpg' not found.")

# Generate Gaussian noise
noise = np.random.normal(0, 25, image.shape).astype('uint8')

# Create an adversarial image by blending the original image with noise
adv_image = cv2.addWeighted(image, 0.9, noise, 0.1, 0)
adv_image_path = os.path.join(output_dir, "Adversarial_image.jpg")
cv2.imwrite(adv_image_path, adv_image)

# --- GAN Definitions ---
latent_dim = 100  # Dimension of noise vector

# Generator Model
generator = nn.Sequential(
    nn.Linear(latent_dim, 128),
    nn.ReLU(),
    nn.Linear(128, 256),
    nn.ReLU(),
    nn.Linear(256, 28 * 28),
    nn.Tanh()
)

# Discriminator Model
discriminator = nn.Sequential(
    nn.Linear(28 * 28, 256),
    nn.LeakyReLU(0.2),
    nn.Linear(256, 128),
    nn.LeakyReLU(0.2),
    nn.Linear(128, 1),
    nn.Sigmoid()
)

# Loss function and optimizers
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002)
optimizer_G = optim.Adam(generator.parameters(), lr=0.0002)

# Placeholder for real and fake data
real_labels = torch.ones((64, 1))  # Batch size of 64
fake_labels = torch.zeros((64, 1))

# Example Training Loop for GAN
for epoch in range(1):  # Replace with desired number of epochs
    # Generate random noise and fake images
    noise = torch.randn(64, latent_dim)  # Batch size of 64
    fake_imgs = generator(noise)

    # Real images (placeholder)
    real_imgs = torch.randn(64, 28 * 28)  # Replace with real training images

    # Train Discriminator
    optimizer_D.zero_grad()
    real_loss = criterion(discriminator(real_imgs), real_labels)
    fake_loss = criterion(discriminator(fake_imgs.detach()), fake_labels)
    d_loss = real_loss + fake_loss
    d_loss.backward()
    optimizer_D.step()

    # Train Generator
    optimizer_G.zero_grad()
    fake_preds = discriminator(fake_imgs)
    g_loss = criterion(fake_preds, real_labels)  # Generator tries to fool Discriminator
    g_loss.backward()
    optimizer_G.step()

# --- Image Noise Addition and Denoising ---

# Resize image to 128x128 and normalize to range [0, 1]
image = cv2.resize(image, (128, 128)) / 255.0

# Add Gaussian noise in multiple steps and save results
for i in range(5):
    noise = np.random.normal(0, 0.1 * (i + 1), image.shape)
    noisy_image = np.clip(image + noise, 0, 1)
    noisy_image_path = os.path.join(output_dir, f"Noisy_image_step_{i+1}.jpg")
    cv2.imwrite(noisy_image_path, (noisy_image * 255).astype('uint8'))

# Apply GaussianBlur for denoising and save the result
denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)
denoised_image_path = os.path.join(output_dir, "Denoised_image.jpg")
cv2.imwrite(denoised_image_path, (denoised_image * 255).astype('uint8'))

print(f"All result images have been saved to the '{output_dir}' directory.")
