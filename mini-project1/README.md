# Mini-Project 1: Basic Image Manipulation

This project serves as an introduction to fundamental image processing concepts through pixel-level manipulation. The scripts use a custom `SimpleImage` library to abstract away some of the complexities of image handling, allowing a focus on the core algorithms.

## Scripts

### [`imageexamples.py`](./imageexamples.py)
This script is a collection of functions that perform basic, full-image transformations. It includes implementations for:
- **Grayscale Conversion**: Converts a color image to grayscale by averaging the R, G, and B values.
- **Darkening**: Reduces the brightness of an image by halving the value of each color channel for every pixel.
- **Red Channel Isolation**: Filters out the green and blue channels, leaving only the red component of the image.
- **Conditional Formatting**: Applies an effect (darkening) to only the right half of the image.

### [`greenscreen.py`](./greenscreen.py)
This script implements a chroma key effect, commonly known as "greenscreen" or in this case, "redscreen". It demonstrates how to:
- Iterate through each pixel of a "main" image.
- Check if a pixel's red component is significantly higher than the pixel's average brightness.
- If it is, replace that pixel with the corresponding pixel from a separate "background" image.

The main function provides an example where the red parts of a stop sign are replaced with an image of leaves.
