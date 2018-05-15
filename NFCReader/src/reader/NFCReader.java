package reader;
import org.nfctools.spi.acs.AcsTerminal;
import org.nfctools.spi.acs.Acr122ReaderWriter;
import org.nfctools.mf.mfCardListener;
import otg.nfctools.utils.CardTerminalUtils;
import javax.smartcardio.cardTerminal

public class NFCReader extends AcsTerminal {

	private Acr122ReaderWriter rw;
	
	public NFCReader() {
		CardTerminal term = CardTerminalUtils.getTerminalByName("ACR122");
		setCardTerminal(term);
		rw = new Acr122ReaderWriter(this);
	}
	
	public void listen(MfCardListener listener) {
		rw.setCardListener(listener);
	}

	public void start() {
		super.open();
	}
	
	public void end() {
		rw.removeCardListener();
		super.end();
	}
	
}
