// Autor del código: https://www.cartagena99.com/recursos/alumnos/temarios/Backtracking.pdf

public class NReinas {

    public static void main(String[] args) {
        int n = 8; // Puedes cambiar el valor de n según sea necesario
        n_reinas(n);
    }

    public static void n_reinas(int n) {
        int[] c = new int[n];

        boolean[] f = new boolean[n];
        for (int i = 0; i < n; i++)
            f[i] = true;

        boolean[] dp = new boolean[2 * n - 1];
        for (int i = 0; i < 2 * n - 1; i++)
            dp[i] = true;

        boolean[] ds = new boolean[2 * n - 1];
        for (int i = 0; i < 2 * n - 1; i++)
            ds[i] = true;

        buscarReinas(n, 0, c, f, dp, ds);
    }

    public static void buscarReinas(int n, int i, int[] solucion,
                                    boolean[] f, boolean[] dp, boolean[] ds) {
        for (int j = 0; j < n; j++)
            if (f[j] && dp[i - j + n - 1] && ds[i + j]) {
                solucion[i] = j;

                f[j] = false;
                dp[i - j + n - 1] = false;
                ds[i + j] = false;

                if (i == n - 1)
                    imprimir(solucion);
                else
                    buscarReinas(n, i + 1, solucion, f, dp, ds);

                f[j] = true;
                dp[i - j + n - 1] = true;
                ds[i + j] = true;
            }
    }

    public static void imprimir(int[] solucion) {
        int n = solucion.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (solucion[i] == j)
                    System.out.print("Q ");
                else
                    System.out.print(". ");
            }
            System.out.println();
        }
        System.out.println();
    }
}

                    
