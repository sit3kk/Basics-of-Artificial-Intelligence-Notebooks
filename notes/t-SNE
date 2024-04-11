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
