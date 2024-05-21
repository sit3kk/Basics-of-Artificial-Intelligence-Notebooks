# Definicje i Przykład Metryk Klasyfikacyjnych

## Accuracy (ACC)
**Accuracy** (dokładność) to miara wydajności klasyfikatora, określająca stosunek liczby poprawnie sklasyfikowanych próbek do całkowitej liczby próbek.

$$
\text{Accuracy} = \frac{\text{Liczba poprawnych predykcji}}{\text{Całkowita liczba próbek}}
$$

## Confusion Matrix
**Confusion Matrix** (macierz pomyłek) to tabela, która pozwala wizualizować wydajność algorytmu klasyfikacji. Składa się z czterech elementów:

- **TP (True Positive):** Liczba prawdziwie pozytywnych wyników.
- **TN (True Negative):** Liczba prawdziwie negatywnych wyników.
- **FP (False Positive):** Liczba fałszywie pozytywnych wyników.
- **FN (False Negative):** Liczba fałszywie negatywnych wyników.

|                        | Przewidywane Pozytywne | Przewidywane Negatywne |
|------------------------|------------------------|------------------------|
| **Rzeczywiste Pozytywne** | TP                     | FN                     |
| **Rzeczywiste Negatywne** | FP                     | TN                     |

## F1 Score
**F1 Score** to miara wydajności klasyfikatora, która jest średnią harmoniczną precyzji (precision) i czułości (recall). 

