#include<iostream>
using namespace std;

bool is_hannumber(int num) {
    int d, digit = 0;
    int iter = num;
    while (iter > 0) {
        iter /= 10;
        digit++;
    }
    int num_arr[digit] = {0, };
    for (int i = 0; i < digit; i++) {
        num_arr[i] = num % 10;
        num /= 10;
    }
    for (int i = 0; i < digit; i++) {
        if (i == 0) {
            d = num_arr[i+1] - num_arr[i];
        }
        if (i+1 < digit && num_arr[i+1] - num_arr[i] != d) {
            return false;
        }
    }
    return true;
}

int main() {
    int N;
    int count = 0;
    cin >> N;
    for (int i = 1; i < N+1; i++) {
        if (is_hannumber(i) == true) {
            count++;
        }
    }
    cout << count << endl;
}