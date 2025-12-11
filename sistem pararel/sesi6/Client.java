import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            // Menghubungkan ke registry RMI di localhost
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);

            // Lookup objek remote
            PesanTiket stub = (PesanTiket) registry.lookup("TiketService");

            // Input dari pengguna
            Scanner sc = new Scanner(System.in);
            System.out.print("Masukkan nama pemesan: ");
            String nama = sc.nextLine();
            System.out.print("Masukkan tujuan: ");
            String tujuan = sc.nextLine();

            // Memanggil method remote
            String respon = stub.pesanTiket(nama, tujuan);
            System.out.println("Respon dari server: " + respon);

        } catch (Exception e) {
            System.err.println("Client error: " + e);
            e.printStackTrace();
        }
    }
}
