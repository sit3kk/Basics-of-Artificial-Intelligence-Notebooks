# Model Evaluation and Improvement

Cross-validation to statystyczna metoda oceny modelu, która jest bardziej stabilna i dokładna, niż przy użyciu podziału na train/test. Podczas cross-validation dane są wielokrotnie dzielone, a na podziałach uczymy wiele modeli. 

Najczęściej używaną wersją cross-validation jest k-fold cross-validation, gdzie k określa się zwykle 5 lub 10. Podczas wykonywania five-fold cross-validation, dane są najpierw dzielone na pięć części (jeśli się da) równej wielkości, zwanych foldami.

## k-Fold Cross-Validation

1. **Podział danych:** Dane są podzielone na k części, zwanych foldami.
2. **Uczenie modeli:** 
    - Pierwszy model jest uczony przy użyciu pierwszego folda jako zestawu testowego, a pozostałe foldy (2-5) są używane jako zestaw treningowy.
    - Model jest budowany z wykorzystaniem danych w foldach 2-5, a następnie dokładność jest oceniana w foldzie 1.
    - Proces powtarza się, stosując foldy 3, 4 i 5 jako zestawy testowe.
3. **Ocena:** Dla każdego z tych pięciu rozdziałów danych na train/test obliczamy dokładność modelu.

### Przykład w Pythonie

```python
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

# Wczytaj dane
iris = load_iris()
X = iris.data
y = iris.target

# Konfiguracja k-fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=1)

accuracies = []

# Wykonaj k-fold cross-validation
for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Trenuj model
    model = SVC()
    model.fit(X_train, y_train)
    
    # Prognozuj i oceniaj model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Wyświetl dokładności
print(f'K-Fold Cross-Validation Accuracies: {accuracies}')
print(f'Srednia dokladnosc: {np.mean(accuracies)}')
```

## Stratified k-Fold Cross-Validation

Prosta strategia k-Fold Cross-Validation może doprowadzić do podziału, w którym w jednym foldzie znajduje się tylko jedna klasa. Aby temu zapobiec, używa się stratified k-fold cross-validation. W tej metodzie dzielimy dane tak, aby proporcje między klasami były takie same w każdym foldzie, jak w całym zbiorze danych.

### Przykład w Pythonie

```python
from sklearn.model_selection import StratifiedKFold
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

# Wczytaj dane
iris = load_iris()
X = iris.data
y = iris.target

# Konfiguracja stratified k-fold cross-validation
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)

stratified_accuracies = []

# Wykonaj stratified k-fold cross-validation
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Trenuj model
    model = SVC()
    model.fit(X_train, y_train)
    
    # Prognozuj i oceniaj model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    stratified_accuracies.append(accuracy)

# Wyświetl dokładności
print(f'Stratified K-Fold Cross-Validation Accuracies: {stratified_accuracies}')
print(f'Średnia dokładność: {np.mean(stratified_accuracies)}')
```

## Leave-One-Out Cross-Validation (LOOCV)

Inną często używaną metodą sprawdzania poprawności modelu jest metoda Leave-One-Out Cross-Validation (LOOCV). Można myśleć o LOOCV jako o klasycznej metodzie k-Fold Cross-Validation, gdzie każdy fold jest pojedynczą próbką.

### Przykład w Pythonie

```python
from sklearn.model_selection import LeaveOneOut
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

# Wczytaj dane
iris = load_iris()
X = iris.data
y = iris.target

# Konfiguracja leave-one-out cross-validation
loo = LeaveOneOut()

loo_accuracies = []

# Wykonaj leave-one-out cross-validation
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Trenuj model
    model = SVC()
    model.fit(X_train, y_train)
    
    # Prognozuj i oceniaj model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    loo_accuracies.append(accuracy)

# Wyświetl dokładności
print(f'Leave-One-Out Cross-Validation Accuracies: {loo_accuracies}')
print(f'Średnia dokładność: {np.mean(loo_accuracies)}')
```


## Cross-Validation with Groups

Cross-Validation with Groups jest techniką oceny modelu stosowaną w przypadkach, gdy dane mają wewnętrzne zależności grupowe. Zwykłe metody cross-validation mogą nie uwzględniać takich zależności, co prowadzi do nierealistycznych ocen wydajności modelu.

### Opis metody

W cross-validation with groups celem jest zapewnienie, że wszystkie dane z tej samej grupy znajdują się albo w zbiorze treningowym, albo w zbiorze testowym. Jest to szczególnie ważne w przypadkach, gdy dane z jednej grupy są mocno ze sobą skorelowane i nie można ich traktować jako niezależne próbki.

### Przykład

Załóżmy, że chcesz zbudować system rozpoznawania emocji na podstawie zdjęć twarzy. Zbiór danych składa się z zdjęć 100 osób, z których każda osoba jest wielokrotnie użyta, pokazując różne emocje. Celem jest zbudowanie klasyfikatora, który może poprawnie identyfikować emocje osób nie znajdujących się w zbiorze danych treningowych.

### Przykład w Pythonie

```python
from sklearn.model_selection import GroupKFold
from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np

# Tworzenie przykładowych danych
X, y = make_classification(n_samples=100, n_features=20, random_state=1)
groups = np.array([i // 10 for i in range(100)])  # Każda grupa ma 10 próbek

# Konfiguracja GroupKFold cross-validation
gkf = GroupKFold(n_splits=5)

group_accuracies = []

# Wykonaj GroupKFold cross-validation
for train_index, test_index in gkf.split(X, y, groups=groups):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Trenuj model
    model = SVC()
    model.fit(X_train, y_train)
    
    # Prognozuj i oceniaj model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    group_accuracies.append(accuracy)

# Wyświetl dokładności
print(f'GroupKFold Cross-Validation Accuracies: {group_accuracies}')
print(f'Średnia dokładność: {np.mean(group_accuracies)}')
```