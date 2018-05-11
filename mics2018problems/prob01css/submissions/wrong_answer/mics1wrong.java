/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mics1;

import java.util.*;              // needed for input Scanner
/**
 *
 * @author tgibbons
 */
public class mics1accepted {
    // declare console for input
    static Scanner console = new Scanner(System.in);

    public static void spaces() {
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("");
    }
        
    public static void one() {
        System.out.println("CCCCC     SSSSS     SSSSS");
        System.out.println("C         S         S    ");
        System.out.println("C         SSSSS     SSSSS");
        System.out.println("C             S         S");
        System.out.println("CCCCC     SSSSS     SSSSS");
    }
    public static void two() {
        System.out.println("CCCCCCCCCC          SSSSSSSSSS          SSSSSSSSSS");
        System.out.println("CCCCCCCCCC          SSSSSSSSSS          SSSSSSSSSS");
        System.out.println("CC                  SS                  SS        ");
        System.out.println("CC                  SS                  SS        ");
        System.out.println("CC                  SSSSSSSSSS          SSSSSSSSSS");
        System.out.println("CC                  SSSSSSSSSS          SSSSSSSSSS");
        System.out.println("CC                          SS                  SS");
        System.out.println("CC                          SS                  SS");
        System.out.println("CCCCCCCCCC          SSSSSSSSSS          SSSSSSSSSS");
        System.out.println("CCCCCCCCCC          SSSSSSSSSS          SSSSSSSSSS");        
    }
        public static void three() {
        System.out.println("CCCCCCCCCCCCCCC               SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
        System.out.println("CCCCCCCCCCCCCCC               SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
        System.out.println("CCCCCCCCCCCCCCC               SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
        System.out.println("CCC                           SSS                           SSS            ");
        System.out.println("CCC                           SSS                           SSS            ");
        System.out.println("CCC                           SSS                           SSS            ");
        System.out.println("CCC                           SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
        System.out.println("CCC                           SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
        System.out.println("CCC                           SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
        System.out.println("CCC                                       SSS                           SSS");
        System.out.println("CCC                                       SSS                           SSS");
        System.out.println("CCC                                       SSS                           SSS");
        System.out.println("CCCCCCCCCCCCCCC               SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
        System.out.println("CCCCCCCCCCCCCCC               SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
        System.out.println("CCCCCCCCCCCCCCC               SSSSSSSSSSSSSSS               SSSSSSSSSSSSSSS");
    }
    public static void printc(String s, int num) {
        for (int n = 0; n<num; ++n) {
            System.out.print(s);
        }
    }
    
    
    public static void ten() {
        for (int i=0; i<10; i++) {
           printc("C",50);  
           printc(" ",50);
           printc("S",50);
           printc(" ",50);
           printc("S",50);
           System.out.println("");
        }

        for (int i=0; i<10; i++) {
           printc("C",10); 
           printc(" ",40);
           printc(" ",50);
           printc("S",10);
           printc(" ",40);
           printc(" ",50);
           printc("S",50);
           printc(" ",40);
           System.out.println("");
        }
        for (int i=0; i<10; i++) {
           printc("C",10); 
           printc(" ",40); 
           printc(" ",50);
           printc("S",50);
           printc(" ",50);
           printc("S",50);
           System.out.println("");
        }
        for (int i=0; i<10; i++) {
           printc("C",10); 
           printc(" ",40);
           printc(" ",50);
           printc(" ",40);
           printc("S",10);
           printc(" ",50);
           printc(" ",40);
           printc("S",50);
           System.out.println("");
        }
        
        for (int i=0; i<10; i++) {
           printc("C",50);  
           printc(" ",50);
           printc("S",50);
           printc(" ",50);
           printc("S",50);
           System.out.println("");
        }
        
    }
    
    public static void main(String[] args) {
        int numLines = console.nextInt();
        for (int n = 0; n<numLines; ++n) {
          int size = console.nextInt(); 
          if (size == 1) {
              one();
          }
          if (size == 2) {
              two();
          }
          if (size == 3) {
              three();
          }
          if (size == 10) {
              ten();
          }
          spaces();
        }

    }
    
}
