# DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

DBSCAN jest algorytmem klastrowania wykorzystywanym do identyfikacji skupisk (klastrów) w danych na podstawie gęstości. Jest szczególnie przydatny w przypadkach, gdy kształty klastrów są nieregularne i kiedy w danych występuje szum.

## Zasada Działania

Algorytm klasyfikuje punkty danych na podstawie dwóch kluczowych parametrów:

- **ε (epsilon):** Promień sąsiedztwa wokół punktu.
- **MinPts (minimalna liczba punktów):** Minimalna liczba punktów w sąsiedztwie ε, potrzebna, aby punkt był uznany za centralny.

### Kategorie Punków

W DBSCAN każdy punkt jest klasyfikowany jako:

- **Punkt centralny (core point):** Posiada co najmniej MinPts w swoim sąsiedztwie ε.
- **Punkt graniczny (border point):** Nie jest punktem centralnym, ale znajduje się w sąsiedztwie punktu centralnego.
- **Szum (noise point):** Nie jest ani punktem centralnym, ani granicznym.

## Algorytm

1. **Inicjalizacja:** Wszystkie punkty są oznaczane jako nieodwiedzone.
2. **Przetwarzanie:**
   - Dla każdego nieodwiedzonego punktu, oznacz go jako odwiedzony.
   - Znajdź wszystkich sąsiadów w obrębie ε.
   - Jeśli punkt ma mniej niż MinPts sąsiadów, oznacz go jako szum.
   - W przeciwnym razie, rozpocznij tworzenie klastra z tego punktu jako punktu centralnego.
   - Dodaj do klastra wszystkie sąsiadujące punkty i iteracyjnie rozszerzaj klastery.
3. **Powtarzaj** do momentu odwiedzenia wszystkich punktów.

## Zalety i Wady

### Zalety

- Skutecznie radzi sobie z danymi o nieregularnych kształtach i szumami.
- Nie wymaga z góry określonej liczby klastrów.

### Wady

- Wybór parametrów ε i MinPts może być trudny.
- Nie jest efektywny dla danych, gdzie klastry mają bardzo różną gęstość.

DBSCAN jest potężnym narzędziem do analizy przestrzennej i wykrywania anomalii, oferującym elastyczność w radzeniu sobie z różnorodnością kształtów i szumów w danych.
