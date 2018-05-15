package reader;
import org.nfctools.mf.card.MfCard;
import org.nfctools.mf.MfCardListener;

public class ReadCard {
	
	MfCardListener listener = new MfCardListener() {
		public void detect(MfCard card) {
			System.out.println(card.toString()); //Card Information
		}
	};
	
	ping(listener);

	private static void ping(MfCardListener listener) {
		NFCReader nfcr;
		nfcr.start();
		nfcr.ping(listener);
		System.in.read(); //Wait for input to exit
		nfcr.end(); 
		
	}
	
}
