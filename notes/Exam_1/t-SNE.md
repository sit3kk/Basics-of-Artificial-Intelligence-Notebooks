# t-SNE (t-distributed Stochastic Neighbor Embedding)

t-SNE jest zaawansowaną techniką redukcji wymiarowości, która jest często wykorzystywana do wizualizacji danych wielowymiarowych w przestrzeni dwuwymiarowej (R2) lub trójwymiarowej (R3). Algorytm ten jest szczególnie ceniony za zdolność do zachowania lokalnych struktur i odkrywania wzorców w złożonych zbiorach danych.

## Główne cechy t-SNE

- **SNE (Stochastic Neighbor Embedding):** Bazuje na podejściu probabilistycznym do zachowania sąsiedztwa punktów. SNE próbuje zachować rozkłady prawdopodobieństwa podobieństwa punktów w przestrzeni wielowymiarowej i przestrzeni o niższej wymiarowości.
- **t-Statystyka i Rozkład Cauchy'ego:** W przeciwieństwie do oryginalnego SNE, t-SNE wykorzystuje t-Studenta (rozkład Cauchy'ego) w przestrzeni o niższej wymiarowości. Pozwala to na lepsze oddzielenie klastrów danych przez łagodzenie problemu "zwijania kuli" (ang. "crowding problem").
- **Perplexity:** Parametr perplexity odgrywa kluczową rolę w t-SNE, kontrolując skalę lokalności. Można go interpretować jako efektywną liczbę sąsiadów. Typowa wartość dla perplexity to około 30, ale dobór optymalnej wartości zależy od rozmiaru i natury danych.

## Jak działa t-SNE?

1. **Początkowo:** Dla każdego punktu w oryginalnej przestrzeni wielowymiarowej, t-SNE definiuje prawdopodobieństwo podobieństwa między punktami, tak, że podobne punkty mają wysokie prawdopodobieństwo bycia "sąsiadami", a niepodobne - niskie.
2. **Optymalizacja:** t-SNE następnie poszukuje reprezentacji tych punktów w przestrzeni o niższej wymiarowości (zazwyczaj R2 lub R3), starając się jak najlepiej odwzorować te prawdopodobieństwa podobieństwa. Używa do tego celu techniki optymalizacji gradientowej.
3. **Wynik:** Ostateczna wizualizacja w przestrzeni o niższej wymiarowości zachowuje lokalne struktury danych, co umożliwia identyfikację grup (klastrów) danych i ich wzajemnych relacji.

## Wady i zalety

### Zalety

- **Zachowanie lokalnych struktur:** t-SNE jest bardzo dobre w zachowaniu lokalnych relacji między punktami, co ułatwia identyfikację klastrów i subklastrów w danych.
- **Wizualizacja skomplikowanych struktur danych:** Pozwala na efektywne wizualizowanie danych o złożonych strukturach i różnorodnych skalach.

### Wady

- **Wrażliwość na parametry:** Wybór parametru perplexity może mieć znaczący wpływ na wyniki, wymagając eksperymentowania.
- **Nie nadaje się do redukcji wymiarowości:** t-SNE jest głównie używane do wizualizacji, a nie jako krok przeduczania w modelowaniu predykcyjnym, ze względu na tendencję do tworzenia optymalnych reprezentacji tylko w bardzo niskich wymiarach.
- **Koszt obliczeniowy:** t-SNE może być czasochłonne, szczególnie dla bardzo dużych zbiorów danych.

t-SNE jest potężnym narzędziem do eksploracji i wizualizacji danych, które pomaga w odkrywaniu ukrytych struktur w danych wielowymiarowych, choć wymaga starannego doboru parametrów i interpretacji wyników.

# Przykład działania t-SNE

Załóżmy, że naszym zadaniem jest wizualizacja złożonego zbioru danych kwiatów, gdzie każdy kwiat opisany jest za pomocą czterech cech: długość płatka, szerokość płatka, długość kielicha i szerokość kielicha. Naszym celem jest przedstawienie tych danych w przestrzeni dwuwymiarowej (R2), aby łatwiej zidentyfikować wzorce i zależności między różnymi typami kwiatów.

## Krok 1: Przygotowanie danych

Mamy zbiór danych składający się z 150 próbek kwiatów, każda z nich opisana czterema cechami. Dane są pierwotnie w przestrzeni czterowymiarowej, co utrudnia ich bezpośrednią wizualizację.

## Krok 2: Stosowanie t-SNE

Do redukcji wymiarowości naszego zbioru danych stosujemy t-SNE z następującymi parametrami:
- `perplexity`: 30, co jest standardową wartością dla zbiorów o średniej wielkości i oznacza, że każdy punkt będzie miał około 30 "sąsiadów" w sensie podobieństwa.
- `n_components`: 2, ponieważ chcemy zredukować nasze dane do przestrzeni dwuwymiarowej.

## Krok 3: Wizualizacja wyników

Po zastosowaniu t-SNE otrzymujemy nową reprezentację naszych danych w przestrzeni dwuwymiarowej. Każdy punkt na wykresie odpowiada jednemu kwiatowi z oryginalnego zbioru danych, a jego położenie odzwierciedla podobieństwo do innych kwiatów w kontekście wszystkich czterech cech.

### Co możemy zaobserwować?

- **Klastry:** Kwiaty podobne do siebie (np. te same gatunki) są grupowane razem w klastry, co wskazuje na ich bliskość w przestrzeni wielowymiarowej.
- **Oddzielenie gatunków:** Jeśli różne gatunki kwiatów mają unikalne charakterystyki, t-SNE pomoże w ich rozdzieleniu na wykresie, nawet jeśli różnice te są subtelne i rozproszone po wielu wymiarach.
- **Wyjątki i anomalie:** Punkty, które nie pasują do głównych grup, mogą zostać zidentyfikowane jako potencjalne wyjątki lub anomalie, co może wskazywać na błędy w danych lub nietypowe przypadki.

## Podsumowanie

t-SNE pozwoliło nam na skuteczną wizualizację i zrozumienie złożonych zależności między próbkami kwiatów, co byłoby trudne do osiągnięcia w oryginalnej, czterowymiarowej przestrzeni. Ta technika jest nieoceniona w eksploracyjnej analizie danych, gdzie wizualne przedstawienie może ujawnić ukryte wzorce i struktury.
