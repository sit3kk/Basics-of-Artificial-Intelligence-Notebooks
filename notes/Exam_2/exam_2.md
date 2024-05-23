## Podstawy sztucznej inteligencji - egzamin

### 1. Podaj ogólny wzór na logarytmiczną funkcję wiarygodności:
## $ l(w) = \sum_{i=1}^{n} \left( y_i \log(p(y_i|x_i; w)) + (1 - y_i) \log(1 - p(y_i|x_i; w)) \right) $

### 2. Metoda największego spadku jest iteracyjnym algorytmem wyszukiwania minimum zadanej funkcji celu. Na samym początku algorytmu wybieramy jest punkt startowy x0. Następne punkty xk obliczane według wzoru:
# $ x_{k+1} = x_k - \eta \nabla f(x_k) $

### 3. Wymień trzy algorytmy wykonujące regresję liniową:
1. Regresja liniowa zwykła (OLS)
2. Regresja grzbietowa (Ridge Regression)
3. Regresja LASSO

### 4. Podaj wzór na Accuracy (ACC):
# $ ACC = \frac{TP + TN}{TP + TN + FP + FN}  $

### 5. Niech będzie dany zbiór danych $ (X, Y) = \{(x_i, y_i)\}_{i=1}^{n} $, gdzie $ y_i \in \{0, 1\} $ (klasyfikacja binarna). Podaj funkcję kosztu modelu regresji logistycznej:
##  $  J(w) = -\frac{1}{m} \sum_{i=1}^{m} \left[ y_i \log(h_w(x_i)) + (1 - y_i) \log(1 - h_w(x_i)) \right] \ $

### 6. Rozważmy problem klasyfikacji binarnej. Podaj definicje pojęć:
1. **True negatives**: Liczba przypadków, gdzie model poprawnie przewidział klasę negatywną.
2. **False positives**: Liczba przypadków, gdzie model błędnie przewidział klasę pozytywną.
3. **False negatives**: Liczba przypadków, gdzie model błędnie przewidział klasę negatywną.
4. **True positives**: Liczba przypadków, gdzie model poprawnie przewidział klasę pozytywną.

### 7. Precision wyraża się wzorem:
# $ \text{Precision} = \frac{TP}{TP + FP} $

### 8. Recall wyraża się wzorem:
# $ \text{Recall} = \frac{TP}{TP + FN} $

### 9. F1 score jest średnią:
# $ F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} $

### 10. Czym różni się randomized search od grid search:
- **Randomized Search**: Przeszukuje losowe kombinacje hiperparametrów.
- **Grid Search**: Przeszukuje wszystkie możliwe kombinacje hiperparametrów w ustalonym zakresie.

### 11. Wymień 3 algorytmy uczenia maszynowego będące komitetami klasyfikatorów:
1. Random Forest
2. Gradient Boosting
3. AdaBoost

### 12. Czym różni się bagging od pasting:
- **Bagging**: Losowanie próbek z powtórzeniami do treningu modeli.
- **Pasting**: Losowanie próbek bez powtórzeń do treningu modeli.

### 13. Podaj wzór na Softmax:
# $ \text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}} $

## Podstawy sztucznej inteligencji - egzamin

### 14. Czym różni się soft voting od hard voting:
- **Soft Voting**: Agreguje prognozy wszystkich klasyfikatorów, uwzględniając prawdopodobieństwa klas.
- **Hard Voting**: Agreguje prognozy wszystkich klasyfikatorów na podstawie większości głosów (klasy).

### 15. Zdefiniuj ROC curves:
- **ROC Curve (Receiver Operating Characteristic Curve)**: Wykres ilustrujący wydajność modelu klasyfikacyjnego, przedstawiający zależność między True Positive Rate (TPR) a False Positive Rate (FPR) przy różnych progach decyzyjnych.

### 16. Podaj wzór na jądro RBF z parametrem γ:
# $ K(x, x') = \exp(-\gamma \| x - x' \|^2) $

### 17. Co to jest kernel trick:
- **Kernel Trick**: Technika umożliwiająca zastosowanie algorytmów liniowych do danych nieliniowych przez przekształcenie danych do przestrzeni o wyższej wymiarowości za pomocą funkcji jądrowych, bez konieczności jawnego obliczania współrzędnych w tej przestrzeni.

### 18. Przy oznaczeniach z wykładu, funkcję kosztu SVM (liniowego) o twardym marginesie możemy wyrazić jako problem optymalizacyjny:
# $ \min \frac{1}{2} \| w \|^2 $
subject to
# $ y^{(i)} (w^T x^{(i)} + b) \geq 1 $

### 19. Czym różni się Group K-Fold od klasycznego K-Fold:
- **Group K-Fold**: Zapewnia, że dane z tych samych grup nie pojawią się jednocześnie w zestawie treningowym i testowym.
- **Klassyczny K-Fold**: Losowo dzieli dane na K części, bez uwzględniania grup.

### 20. Czym różni się Stratified K-Fold od klasycznego K-Fold:
- **Stratified K-Fold**: Zachowuje proporcje klas w każdej z K części, co zapewnia bardziej reprezentatywne podziały.
- **Klassyczny K-Fold**: Dzieli dane losowo, co może prowadzić do nierównomiernego rozkładu klas w różnych częściach.
