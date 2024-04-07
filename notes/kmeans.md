# Zwykły K-Means

## Przykładowe Dane

Mamy 6 punktów: {2, 4, 5, 11, 12, 20}, i chcemy podzielić je na 2 klastry (k = 2).

### Krok 1: Losowa Inicjalizacja Centroidów

Wybieramy losowo dwa punkty jako początkowe centroidy. Załóżmy, że losowo wybieramy:

- C1: 4
- C2: 11

### Krok 2: Przypisanie do Centroidów

Punkty {2, 4, 5} są bliżej C1.
Punkty {11, 12, 20} są bliżej C2.

### Krok 3: Aktualizacja Centroidów

Nowy C1 to średnia {2, 4, 5}, czyli 3.66.
Nowy C2 to średnia {11, 12, 20}, czyli 14.33.

### Krok 4: Iteracja

Powtarzamy kroki 2 i 3, aż przypisania punktów się stabilizują. W tym prostym przypadku, mogą się już nie zmienić po pierwszej iteracji.

# K-Means++

## Przykładowe Dane

Mamy 6 punktów: {2, 4, 5, 11, 12, 20}, i chcemy podzielić je na 2 klastry (k = 2).

### Krok 1: Ulepszona Inicjalizacja Centroidów

Losowo wybieramy pierwszy centroid, załóżmy C1: 4.
Obliczamy odległości wszystkich punktów od wybranego centroidu i wybieramy kolejny centroid z prawdopodobieństwem proporcjonalnym do kwadratu tych odległości. Załóżmy, że ten proces daje nam C2: 20 jako drugi centroid.

### Krok 2: Przypisanie do Centroidów

Z odległości do centroidów {4, 20}:

Punkty {2, 4, 5} są bliżej C1.
Punkty {11, 12, 20} są bliżej C2.

### Krok 3: Aktualizacja Centroidów

Nowy C1: średnia {2, 4, 5} = 3.66.
Nowy C2: średnia {11, 12, 20} = 14.33.

### Krok 4: Iteracja

Powtarzamy kroki 2 i 3, aż do konwergencji. Metoda k-means++ może skutkować szybszym osiągnięciem stabilności, dzięki lepszemu wyborowi początkowym centroidów.

# Mini-batch k-means

## Przykładowe Dane

Załóżmy, że mamy zestaw danych składający się z 6 punktów: {2, 4, 5, 11, 12, 20}. Chcemy podzielić je na 2 klastry (k = 2).

### Krok 1: Inicjalizacja Centroidów

Losowo wybieramy dwa punkty jako początkowe centroidy. Załóżmy, że wybieramy 4 i 12 jako początkowe centroidy.

- C1: 4
- C2: 12

### Krok 2: Wybór Mini-Batch

Załóżmy, że w każdym mini-batch będziemy mieli 3 punkty. Losowo wybieramy pierwsze trzy punkty: {2, 4, 5}.

### Krok 3: Przypisanie do Centroidów

Punkty 2, 4, 5 są bliżej centroidu C1 (4), więc wszystkie są przypisane do C1.

### Krok 4: Aktualizacja Centroidów

Aktualizujemy centroidy na podstawie przypisanych punktów:

- Nowy C1 to średnia z {2, 4, 5}, co daje 3.66 (zaokrąglając do dwóch miejsc po przecinku).
- C2 pozostaje niezmienione, ponieważ żaden punkt nie został do niego przypisany w tej iteracji.

### Krok 5: Powtórzenie z Nowym Mini-Batch

Wybieramy kolejny mini-batch punktów: {11, 12, 20}.

### Krok 6: Przypisanie do Centroidów

Punkty 11 i 12 są bliżej C2, a 20 jest znacznie bliżej C2 niż C1, więc wszystkie są przypisane do C2.

### Krok 7: Aktualizacja Centroidów

Aktualizujemy centroidy na podstawie nowych przypisań:

- C1 pozostaje niezmienione, ponieważ żaden nowy punkt nie został do niego przypisany.
- Nowy C2 to średnia z {11, 12, 20}, co daje 14.33 (zaokrąglając).

### Krok 8: Sprawdzenie Konwergencji

W prawdziwej iteracji algorytmu kontynuowalibyśmy proces z kolejnymi mini-batchami i aktualizacjami centroidów aż do osiągnięcia konwergencji, czyli do momentu, gdy przypisania punktów do klastrów się stabilizują i centroidy się już nie zmieniają.

