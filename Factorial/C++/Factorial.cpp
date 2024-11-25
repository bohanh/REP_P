#include <algorithm>
#include <string>
#include <iostream>

long long int factorial(long long int n)
{
   long long int r = 1;
   while(1 < n) {
       r *= n--;
   }
   return r;
}

int main( ) {
   int number = 10;
   std::cout << factorial(number) << std::endl;
   return 0 ;
}