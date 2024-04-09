# Analiza Składowych Głównych (PCA)

PCA jest techniką statystyczną wykorzystywaną do redukcji wymiarów poprzez przekształcenie danych do nowego układu współrzędnych, gdzie największa wariancja znajduje się na pierwszej współrzędnej (pierwsza składowa główna), a każda kolejna składowa ma możliwie największą wariancję pod warunkiem, że jest ortogonalna do poprzednich.

## Kroki algorytmu PCA:

1. **Standaryzacja danych**
   Dane wejściowe należy najpierw znormalizować, tak aby każda cecha miała średnią równą 0 i wariancję równą 1.

2. **Obliczenie macierzy kowariancji**
   Na podstawie znormalizowanych danych oblicza się macierz kowariancji, która pokazuje, jak zmieniają się cechy względem siebie.

3. **Wyznaczenie wartości własnych i wektorów własnych macierzy kowariancji**
   Z macierzy kowariancji wyznacza się wartości własne i odpowiadające im wektory własne. Wartości własne reprezentują wariancję, którą można przypisać odpowiadającym im wektorom własnym.

4. **Sortowanie wartości własnych i odpowiadających im wektorów własnych**
   Wartości własne sortuje się od największej do najmniejszej, aby określić, które wektory własne mają największy wpływ na wariancję danych.

5. **Wybór k składowych głównych**
   Wybiera się `k` największych wartości własnych i odpowiadających im wektorów własnych, gdzie `k` jest liczbą wymiarów, do których chcemy zredukować nasze dane.

6. **Transformacja danych do nowej przestrzeni**
   Oryginalne dane są transformowane do nowej przestrzeni za pomocą wybranych wektorów własnych. W ten sposób otrzymujemy zredukowany zestaw danych.

## Przykładowa implementacja w Pythonie:

```python
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Zdefiniowanie przykładowych danych
X = np.array([[1, 2], [3, 4], [5, 6]])

# Standaryzacja danych
X_scaled = StandardScaler().fit_transform(X)

# Inicjalizacja i dopasowanie PCA
pca = PCA(n_components=2)
pca.fit(X_scaled)

# Wyświetlenie składowych głównych i wariancji, którą wyjaśniają
components = pca.components_
explained_variance = pca.explained_variance_

# Transformacja danych do przestrzeni składowych głównych
X_pca = pca.transform(X_scaled)
