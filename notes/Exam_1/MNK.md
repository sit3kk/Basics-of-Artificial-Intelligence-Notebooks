# Metoda Najmniejszych Kwadratów

Metoda najmniejszych kwadratów jest standardową techniką w statystyce do estymacji linii regresji w modelach liniowych. Celem jest znalezienie linii (lub hiperpłaszczyzny w wyższych wymiarach), która najlepiej pasuje do zestawu punktów danych. "Najlepiej pasująca" linia jest zdefiniowana jako linia, która minimalizuje sumę kwadratów różnic pomiędzy obserwowanymi wartościami a wartościami przewidywanymi przez model liniowy.

## Model Liniowy

W przypadku modelu liniowego z jedną zmienną niezależną, model jest opisany równaniem:

\[ y = ax + b \]

gdzie:
- \( y \) to zmienna zależna,
- \( x \) to zmienna niezależna,
- \( a \) to współczynnik kierunkowy prostej (nachylenie),
- \( b \) to wyraz wolny (przecięcie z osią Y).

## Kryterium Najmniejszych Kwadratów

Znalezienie najlepszych parametrów \( a \) i \( b \) polega na minimalizacji sumy kwadratów odchyleń \( S \):

\[ S = \sum_{i=1}^{n} (y_i - (ax_i + b))^2 \]

## Wzory na Współczynniki \( a \) i \( b \)

Parametry \( a \) i \( b \) są obliczane za pomocą wzorów:

\[ a = \frac{N\sum (x_iy_i) - \sum x_i \sum y_i}{N\sum x_i^2 - (\sum x_i)^2} \]

\[ b = \frac{\sum y_i - a \sum x_i}{N} \]

gdzie:
- \( N \) to liczba obserwacji,
- \( x_i \) to i-ta wartość zmiennej niezależnej,
- \( y_i \) to i-ta wartość zmiennej zależnej.

## Procedura Obliczania

1. Zsumuj wszystkie wartości \( x \) i \( y \).
2. Znajdź sumę iloczynów każdej pary \( x_i \) i \( y_i \).
3. Znajdź sumę kwadratów wszystkich wartości \( x \).
4. Podstaw wartości do wzorów na \( a \) i \( b \).
5. Oblicz wartości \( a \) i \( b \).

Uzyskane parametry \( a \) i \( b \) pozwolą na narysowanie linii regresji, która jest najlepszym dopasowaniem do danych w sensie metody najmniejszych kwadratów.
