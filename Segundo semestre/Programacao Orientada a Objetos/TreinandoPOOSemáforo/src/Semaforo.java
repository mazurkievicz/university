public class Semaforo {
    private int color;
    public static final int VERDE = 0;
    public static final int AMARELO = 1;
    public static final int VERMELHO = 2;

    public Semaforo() {
        color = VERMELHO;
    }


    public void changeNextColor() {
        color = color < VERMELHO ? color + 1 : VERDE;

    }

    public void changeFixedColor(int nextColor) {
        if (color != VERDE && color != AMARELO && color != VERMELHO) {
            System.err.println("Cor inválida!");
            return;
        }

        this.color = nextColor;

    }

    public int showColor(){
        return color;
    }

    public Semaforo(int color) {
        this.color = color;
    }
}


