## Współczynniki korelacji

### Korelacja Pearsona
- **Typ**: Parametryczna miara korelacji.
- **Co ocenia**: Liniowy związek między dwiema ciągłymi zmiennymi.
- **Charakterystyka**: Zakłada normalność danych. Wrażliwa na wartości odstające.
- **Zakres**: Od -1 (doskonała negatywna korelacja liniowa) do 1 (doskonała pozytywna korelacja liniowa).
- **Przypadek użycia**: Gdy oczekiwany jest liniowy związek i dane są w przybliżeniu normalne bez wartości odstających.

### Korelacja rang Spearmana
- **Typ**: Nieliniowa miara korelacji rang.
- **Co ocenia**: Monotoniczny związek, czy to liniowy czy nieliniowy, między dwiema zmiennymi.
- **Charakterystyka**: Nie zakłada normalności danych. Mniej wrażliwa na wartości odstające niż korelacja Pearsona.
- **Zakres**: Od -1 do 1, podobnie jak Pearson, ale oparta na wartościach rangowych.
- **Przypadek użycia**: Gdy związek jest monotoniczny, ale niekoniecznie liniowy.

### Korelacja Kendalla
- **Typ**: Nieliniowa miara korelacji rang.
- **Co ocenia**: Związek porządkowy między parami obserwacji.
- **Charakterystyka**: Odporna na wartości odstające. Mniej wrażliwa na błędy w danych niż korelacja Spearmana.
- **Zakres**: Od -1 (doskonała negatywna korelacja rang) do 1 (doskonała pozytywna korelacja rang).
- **Przypadek użycia**: W analizie danych z dużą liczbą powiązań.

### Korelacja odległościowa (Distance correlation)
- **Typ**: Miara korelacji oparta na odległościach.
- **Co ocenia**: Związek między zmiennymi w przestrzeni wielowymiarowej.
- **Charakterystyka**: Może wykrywać związki nieliniowe i złożone, które nie są widoczne dla innych współczynników korelacji.
- **Zakres**: Od 0 (brak zależności) do 1 (doskonała zależność), ale nie przyjmuje wartości ujemnych.
- **Przypadek użycia**: W sytuacjach, gdy inne miary korelacji nie wykazują związku, a dane mogą mieć złożone nieliniowe związki.
