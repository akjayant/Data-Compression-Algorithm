# Data-Compression-Algorithm
It is python 3.5 implementation of LZW lossless compression algorithm as given in pseudocode on geeksforgeeks.org - 
  
    PSEUDOCODE for LZW Algorithm
         Initialize table with single character strings
         P = first input character
         WHILE not end of input stream
             C = next input character
              IF P + C is in the string table
                 P = P + C
              ELSE
                output the code for P
      	  add P + C to the string table
                P = C
         END WHILE
         output code for P 
         
