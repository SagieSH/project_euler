#include <iostream>



int main() {
    size_t a = 1;
    size_t b = 2;
    size_t c = 3;
    size_t sum = 2;

    while (c < 4000000 ) {
        if (c % 2 == 0) {
            sum += c;
        }

        a = b;
        b = c;
        c = a + b;
    }

    // The answer is '4613732'
    std::cout << sum << std::endl;
}
