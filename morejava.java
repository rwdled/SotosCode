import java.util.ArrayList;

public class morejava {
    public static void main(String[] args){
        var dec2ben = new ArrayList<Integer>();
        int num = 10;
        while (num > 0){
            dec2ben.add(num % 2);
            num = num / 2;
            System.out.println(num);
        }
        for (int i = dec2ben.size() - 1; i >= 0; i--){
            System.out.print(dec2ben.get(i));
        }

    }
}
