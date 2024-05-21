# Strategia One-vs-One (OvO)

Strategia **One-vs-One (OvO)** to technika stosowana w klasyfikacji wieloklasowej, gdzie problem klasyfikacji z wieloma klasami (więcej niż dwie klasy) jest rozbijany na kilka problemów binarnych, z jednym problemem binarnym dla każdej pary klas.

## Jak działa strategia One-vs-One (OvO)


1. **Rozbicie problemu:** Dla każdej pary klas w zbiorze danych trenujemy osobny klasyfikator binarny. Jeśli mamy \( K \) klas, to potrzebujemy 
$$ 
\frac{K(K-1)}{2}\ 
$$ klasyfikatorów.

2. **Trening:** Trenujemy jeden model binarny dla każdej pary klas. Dla klas \(i\) i \(j\), model jest trenowany tylko na próbkach należących do tych dwóch klas. Etykieta będzie \(1\) dla próbek należących do klasy \(i\) i \(0\) dla próbek należących do klasy \(j\).

3. **Predykcja:** Podczas klasyfikacji nowych próbek, każdy z trenowanych modeli binarnych dokonuje predykcji. Klasa, która otrzymuje najwięcej "głosów" (predykcji) od wszystkich modeli, jest wybierana jako ostateczna klasa dla danej próbki.

## Przykład

Załóżmy, że mamy problem klasyfikacji z trzema klasami: A, B, C.

1. **Model A vs B:**
   - Trenujemy model na próbkach z klasy A i B.

2. **Model A vs C:**
   - Trenujemy model na próbkach z klasy A i C.

3. **Model B vs C:**
   - Trenujemy model na próbkach z klasy B i C.

Podczas klasyfikacji nowej próbki, każdy z trzech modeli (A vs B, A vs C, B vs C) dokonuje predykcji. Przykład może wyglądać tak:

- **Model A vs B:** Przewiduje klasę A
- **Model A vs C:** Przewiduje klasę A
- **Model B vs C:** Przewiduje klasę C

Klasa A otrzymuje dwa głosy, a klasa C jeden głos. Dlatego nowa próbka zostaje zaklasyfikowana jako klasa A.

## Kiedy używać strategii One-vs-One

- **Modele binarne:** Strategia OvO jest szczególnie użyteczna, gdy mamy algorytmy dobrze radzące sobie z klasyfikacją binarną.
- **Duża liczba klas:** Może być bardziej efektywna niż OvA w przypadku, gdy mamy dużą liczbę klas, ponieważ każdy klasyfikator widzi tylko podzbiór danych.
- **Dobre wsparcie przez biblioteki:** Wiele bibliotek, takich jak scikit-learn, wspiera OvO i może automatycznie rozbijać problem wieloklasowy na pary binarne.

## Zalety i wady

**Zalety:**
- Dobre wyniki w przypadku zbalansowanych zbiorów danych.
- Każdy model binarny jest trenowany na mniejszym podzbiorze danych, co może przyspieszyć trening.

**Wady:**
- Wymaga trenowania dużej liczby modeli
$$
\frac{K(K-1)}{2}\
$$
modeli dla \(K\) klas, co może być czasochłonne i wymagać dużo zasobów.
- Może prowadzić do problemów z niezbalansowanymi danymi, gdy jedna klasa jest znacznie mniej liczna niż inne.

## Przykład implementacji w Pythonie

Poniżej znajduje się prosty przykład użycia strategii One-vs-One z wykorzystaniem regresji logistycznej na zbiorze danych Iris:

```python
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsOneClassifier

# Wczytanie zbioru danych Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Stworzenie i trenowanie modelu One-vs-One przy użyciu regresji logistycznej
ovo_clf = OneVsOneClassifier(LogisticRegression(max_iter=200))
ovo_clf.fit(X_train, y_train)

# Predykcja na zbiorze testowym
y_pred = ovo_clf.predict(X_test)

# Ocena dokładności
accuracy = accuracy_score(y_test, y_pred)
print(f'Dokładność: {accuracy}')
