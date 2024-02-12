#include <iostream>

int main() {
    size_t sum = 0;
    for (size_t i = 0; i < 1000; i++) {
        if ((i % 3 == 0) || (i % 5 == 0)) {
            sum += i;
        }
    }

    // The answer is '233168'
    std::cout << sum << std::endl;
}
