// Autor del código: https://www.cartagena99.com/recursos/alumnos/temarios/Backtracking.pdf

void n_reinas(int n){
    int[] c = new int[n];

    boolean[] f = new boolean[n];
    for(int i=0; i<n; i++)
        f[i] = true;
    
    boolean[] dp = new boolean[2*n-1];
    for(int i=0; i<2*n-1; i++)
        dp[i] = true;
    
    boolean[] ds = new boolean[2*n-1];
    for(int i=0; i<2*n-1; i++)
        ds[i] = true;

    buscarReinas(8, 0, c, f, dp, ds);
}

void buscarReinas(int n, int i, int[] solucion,
                    boolean[] f, boolean[] dp, boolean [] ds){
    for(int j=0; j<n; j++)
        if(f[j] && dp[i-j+n-1] && ds[i+j]){
            solucion[i] = j;
            
            f[j] = false;
            dp[i-j+n-1] = false;
            ds[i+j] = false;

            if(i==n-1)
                imprimir(solucion)
            else
                buscarReinas(n, i+1, solucion, f, dp, ds);

            f[j] = true;
            dp[i-j+n-1] = true;
            ds[i+j] = true;
        }
                    }


