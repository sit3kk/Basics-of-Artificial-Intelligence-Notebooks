# Support Vector Machines (SVM)

Support Vector Machines (SVM) to potężne algorytmy nadzorowanego uczenia maszynowego stosowane głównie do klasyfikacji, ale także do regresji. Celem SVM jest znalezienie optymalnej hiperpowierzchni, która maksymalizuje margines między dwiema klasami w danych treningowych.

## Podstawowe pojęcia

### Hiperpłaszczyzna

Hiperpłaszczyzna to przestrzeń, która dzieli dane na różne klasy. W przypadku dwuwymiarowych danych hiperpłaszczyzna jest linią, w trójwymiarowych płaszczyzną, a dla wyższych wymiarów przestrzeni jest to przestrzeń n-1 wymiarowa.

### Margines

Margines jest odległością między hiperpłaszczyzną a najbliższymi punktami danych z każdej klasy. SVM maksymalizuje ten margines, aby poprawić generalizację modelu.

### Wektory nośne

Wektory nośne to punkty danych, które znajdują się najbliżej hiperpłaszczyzny i mają kluczowe znaczenie dla definiowania jej pozycji i orientacji. To właśnie te punkty mają największy wpływ na budowę modelu SVM.

## Jak działa SVM

1. **Znalezienie hiperpowierzchni:** SVM znajduje hiperpowierzchnię, która najlepiej oddziela dane z różnych klas. 
2. **Maksymalizacja marginesu:** Optymalna hiperpowierzchnia to taka, która maksymalizuje margines między dwiema klasami danych.

### Równanie hiperpłaszczyzny

Hiperpłaszczyznę można przedstawić jako równanie:

$$
\mathbf{w} \cdot \mathbf{x} - b = 0
$$

Gdzie:
- \( \mathbf{w} \) to wektor wag.
- \( \mathbf{x} \) to wektor cech.
- \( b \) to wyraz wolny.

### Funkcja decyzyjna

Funkcja decyzyjna SVM określa, do której klasy należy nowy punkt danych:

$$
f(\mathbf{x}) = \mathbf{w} \cdot \mathbf{x} - b
$$

## Rodzaje SVM

### SVM liniowe

SVM liniowe stosuje się, gdy dane są liniowo separowalne. Algorytm stara się znaleźć linię (w 2D) lub płaszczyznę (w 3D), która najlepiej oddziela klasy.

### SVM nieliniowe

SVM nieliniowe są używane, gdy dane nie są liniowo separowalne. W takich przypadkach SVM wykorzystuje jądra (kernels) do transformacji danych do wyższych wymiarów, gdzie możliwe jest znalezienie liniowej hiperpowierzchni separującej klasy.

## Jądra (Kernels)

Jądra są funkcjami, które przekształcają dane do wyższych wymiarów. Popularne jądra to:

- **RBF (Radial Basis Function):**

$$
K(\mathbf{x}_i, \mathbf{x}_j) = \exp(-\gamma \|\mathbf{x}_i - \mathbf{x}_j\|^2)
$$

- **Polynomial:**

$$
K(\mathbf{x}_i, \mathbf{x}_j) = (\mathbf{x}_i \cdot \mathbf{x}_j + c)^d
$$

- **Sigmoid:**

$$
K(\mathbf{x}_i, \mathbf{x}_j) = \tanh(\alpha \mathbf{x}_i \cdot \mathbf{x}_j + c)
$$

## Funkcja kosztu

Funkcja kosztu SVM penalizuje błędy klasyfikacji i stara się maksymalizować margines:

$$
J(\mathbf{w}) = \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^{m} \max(0, 1 - y_i (\mathbf{w} \cdot \mathbf{x}_i - b))
$$

Gdzie:
- \( C \) to parametr regularyzacji, który kontroluje równowagę między maksymalizacją marginesu a minimalizacją błędów klasyfikacji.

## Zalety SVM

- **Efektywność w przestrzeniach wysokowymiarowych.**
- **Skuteczność przy dużej liczbie cech.**
- **Elastyczność dzięki wykorzystaniu różnych jąder.**

## Wady SVM

- **Skalowanie do dużych zbiorów danych może być trudne.**
- **Wybór odpowiedniego jądra i parametrów może być skomplikowany.**

### Podsumowanie

SVM to wszechstronne i potężne narzędzie do klasyfikacji i regresji, które wykorzystuje optymalną hiperpowierzchnię do maksymalizacji marginesu między klasami. Dzięki wykorzystaniu jąder SVM potrafi radzić sobie zarówno z liniowo, jak i nieliniowo separowalnymi danymi.