$$
\text{F1 Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$

Gdzie:
- **Precision** (precyzja) to stosunek liczby prawdziwie pozytywnych wyników do sumy prawdziwie pozytywnych i fałszywie pozytywnych wyników.

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

- **Recall** (czułość) to stosunek liczby prawdziwie pozytywnych wyników do sumy prawdziwie pozytywnych i fałszywie negatywnych wyników.

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

## Przykład

Załóżmy, że mamy zbiór danych testowych zawierający 10 próbek. Wyniki klasyfikacji są następujące:

- TP = 3 (prawdziwie pozytywne)
- TN = 4 (prawdziwie negatywne)
- FP = 1 (fałszywie pozytywne)
- FN = 2 (fałszywie negatywne)

### Obliczenia

1. **Accuracy (ACC):**

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{3 + 4}{3 + 4 + 1 + 2} = \frac{7}{10} = 0.7
$$

2. **Confusion Matrix:**

|                        | Przewidywane Pozytywne | Przewidywane Negatywne |
|------------------------|------------------------|------------------------|
| **Rzeczywiste Pozytywne** | 3                      | 2                     |
| **Rzeczywiste Negatywne** | 1                      | 4                     |

3. **Precision:**

$$
\text{Precision} = \frac{TP}{TP + FP} = \frac{3}{3 + 1} = \frac{3}{4} = 0.75
$$

4. **Recall:**

$$
\text{Recall} = \frac{TP}{TP + FN} = \frac{3}{3 + 2} = \frac{3}{5} = 0.6
$$

5. **F1 Score:**

$$
\text{F1 Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \cdot \frac{0.75 \cdot 0.6}{0.75 + 0.6} = 2 \cdot \frac{0.45}{1.35} = 2 \cdot 0.333 = 0.666
$$

### Podsumowanie

- **Accuracy:** 0.7
- **Precision:** 0.75
- **Recall:** 0.6
- **F1 Score:** 0.666

Powyższe miary pomagają zrozumieć, jak dobrze działa klasyfikator w różnych aspektach, takich jak dokładność, precyzja, czułość oraz zbalansowanie pomiędzy precyzją a czułością.

# Kiedy używać której miary oceny klasyfikatora

Wybór odpowiedniej miary oceny klasyfikatora zależy od specyfiki problemu i celów, jakie chcemy osiągnąć. Poniżej przedstawiono kilka kluczowych scenariuszy i rekomendacje dotyczące użycia różnych miar.

## Accuracy (Dokładność)

**Kiedy używać:**
- Gdy dane są zrównoważone, czyli liczba próbek w każdej klasie jest mniej więcej równa.
- Gdy koszt popełnienia błędu (fałszywie pozytywny vs fałszywie negatywny) jest taki sam dla obu typów błędów.

**Kiedy nie używać:**
- Gdy dane są niezbalansowane, czyli jedna klasa jest znacznie liczniejsza od drugiej.
- Gdy koszty popełnienia błędów są różne dla różnych klas.

## Confusion Matrix (Macierz Pomyłek)

**Kiedy używać:**
- Zawsze, gdy chcemy uzyskać szczegółowy przegląd wydajności klasyfikatora.
- Gdy ważne jest zrozumienie liczby prawdziwych pozytywów, prawdziwych negatywów, fałszywych pozytywów i fałszywych negatywów.
- Przy analizie niezbalansowanych danych, aby lepiej zrozumieć skutki popełnionych błędów.

**Kiedy nie używać:**
- Macierz pomyłek jest zawsze przydatna, ale sama w sobie nie jest wystarczająca do pełnej oceny modelu; zwykle jest używana w połączeniu z innymi miarami.

## Precision (Precyzja)

**Kiedy używać:**
- Gdy koszt fałszywie pozytywnych wyników jest wysoki.
- Gdy zależy nam na minimalizowaniu liczby błędnych alarmów (fałszywych pozytywów).

**Przykłady:**
- Wykrywanie spamu: Gdy wysyłanie fałszywie pozytywnych wiadomości do folderu spamu jest kosztowne.
- Diagnostyka medyczna: Gdy fałszywie pozytywna diagnoza może prowadzić do niepotrzebnych i potencjalnie szkodliwych dalszych testów.

## Recall (Czułość)

**Kiedy używać:**
- Gdy koszt fałszywie negatywnych wyników jest wysoki.
- Gdy zależy nam na maksymalnym wykryciu wszystkich pozytywnych przypadków.

**Przykłady:**
- Wykrywanie chorób: Gdy przeoczenie prawdziwie pozytywnego przypadku (fałszywie negatywne) jest bardzo kosztowne.
- Systemy bezpieczeństwa: Gdy niezauważenie zagrożenia może mieć poważne konsekwencje.

## F1 Score

**Kiedy używać:**
- Gdy dane są niezbalansowane i ważne jest zbalansowanie pomiędzy precyzją a czułością.
- Gdy zarówno fałszywie pozytywne, jak i fałszywie negatywne wyniki są kosztowne i chcemy osiągnąć kompromis.

**Kiedy nie używać:**
- Gdy dokładność samodzielnie jest wystarczająca (np. w dobrze zbalansowanych zbiorach danych z równymi kosztami błędów).

## Przykłady

### Przykład 1: Wykrywanie Spamu

- **Scenariusz:** Chcemy klasyfikować e-maile jako spam (1) lub nie-spam (0).
- **Ważne miary:**
  - **Precision:** Ważne, aby zminimalizować fałszywie pozytywne (nie-spam zaklasyfikowany jako spam), aby nie przegapić ważnych wiadomości.
  - **Recall:** Ważne, aby zidentyfikować jak najwięcej spamu.

### Przykład 2: Diagnostyka Medyczna

- **Scenariusz:** Chcemy zidentyfikować chorobę u pacjentów.
- **Ważne miary:**
  - **Recall:** Ważne, aby wykryć wszystkie przypadki choroby (fałszywie negatywne mogą być bardzo kosztowne).
  - **F1 Score:** Ważne, aby zrównoważyć precyzję i czułość, jeśli fałszywie pozytywne diagnozy również są kosztowne.

### Przykład 3: Systemy Bezpieczeństwa

- **Scenariusz:** Chcemy wykryć zagrożenia bezpieczeństwa (np. intruzów).
- **Ważne miary:**
  - **Recall:** Ważne, aby wykryć wszystkie zagrożenia (fałszywie negatywne mogą być bardzo kosztowne).
  - **Precision:** Ważne, aby zminimalizować fałszywe alarmy (fałszywie pozytywne), które mogą powodować niepotrzebne interwencje.

## Podsumowanie

Każda miara ma swoje zalety i wady, a wybór odpowiedniej zależy od specyficznych potrzeb i kontekstu zastosowania. W praktyce, często używa się kilku miar jednocześnie, aby uzyskać pełny obraz wydajności klasyfikatora.
