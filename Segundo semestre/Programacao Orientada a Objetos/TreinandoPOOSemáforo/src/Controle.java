import java.util.Scanner;

public class Controle {
    public static void main(String[] args) {
        System.out.println("Escolha uma cor para o semáforo: ");
        System.out.println("0 - Verde, 1 - Amarelo, 2 - Vermelho");
        System.out.println("Opção: ");
        Scanner in = new Scanner(System.in);
        int color = Integer.parseInt(in.nextLine());

        Semaforo semaforo = new Semaforo();
        System.out.println(semaforo.showColor());

        for (int i = 0; i < 10; i++) {
            semaforo.changeNextColor();
            System.out.println(semaforo.showColor());
        }

        semaforo.changeFixedColor(Semaforo.VERDE);
        System.out.println(semaforo.showColor());
    }
}
