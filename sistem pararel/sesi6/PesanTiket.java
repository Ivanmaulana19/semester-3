import java.rmi.Remote;
import java.rmi.RemoteException;

// Interface remote (kontrak antara client dan server)
public interface PesanTiket extends Remote {
    String pesanTiket(String nama, String tujuan) throws RemoteException;
}
