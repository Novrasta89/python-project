import math

# 2D uzaydaki noktaları temsil eden bir liste
points = [(1, 2), (4, 6), (5, 1), (7, 9)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])*2 + (point2[1] - point1[1])*2)

# Mesafeleri saklayacak liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesapla ve distances listesine ekle
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# distances listesindeki minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance}")
