# StandardScaler

`StandardScaler` to klasa z biblioteki scikit-learn, która jest używana do standaryzacji cech w zestawie danych. Standaryzacja oznacza, że cechy będą miały średnią równą 0 i odchylenie standardowe równe 1.

## Dlaczego warto używać StandardScaler?

Wiele algorytmów uczenia maszynowego działa lepiej, gdy dane wejściowe mają podobną skalę. Na przykład, w algorytmach takich jak Support Vector Machines (SVM) lub k-Nearest Neighbors (k-NN), różne skale cech mogą prowadzić do nieprawidłowych wyników. Standaryzacja danych pomaga poprawić stabilność i wydajność modeli.

## Jak działa StandardScaler?

StandardScaler działa poprzez obliczanie średniej i odchylenia standardowego dla każdej cechy w zestawie treningowym, a następnie używa tych wartości do transformacji danych:

$$
z = \frac{(x - \mu)}{\sigma}
$$

Gdzie:
- \( x \) to oryginalna wartość cechy,
- \( \mu \) to średnia cechy w zestawie treningowym,
- \( \sigma \) to odchylenie standardowe cechy w zestawie treningowym,
- \( z \) to zstandaryzowana wartość cechy.

## Przykład użycia StandardScaler w Pythonie

Poniżej znajduje się przykładowy kod pokazujący, jak używać StandardScaler do standaryzacji danych:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd

# Wczytaj dane
iris = load_iris()
X = iris.data
y = iris.target

# Przed standaryzacją
print("Przed standaryzacją:")
print(pd.DataFrame(X).describe())

# Inicjalizacja StandardScaler
scaler = StandardScaler()

# Dopasowanie i transformacja danych treningowych
X_scaled = scaler.fit_transform(X)

# Po standaryzacji
print("\nPo standaryzacji:")
print(pd.DataFrame(X_scaled).describe())
