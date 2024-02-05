import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('leo.jpg')

# Specify the desired width
desired_width = 400

# Calculate the aspect ratio
height, width = image.shape[:2]
aspect_ratio = width / height

# Calculate the new height based on the desired width and aspect ratio
desired_height = int(desired_width / aspect_ratio)

# Resize the image
resized_image = cv2.resize(image, (desired_width, desired_height))

gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(gray_image, (7,7),0)
(T, bin) = cv2.threshold(suave, 160,255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160,255, cv2.THRESH_BINARY_INV)

resultado = np.vstack(
    [
        np.hstack([suave, bin]),
        np.hstack([binI, cv2.bitwise_and(gray_image, gray_image, mask=binI)])
                       
                       ])
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# axes[0].imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
# axes[0].set_title('Color Image')
# axes[0].axis('off')

# axes[1].imshow(gray_image, cmap='gray')
# axes[1].set_title('Gray Image')
# axes[1].axis('off')

# axes[2].imshow(resultado, cmap='gray')
# axes[2].set_title('Binary Image')
# axes[2].axis('off')

# plt.tight_layout()
# plt.show()
# Display or save the resized image
cv2.imshow('Resized Image', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()

