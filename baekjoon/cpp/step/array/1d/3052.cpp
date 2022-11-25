#include<iostream>
using namespace std;

int main() {
    int N = 10;
    int X = 42;
    int num_arr[N] = {0, };
    int remainder_arr[X+1] = {0, };
    int remainder = 0;
    for (int i = 0; i < N; i++) {
        cin >> num_arr[i];
        remainder = num_arr[i] % X;
        remainder_arr[remainder] = 1;
    }
    int sum = 0;
    for (int i = 0; i < X+1; i++) {
        sum += remainder_arr[i];
    }
    cout << sum << endl;
}