import java.util.Random;

public class genUID {

    public static void main(String[] args) {
        char[] UID;
        UID = new char[8];
        Random rand = new Random();

        for ( int i = 0; i <8; i++ ) {
            int val = rand.nextInt(16);
            switch(val) {
                case 10: UID[i] = 'A';
                         break;
                case 11: UID[i] = 'B';
                         break;
                case 12: UID[i] = 'C';
                    break;
                case 13: UID[i] = 'D';
                    break;
                case 14: UID[i] = 'E';
                    break;
                case 15: UID[i] = 'F';
                    break;
                default : UID[i] = (char) (val + '0');
                          break;

            }
        }
        System.out.println(UID);
    }
}
