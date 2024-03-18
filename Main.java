import java.util.Scanner; //for reading keyboard input and Files
import java.io.BufferedReader; //Fast way to read large files and other data streams
import java.io.FileReader; //used when using BufferedReader to read a File
import java.io.BufferedWriter; //Fast way to write large files and other data streams
import java.io.FileWriter; //used when using BufferedWriter to write a File
import java.io.IOException; //Exception that can be thrown by BufferedReader and BufferedWriter
import java.util.ArrayList;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JRadioButton;
import javax.swing.ButtonGroup;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import javax.swing.JTextField;
import javax.swing.JLabel;
import java.awt.BorderLayout;

//declare instance variables


/**
 * Write a description of class main here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Main
{
    JFrame mainFrame;
    JPanel mainPanel;
    JButton convertButton;
    List<String> conversionOptions;
    List<JRadioButton> radioButtons;
    ButtonGroup buttonGroup;
    JTextField userEntry;
    JLabel resultText;
    Boolean CN;
    public Main(){
        mainFrame = new JFrame("CEFI");
        mainPanel = new JPanel();
        convertButton = new JButton("Convert");
        convertButton.addActionListener(this);
        conversionOptions = setConversionOptions();
        buttonGroup = new ButtonGroup();
        radioButtons = buildRadioButtons();
        userEntry = new JTextField();
        resultText = new JLabel();
    }
    public static void main(String[] args){
        ArrayList<String[]> cefiScore5to11 = new ArrayList<String[]>();
        try {
            cefiScore5to11 = readDataFromFile("CEFItableS5to11.csv");
            System.out.println("Data successfully read");
        } catch (IOException e) {
            System.out.println("An error occurred: " + e);
        }
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                gui.createAndShowGUI();
            }
        });
        int[] ans = questionaire(cefiScore5to11);
        //int AT = pass;
    }
    public static int[] questionaire(ArrayList<String[]> a){
        //0AT,1ER,2FX,3IC,4IT,5OG,6FL,7SM,8WM,9CI,10NI,11PI,12ommited
        int[] ans = new int[13];
        int[][] catQ = {{2,10,20,24,25,43,55,61,74,79,90,96},
                        {9,11,41,46,63,67,72,78,80},
                        {6,40,45,59,66,87,98},
                        {0,18,31,37,48,69,73,91,95,97},
                        {15,29,38,39,54,57,64,77,83,92},
                        {4,12,17,26,33,51,62,75,82,88},
                        {8,14,21,27,34,49,58,70,85,89,99},
                        {5,13,16,28,36,47,52,68,81,93},
                        {3,7,22,25,30,42,50,56,71,84,86},
                        {9,11,21,34,27,89,40,66,43,55,69,91,79,90,85,99}};
        int[] flip = {3,17,18,22,23,32,39,41,42,45,46,47,48,50,53,58,64,67,68,70,73,74,77,84,87,92,93,94};
        int temAns = -1;
        int[] raw = new int[100];
        for(int i =1;i<101;i++){
            switch (a.get(i)[1]) {
                case "N":
                    temAns = 0;
                    break;
                case "R":
                    temAns = 1;
                    break;
                case "S":
                    temAns = 2;
                    break;
                case "O":
                    temAns = 3;
                    break;
                case "V":
                    temAns = 4;
                    break;
                case "A":
                    temAns = 5;
                    break;
                case "":
                    temAns = -1;
                    ans[12]++;
                    break;
                default:
                    temAns = -1;
                    break;
            }
            if (flip.contains(i)) {
                temAns = 5 - temAns;
            }
            if (temAns < 5 && temAns > 0) {
                raw[i] = temAns;
            }
        }
        temAns = 0;
        for(int j=0;j<12;j++){
            if(j!=9&&j!=11){
                for(int k = 0; k<catQ[j].length;k++){
                    ans[j]+=raw[catQ[j][k]];
                }
            }else if(j==9){
                for(int k = 0; k<catQ[9].length;k+=2){
                    temAns = Math.abs(raw[catQ[9][k]]-raw[catQ[9][k+1]]);
                    if(temAns<=1){
                        continue;
                    }else{
                        ans[9] += temAns;
                        temAns = 0;
                    }
                }
            } else if (j==11) {
                ans[11] = 50-ans[11];

            }
        }
        return ans;
    }
    public static int score(int score, int cat, ArrayList<String[]> cefi,boolean percent){
        //0cat,1percentile,2score,3Raw standard,4AT,5ER,6FX,7IC,8it,og,pl,sm,wm
        for(int i = 0; i<cefi.size();i++){
            if(Integer.parseInt(cefi.get(i)[cat])==score){
                if(percent){
                    return Integer.parseInt(cefi.get(i)[1]);
                }else{
                    return Integer.parseInt(cefi.get(i)[2]);
                }
            }
        }
        return 0;
    }
    public static ArrayList<String[]> readDataFromFile(String filename) throws IOException {
        FileReader file = new FileReader(filename);
        BufferedReader myFile = new BufferedReader(file);

        ArrayList<String[]> csvdata = new ArrayList<String[]>();
        String[] row;
        String line = myFile.readLine();
        while (line != null) {
            row = line.split(",");
            csvdata.add(row);
            line = myFile.readLine();
        }
        myFile.close();
        return csvdata;
    }
    public static void writeDataToFile(ArrayList<String[]> csvdata, String filename) throws IOException {
        FileWriter file = new FileWriter(filename);
        BufferedWriter myFile = new BufferedWriter(file);
        for (String[] row : csvdata) {
            myFile.write(String.join(",", row) + "\n");
        }
        myFile.close();
    }
    private ArrayList buildRadioButtons() {
        ArrayList<JRadioButton> buttons = new ArrayList();
        for (String conversionOption: conversionOptions)
        {
            JRadioButton button = new JRadioButton(conversionOption);
            buttons.add(button);
            buttonGroup.add(button);
        }
        return buttons;
    }

    /*
    the getSelectedButton() method returns a reference to the button that is currently selected
    that way we can check which button is selected when doing a conversion.
  */
    public JRadioButton getSelectedButton() {
        for (JRadioButton rbutton: radioButtons)
        {
            if (rbutton.isSelected())
                return rbutton;
        }
        //if no radio button is selected
        return null;
    }
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private void createAndShowGUI() {
        //Create and set up the window.
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Size and display the window.
        mainFrame.setSize(400,600);
        mainFrame.setVisible(true);
    }
    /*
        this method is called when the convertButton is clicked.
     */
    public void actionPerformed(ActionEvent e) {
        try{
            doConversion();
        }
        catch(Exception ex)
        {
            resultText.setText("");
            userEntry.setText("");
        }

    }
    /*
    This method returns a list of the conversion options that will be implemented.
    
    The list of option names is used to build JRadioButtons in the GUI
    
    and is the option names are also used in the doConversion() method to identify
    
    which conversion to perform.
     */
    public List setConversionOptions()
    {
//0cat,1percentile,2score,3Raw standard,4AT,5ER,6FX,7IC,8it,og,pl,sm,wm

        List menuOfOptions =  Arrays.asList(
                "1. Raw Score",

                "2. AT",

                "3. ER",

                "4. FX",

                "5. IC",

                "6. IT",

                "7. OG",

                "8. PL",

                "9. SM",

                "10. WM",

                "11. CI",

                "12. NI",

                "13. PI",

                "14. Ave"
        );
        return menuOfOptions;
    }
    public void doConversion()
    {
        int optionNum = setConversionOptions().indexOf(getSelectedButton().getText());

        String[] unit1 = {"Celsius","Fahrenheit","Feet","Meters","Ounces","Mililiters","Pounds","Kilograms","Pascals","Atmospheres"};

        String[] unit2 = {"Fahrenheit","Celsius","Meters","Feet","Mililiters","Ounces","Kilograms","Pounds","Atmospheres","Pascals"};

        String[] units = {"Degrees ","Degrees ","","","","","","","",""};
        List<IntegerFunction> conversions = new ArrayList<IntegerFunction>(10);

        conversions.add(score());

        conversions.add(x->(double)((x-32)*(5.0/9.0)));

        conversions.add(x->(double)(x/3.28084));

        conversions.add(x->(double)(x*3.28084));

        conversions.add(x->(double)(x*29.5735));

        conversions.add(x->(double)(x/29.5735));

        conversions.add(x->(double)(x*0.453592));

        conversions.add(x->(double)(x/0.453592));

        conversions.add(x->(double)(x/101300));

        conversions.add(x->(double)(x*101300));

        String userText = userEntry.getText();

        double u1 = Double.parseDouble(userText);

        resultText.setText(u1+" "+units[optionNum]+unit1[optionNum]+" is "+conversions.get(optionNum).apply(u1)+" "+units[optionNum]+unit2[optionNum]);

        //you can also include html code to change the display of the text.  Try commenting out (adding // in front of) the line above, and un-commenting (removing the //) the line below.
        //resultText.setText(" degrees celsius is  degrees fahrenheit");
    }
}
