// Autor del código: https://www.cartagena99.com/recursos/alumnos/temarios/Backtracking.pdf

public class NReinas {

    public static void main(String[] args) {
        int n = 8; // Haremos uso de 8 reinas únicamente
        n_reinas(n); // O(1) - llamada a la función
    }

    public static void n_reinas(int n) {
        int[] c = new int[n]; // O(n) - creación del array

        boolean[] f = new boolean[n]; // O(n) - creación del array
        for (int i = 0; i < n; i++) // O(n) - iteración sobre el array
            f[i] = true; // O(1) - asignación

        boolean[] dp = new boolean[2 * n - 1]; // O(2n-1) -> O(n) - creación del array
        for (int i = 0; i < 2 * n - 1; i++) // O(2n-1) -> O(n) - iteración sobre el array
            dp[i] = true; // O(1) - asignación

        boolean[] ds = new boolean[2 * n - 1]; // O(2n-1) -> O(n) - creación del array
        for (int i = 0; i < 2 * n - 1; i++) // O(2n-1) -> O(n) - iteración sobre el array
            ds[i] = true; // O(1) - asignación

        buscarReinas(n, 0, c, f, dp, ds); // O(n!) - llamada a la función recursiva
    }

    public static void buscarReinas(int n, int i, int[] solucion,
                                    boolean[] f, boolean[] dp, boolean[] ds) {
        for (int j = 0; j < n; j++) // O(n) - iteración sobre las columnas
            if (f[j] && dp[i - j + n - 1] && ds[i + j]) { // O(1) - verificación de condiciones
                solucion[i] = j; // O(1) - asignación

                f[j] = false; // O(1) - asignación
                dp[i - j + n - 1] = false; // O(1) - asignación
                ds[i + j] = false; // O(1) - asignación

                if (i == n - 1) // O(1) - comparación
                    imprimir(solucion); // O(n^2) - impresión del tablero
                else
                    buscarReinas(n, i + 1, solucion, f, dp, ds); // O(n!) - llamada recursiva

                f[j] = true; // O(1) - asignación
                dp[i - j + n - 1] = true; // O(1) - asignación
                ds[i + j] = true; // O(1) - asignación
            }
    }

    public static void imprimir(int[] solucion) {
        int n = solucion.length; // O(1) - obtener longitud del array
        for (int i = 0; i < n; i++) { // O(n) - iteración sobre las filas
            for (int j = 0; j < n; j++) { // O(n) - iteración sobre las columnas
                if (solucion[i] == j) // O(1) - comparación
                    System.out.print("Q "); // O(1) - impresión
                else
                    System.out.print(". "); // O(1) - impresión
            }
            System.out.println(); // O(1) - salto de línea
        }
        System.out.println(); // O(1) - salto de línea adicional
    }
}
