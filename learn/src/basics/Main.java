package basics;

import org.w3c.dom.ls.LSOutput;

public class Main {
    // methode oder funktion
    public static void main(String[] args){
        //  neues Obejekt Haus mit name meinHaus
        Haus meinHaus = new Haus();
        // definition von dach
        meinHaus.dach = 7;

        System.out.println(meinHaus.dach);
    }

}
