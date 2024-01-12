import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk melakukan deteksi tepi pada gambar
def edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

# Fungsi untuk melakukan segmentasi pada gambar
def remove_background(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])  # Nilai batas rendah untuk warna merah dalam format HSV
    upper_red1 = np.array([10, 255, 255])  # Nilai batas tinggi untuk warna merah dalam format HSV
    lower_red2 = np.array([160, 100, 100])  # Nilai batas rendah alternatif untuk warna merah dalam format HSV
    upper_red2 = np.array([179, 255, 255])  # Nilai batas tinggi alternatif untuk warna merah dalam format HSV
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

# Baca gambar 
original = cv2.imread('Tambahan/baskom.jpg')

# Deteksi tepi pada gambar
edges = edge_detection(original)

# Hapus background pada gambar dengan segmentasi warna merah
segmented = remove_background(original)

# untuk menampilkan ketiga gambar dalam satu jendela
plt.figure(figsize=(10, 5))

# Gambar original
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title('Gambar Original')
plt.axis('off')

# Gambar dengan deteksi tepi
plt.subplot(1, 3, 2)
plt.imshow(edges)
plt.title('Deteksi Tepi Gambar')
plt.axis('off')

# Gambar dengan segmentasi 
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB))
plt.title('Hasil Segmentasi')
plt.axis('off')

# Tampilkan jendela
plt.show()