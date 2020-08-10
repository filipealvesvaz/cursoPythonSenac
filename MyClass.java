class MyClass {
  public static void main(String[ ] args) {
    System.out.println(reverse("computer"));
  }

 public static String reverse(String s){
   String ret = "";
   for(int k=0; k < s.length(); k +=2){
      ret = s.charAt(k) + ret;
   }
   return ret;
 }
  
}