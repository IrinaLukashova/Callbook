import java.util.Arrays;

public class program {
    public static void main(String[] args) {
        Human human1 = new Human("Olga");
        Human human2 = new Human("Konstantin");
        Human human3 = new Human("Saveliy");
        Human human4 = new Human("Vitaliy");

        Market market = new Market();

        market.acceptToMarket(human1);
        market.acceptToMarket(human2);
        market.update();
        market.acceptToMarket(human3);
        market.acceptToMarket(human4);
        market.update();
    }
}
