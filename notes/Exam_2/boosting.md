# AdaBoost

AdaBoost (Adaptive Boosting) jest algorytmem uczenia zespołowego, który łączy wiele słabych klasyfikatorów w celu stworzenia silnego klasyfikatora. Kluczowym elementem AdaBoost jest przypisywanie wag do każdej instancji w zbiorze danych, które są aktualizowane na podstawie błędów popełnionych przez poprzednie klasyfikatory.

## Jak działa AdaBoost?

1. **Inicjalizacja wag**:
   - Na początku wagi dla każdej instancji są ustawione na $ \frac{1}{m} $, gdzie \( m \) to liczba instancji w zbiorze danych.

2. **Trenowanie słabego klasyfikatora**:
   - Trenujemy pierwszy słaby klasyfikator na zbiorze treningowym z aktualnymi wagami.

3. **Obliczenie współczynnika błędu**:
   - Obliczamy ważony współczynnik błędu $ r_j $ dla klasyfikatora:
    # $ r_j = \frac{\sum_{i=1}^m w^{(i)} \cdot I(y^{(i)} \neq \hat{y}^{(i)}_j)}{\sum_{i=1}^m w^{(i)}} $
     # gdzie $ \hat{y}^{(i)}_j $ to predykcja j-tego klasyfikatora dla i-tego przykładu, a $ I $ to funkcja wskaźnikowa.

4. **Obliczenie wagi klasyfikatora**:
   - Obliczamy wagę klasyfikatora $ \alpha_j $:
    $
     \alpha_j = \eta \cdot \log \left( \frac{1 - r_j}{r_j} \right)
     $
     gdzie \( \eta \) to współczynnik uczenia się.

5. **Aktualizacja wag instancji**:
   - Aktualizujemy wagi instancji:
     \[
     w^{(i)} = w^{(i)} \cdot \exp(\alpha_j) \quad \text{jeśli } y^{(i)} \neq \hat{y}^{(i)}_j
     \]
     a następnie normalizujemy wagi, aby ich suma była równa 1.

6. **Powtórzenie procesu**:
   - Trenujemy nowy klasyfikator na zaktualizowanych wagach i powtarzamy kroki 3-5 aż do osiągnięcia określonej liczby klasyfikatorów lub znalezienia idealnego klasyfikatora.

7. **Predykcja końcowa**:
   - Aby przewidzieć etykietę, AdaBoost oblicza przewidywania wszystkich klasyfikatorów i waży je za pomocą \( \alpha_j \). Przewidywana klasa to ta, która otrzymuje większość głosów ważonych.

## Przykład w Pythonie z użyciem Scikit-Learn

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Załadowanie danych
iris = load_iris()
X, y = iris.data, iris.target

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definicja słabego uczącego (decision stump)
weak_learner = DecisionTreeClassifier(max_depth=1)

# Trening modelu AdaBoost z użyciem słabego uczącego
clf = AdaBoostClassifier(base_estimator=weak_learner, n_estimators=50, random_state=42)
clf.fit(X_train, y_train)

# Predykcja i ocena
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


# Gradient Boosting

Gradient Boosting to popularna technika boostingu, która działa poprzez sekwencyjne dodawanie predyktorów do komitetu, z których każdy koryguje błędy swojego poprzednika. Zamiast modyfikować wagi punktów jak w AdaBoost, Gradient Boosting próbuje dopasować nowy predyktor do błędu (residuum) poprzedniego predyktora.

## Jak działa Gradient Boosting?

1. **Inicjalizacja**:
   - Algorytm rozpoczyna od początkowego modelu (np. model stałej przewidujący średnią wartość y w przypadku regresji).

2. **Iteracyjny proces trenowania**:
   - W każdej iteracji obliczane są reszty (różnice między rzeczywistymi wartościami a przewidywanymi).
   - Nowy model jest trenowany na resztach, aby zminimalizować błąd predykcji.
   - Wyniki nowego modelu są dodawane do skumulowanego modelu w celu poprawy predykcji.

3. **Aktualizacja modelu**:
   - Skumulowany model jest aktualizowany poprzez dodanie nowych prognoz pomnożonych przez współczynnik uczenia się \( \eta \).

4. **Kontynuacja iteracji**:
   - Proces jest powtarzany przez określoną liczbę iteracji lub do momentu, gdy dalsze poprawki są niewielkie.
```
## Przykład w Pythonie z użyciem Scikit-Learn

```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Załadowanie danych
iris = load_iris()
X, y = iris.data, iris.target

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trening modelu Gradient Boosting
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Predykcja i ocena
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```