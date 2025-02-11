import java.util.ArrayList;

class javatest{
    public static void main(String[] args){
    
      int[] studentGrades = {100,90,60,70,20,4,60,90,100,10};
      
      if (studentGrades.length == 0){
        System.out.println("No grades available");
      }
       int numfailing = 0;
       int numPassing = 0;
      for (int i = 0; i < studentGrades.length; i++){
        if (studentGrades[i] < 50){
          numfailing++;
        }
        else{
          numPassing++;
        }
        System.out.println("Number of failing grades: " + numfailing);
        System.out.println("Number of passing grades: " + numPassing);
      }
        
    }


}