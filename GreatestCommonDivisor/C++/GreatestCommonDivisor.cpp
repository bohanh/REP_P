#include <iostream>

// Custom gcd function
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    std::cout << "The greatest common divisor of 12 and 18 is " << gcd(12, 18) << " !\n";
    return 0;
}
