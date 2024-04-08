# Gaussian Mixture Model (GMM) - Przykład

Algorytm GMM to podejście gęstościowe do grupowania danych, które wykorzystuje mieszaninę rozkładów normalnych.

## Inicjalizacja
Wybierz liczbę klastrów `K` i zainicjuj parametry dla każdego klastra:
- `π_k`: Waga klastra
- `μ_k`: Średnia klastra
- `Σ_k`: Macierz kowariancji klastra

## Krok E (Expectation)
Dla każdego punktu danych `x_i` oblicz `responsibilities`, które określają stopień przynależności do każdego klastra.

## Krok M (Maximization)
Zaktualizuj parametry klastrów, aby maksymalizować funkcję wiarygodności na podstawie `responsibilities`.

## Iteracja
Powtarzaj kroki E i M do osiągnięcia konwergencji.

# Przygotowanie danych

Przyjmijmy bardzo prosty zestaw danych składający się z kilku punktów, które będziemy próbować podzielić na dwa klastry (K=2) dla uproszczenia:

Punkty: `[1.0, 2.0, 1.5, 5.5, 6.0, 5.8]`

Dla uproszczenia, przyjmujemy, że mamy jednowymiarowe dane.

## Krok 1: Inicjalizacja

Zainicjujemy parametry dla dwóch klastrów (K=2):

- Wagi klastrów π<sub>k</sub>: dla uproszczenia, załóżmy, że każdy klaster ma równą wagę na początku, np. π<sub>1</sub> = 0.5 i π<sub>2</sub> = 0.5.
- Średnie klastrów μ<sub>k</sub>: zainicjujemy średnie dwóch klastrów jako pierwszy i ostatni punkt danych, więc μ<sub>1</sub> = 1.0 i μ<sub>2</sub> = 5.8.
- Macierze kowariancji Σ<sub>k</sub>: ponieważ mamy do czynienia z danymi jednowymiarowymi, "macierz" kowariancji będzie po prostu wariancją. Załóżmy początkową wariancję dla obu klastrów jako Σ<sub>1</sub> = Σ<sub>2</sub> = 1.0.

## Krok 2: Krok E (Expectation)

Obliczymy prawdopodobieństwa przynależności każdego punktu do każdego z klastrów na podstawie aktualnych parametrów.

## Krok 3: Krok M (Maximization)

Na podstawie obliczonych prawdopodobieństw zaktualizujemy parametry π<sub>k</sub>, μ<sub>k</sub> i Σ<sub>k</sub> dla każdego klastra.

Przejdźmy teraz do implementacji tych kroków. Zacznijmy od inicjalizacji i wykonajmy krok E.

W kroku E (Expectation) obliczyliśmy 'responsibilities', czyli prawdopodobieństwa przynależności każdego z punktów do obu klastrów, na podstawie aktualnych parametrów. Oto obliczone 'responsibilities' dla każdego punktu:

- Dla punktów bliskich 1.0 (pierwsze trzy wartości), 'responsibilities' wskazują silną przynależność do pierwszego klastra.
- Dla punktów bliskich 5.8 (ostatnie trzy wartości), 'responsibilities' wskazują silną przynależność do drugiego klastra.
