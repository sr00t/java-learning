package Aufgaben;

public class mycats {
    public static void main(String[] args){
        katze dieKatze = new katze();
        dieKatze.atler = 1;
        dieKatze.gewicht = 5;
        System.out.println("meine erste Katze ist " + dieKatze.atler + " alt und hat " + dieKatze.gewicht + "kg gewischt");
    }
}
