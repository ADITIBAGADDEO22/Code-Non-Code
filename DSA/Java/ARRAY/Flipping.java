package com.company.Arrays;

import java.util.Arrays;

public class Flipping {
    public static void main(String[] args) {
        int [][]image={{1,1,0,1},{1,0,1,1},{0,0,1,1}};
        for (int i=0;i<image.length;i++){
            int k=image[i].length/2;
            int m=0;
            for (int j=image[i].length-1;j>=k;j--){
                    int temp=image[i][m];
                    image[i][m]=image[i][j];
                    image[i][j]=temp;
                    m++;
            }
        }
       for (int i=0;i<image.length;i++){
           for (int j=0;j<image[i].length;j++){
               if(image[i][j]==0)
                   image[i][j]=1;
               else
                   image[i][j]=0;

               System.out.print(image[i][j]);
           }
           System.out.println();
       }

    }
}
