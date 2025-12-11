import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

// Implementasi dari interface PesanTiket
public class PesanTiketImpl extends UnicastRemoteObject implements PesanTiket {
    protected PesanTiketImpl() throws RemoteException {
        super();
    }

    @Override
    public String pesanTiket(String nama, String tujuan) throws RemoteException {
        return "Tiket atas nama " + nama + " dengan tujuan " + tujuan + " berhasil dipesan!";
    }
}
