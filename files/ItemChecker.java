import java.util.Random;

public class ItemChecker {

    //instance variables
    private String userText;
    private boolean checkedText;

    // costructor
    ItemChecker() {
        userText = "";
        checkedText = false;
    }

    // setter
    public void setUserText(String userText) {
        this.userText = userText;
    }

    // method required too check if the provided piece of text conforms to the rules
    // corresponding to the assigned item
    public boolean compute() {
        userText = userText.toUpperCase();// method change leters lowercase to uppercase
        // check the lenght as per format
        if (userText.length() > 13 || userText.length() < 8) {
            System.out.println("Invalid input, please try again");
            checkedText = false;
            return false;
        }
        // check the three-digit year
        char charCheck = ' ';
        int charCheckConverted;
        for (int i = 0; i <= 2; i++) {
            charCheck = userText.charAt(i);
            charCheckConverted = (int) charCheck;
            if (charCheckConverted >= 48 && charCheckConverted <= 57) {
            } else { 
                System.out.println("Invalid input, please try again");
                checkedText = false;
                return false; 
            }
        }
        // check the dash
        if (userText.charAt(3) != '-' && userText.charAt(6) != '-') {
            System.out.println("Invalid input, please try again");
            checkedText = false;
            return false;
        }
        // check the possible county/city identifiers
        String LL = userText.substring(4, 6);
        if (LL.equals("CK") || LL.equals("CE") || LL.equals("CN") || LL.equals("CW") || LL.equals("DN")
                || LL.equals("DL") || LL.equals("GY") || LL.equals("KE") || LL.equals("KK") || LL.equals("KY")
                || LL.equals("LK") || LL.equals("LD") || LL.equals("LH") || LL.equals("LM") || LL.equals("LS")
                || LL.equals("MH") || LL.equals("MN") || LL.equals("MO") || LL.equals("OY") || LL.equals("RN")
                || LL.equals("SO") || LL.equals("TY") || LL.equals("WD") || LL.equals("WH") || LL.equals("WX")
                || LL.equals("WW")) {
        } else {
            System.out.println("Invalid county/city, please try again");
            checkedText = false;
            return false;
        }
        // check if the one to six-digit sequence are numbers
        for (int i = 7; i < userText.length(); i++) {
            charCheck = userText.charAt(i);
            charCheckConverted = (int) charCheck;
            if (charCheckConverted >= 48 && charCheckConverted <= 57) {

            } else {
                System.out.println("Invalid sequence number, please try again");
                checkedText = false;
                return false;
            }
        }
        checkedText = true;
        return checkedText;
    }// end of compute

    // getter
    public String getUserText() {
        return userText;
    }

    // method to create as many items as the given number and store the items in an
    // array of String items
    public String[] securityCode(int number) {
        Random random = new Random();
        String codes[] = new String[number];

        String code = "";
        char randomizedCharacter;
        for (int j = 0; j < number; j++) {
            int randomizedNumber = (int) ((Math.random() * (9999 - 1000)) + 1000);// creating 4 random digit numbers

            code = "";
            for (int i = 0; i < 3; i++) {
                randomizedCharacter = (char) (random.nextInt(26) + 'A');// creating a random alphabet
                code = code + Character.toString(randomizedCharacter);// store the alphabets in a string
            }
            codes[j] = Integer.toString(randomizedNumber) + code;// concatenating the alphabet and numbers(converted to
                                                                 // string) and storing in the array

        }
        return codes;
    }

}
