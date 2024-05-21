## Stochastic Gradient Descent (SGD) z Mini-Batches

### Wstęp
**Stochastic Gradient Descent (SGD)** jest techniką optymalizacji wykorzystywaną w uczeniu maszynowym, szczególnie przy dużych zbiorach danych. Działanie algorytmu polega na iteracyjnej aktualizacji parametrów modelu w celu minimalizacji funkcji straty.

### Problem z dużymi zbiorami danych
Obliczenie gradientu funkcji straty na całym zbiorze danych może być nieefektywne lub nawet niewykonalne ze względów obliczeniowych. SGD radzi sobie z tym problemem, korzystając z pojedynczych próbek lub mini-batchy.

### Funkcja kosztu
Załóżmy, że mamy funkcję kosztu `F(θ)` zdefiniowaną jako:

F(θ) = Σ f(θ; x_i)

perl

gdzie `x_i` jest i-tym punktem danych.

### Mini-Batch
Mini-batch jest to mały, losowo wybrany podzbiór danych, który jest używany do obliczenia estymatu gradientu funkcji kosztu. Pozwala to na bardziej stabilne i szybsze oszacowanie gradientu niż w przypadku pojedynczych próbek.

### Epoka
Epoka to jedno pełne przejście przez cały zbiór danych, podczas którego model uczy się na każdym mini-batchu. Typowy trening obejmuje wiele epok, często około 50.

### Raportowanie funkcji straty
Po każdym mini-batchu obliczamy i raportujemy wartość funkcji straty, dzięki czemu możemy śledzić postęp w uczeniu modelu i dostosowywać hiperparametry, takie jak szybkość uczenia się.

## Przykładowe obliczenia SGD

Załóżmy, że mamy prosty model liniowy z parametrami `θ_0` (przesunięcie) i `θ_1` (nachylenie), oraz funkcją straty MSE (Mean Squared Error).

Dla uproszczenia, rozważmy zestaw danych:
- Punkty danych: `x = [1, 2, 3, 4, 5]`
- Odpowiedzi: `y = [1.5, 2.5, 3.5, 4.5, 5.5]`

Startujemy z początkowymi wartościami `θ_0 = 0` i `θ_1 = 1`.

### Krok 1: Obliczenie funkcji straty
Funkcja straty MSE dla naszego modelu liniowego jest dana wzorem:

MSE = 1/N Σ (y_i - (θ_0 + θ_1 x_i))^2

perl

gdzie `N` to liczba punktów danych.

### Krok 2: Obliczenie gradientu funkcji straty
Gradient funkcji straty dla MSE w modelu liniowym to pochodne cząstkowe względem `θ_0` i `θ_1`:

∂MSE/∂θ_0 = -2/N Σ (y_i - (θ_0 + θ_1 x_i))
∂MSE/∂θ_1 = -2/N Σ (y_i - (θ_0 + θ_1 x_i)) x_i

r


### Krok 3: Aktualizacja parametrów
Parametry aktualizujemy, korzystając z gradientu i współczynnika uczenia `η` (learning rate):

θ_0 = θ_0 - η (∂MSE/∂θ_0)
θ_1 = θ_1 - η (∂MSE/∂θ_1)

bash


### Krok 4: Iteracje
Powtarzamy kroki 1-3 dla wielu epok, korzystając z różnych mini-batchy w każdej iteracji, 