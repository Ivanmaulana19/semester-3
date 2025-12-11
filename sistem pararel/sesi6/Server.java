import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    public static void main(String[] args) {
        try {
            // Membuat instance objek remote
            PesanTiketImpl obj = new PesanTiketImpl();

            // Membuat registry RMI di port 1099
            Registry registry = LocateRegistry.createRegistry(1099);

            // Bind objek ke registry
            registry.rebind("TiketService", obj);

            System.out.println("Server siap dan berjalan di port 1099...");
        } catch (Exception e) {
            System.err.println("Server error: " + e);
            e.printStackTrace();
        }
    }
}
