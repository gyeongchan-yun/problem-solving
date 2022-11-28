#include<iostream>
using namespace std;

int d_func(int num) {
    int ret = num;
    while (num > 0) {
        ret += (num % 10);
        num /= 10;
    }
    return ret;
}

int main() {
    int N = 10000;
    int a[N+1] = {0, };
    int d_result = 0;
    for (int i = 1; i <= N; i++) {
        d_result = d_func(i);
        if (d_result <= N) {
            a[d_result] = 1;
        }
    }
    for (int i = 1; i <= N; i++) {
        if (a[i] != 1) {
            cout << i << endl;
        }
    }
}