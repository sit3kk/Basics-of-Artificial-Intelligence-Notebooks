# Softmax Regression

Model regresji logistycznej można uogólnić tak, aby obsługiwał wiele klas bezpośrednio, bez konieczności uczenia i łączenia wielu klasyfikatorów binarnych. Nazywa się to **Regresją Softmax** lub **Multinomial Logistic Regression**.

## Jak działa Softmax Regression

### Idea

Pomysł jest dość prosty: gdy poda się instancję $ \mathbf{x} $, model regresji Softmax najpierw oblicza wynik $ s_k(\mathbf{x}) $ dla każdej klasy $ k $, a następnie szacuje prawdopodobieństwo każdej klasy przez zastosowanie funkcji softmax (zwanej również znormalizowaną eksponencjalną).

### Obliczanie wyniku

Równanie $ s_k(\mathbf{x}) $ wygląda znajomo, ponieważ jest podobne do równania z regresji logistycznej:

$$
s_k(\mathbf{x}) = \mathbf{\Theta}_k^T \mathbf{x}
$$

Zauważ, że każda klasa ma swój własny wektor parametrów $ \mathbf{\Theta}_k $. Wszystkie te wektory są zwykle przechowywane jako wiersze w macierzy parametrów $ \mathbf{\Theta} $.

### Szacowanie prawdopodobieństw

Po obliczeniu wyniku każdej klasy dla instancji $ \mathbf{x} $, można oszacować prawdopodobieństwo $ \hat{p}_k $, że instancja należy do klasy $ k $ za pomocą funkcji softmax:

$$
\hat{p}_k = \sigma(\mathbf{s}(\mathbf{x}))_k = \frac{\exp(s_k(\mathbf{x}))}{\sum_{j=1}^K \exp(s_j(\mathbf{x}))}
$$

Gdzie:
- $ K $ to liczba klas.
- $ \mathbf{s}(\mathbf{x}) $ to wektor zawierający wyniki dla każdej klasy dla instancji $ \mathbf{x} $.
- $ \sigma(\mathbf{s}(\mathbf{x}))_k $ jest szacowanym prawdopodobieństwem, że instancja $ \mathbf{x} $ należy do klasy $ k $, biorąc pod uwagę wyniki każdej klasy dla tej instancji.

### Predykcja klasy

Podobnie jak w regresji logistycznej, klasyfikator regresji Softmax przewiduje klasę jako tę, która posiada najwyższe prawdopodobieństwo (która jest po prostu klasą o najwyższym wyniku):

$$
\hat{y} = \arg\max_k (\sigma(\mathbf{s}(\mathbf{x}))_k) = \arg\max_k (s_k(\mathbf{x})).
$$

## Funkcja kosztu

Softmax Regression minimalizuje funkcję kosztową zwaną entropią krzyżową:

$$
J(\mathbf{\Theta}) = - \frac{1}{m} \sum_{i=1}^{m} \sum_{k=1}^{K} y^{(i)}_k \log(\hat{p}^{(i)}_k)
$$

Gdzie:
- $ y^{(i)}_k $ jest równe 1, jeśli klasa docelowa dla $ i $-tego wystąpienia wynosi $ k $, a w przeciwnym razie jest równa 0.
- $ m $ to liczba instancji w zbiorze treningowym.

Entropia krzyżowa penalizuje model, gdy szacuje niskie prawdopodobieństwo dla klasy docelowej. Jest często używana do mierzenia, jak dobrze zestaw oszacowanych prawdopodobieństw klas jest zgodny z klasami docelowymi.

## Definicja entropii krzyżowej

Entropia krzyżowa między dwoma rozkładami prawdopodobieństw $ p $ i $ q $ jest zdefiniowana jako:

$$
H(p, q) = - \sum_x p(x) \log(q(x)),
$$

(gdy rozkłady są dyskretne).

### Podsumowanie

Regresja Softmax jest uogólnieniem regresji logistycznej, które pozwala na bezpośrednie obsługiwanie wielu klas. Wykorzystuje funkcję softmax do szacowania prawdopodobieństw klas i minimalizuje entropię krzyżową, aby dopasować model do danych.
