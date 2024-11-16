# Noktalar listesi
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Euclidean Distance fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Mesafeleri hesaplama ve saklama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonuçları yazdırma
print("Noktalar arasındaki mesafeler:", distances)
print("Minimum mesafe:", min_distance)