public class Human {
    String name;
    int age;
    double height;
    int leetCode_rank;
}
class Human1 extends Human{
    public Human1(String name, double height, int leetCode, int age){
        this.name=name;
        this.age=age;
        this.height=height;
        this.leetCode_rank=leetCode;
    }
    void hired(Human2 human2){
        System.out.println("Name is :"+name+", Height is :"+height+", Age is :"+age+", LeetCode rank is :"+leetCode_rank+" ");
        if(human2.leetCode_rank>this.leetCode_rank){
            System.out.println("The company allotted is: Google and congratulations to you");
        }
        else {
            System.out.println("The company allotted is: TCS , good but you can try for other companies too");
        }
    }
}
class Human2 extends Human{
    public Human2(String name, double height, int leetCode, int age){
        this.name=name;
        this.age=age;
        this.height=height;
        this.leetCode_rank=leetCode;
    }
    void placed(Human1 human1)
    {
        System.out.println("Name is :"+name+", Height is :"+height+", Age is :"+age+", LeetCode rank is :"+leetCode_rank+" ");
        if(human1.leetCode_rank>this.leetCode_rank)
    System.out.println("The company allotted is: Google and congratulations to you");
else {
    System.out.println("The company allotted is: TCS , good but you can try for other companies too");
}
    }
}
class Main{
    public static void main(String[] args) {
        Human1 human1=new Human1("Aditi Bagaddeo",5.5,19,20);
        Human2 human2=new Human2("Ashish Saha",5.7,25,21);
        human1.placed(human2);
        System.out.println();
        System.out.println("*******");
        System.out.println();
        human2.placed(human1);
    }
}
