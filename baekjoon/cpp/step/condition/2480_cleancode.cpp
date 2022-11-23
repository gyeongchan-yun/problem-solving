#include<iostream>
using namespace std;

int max(int a, int b, int c) {
    int max = -1;
    if (a > max) {
        max = a;
    }
    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }
    return max;
}

int main() {
    int x,y,z;
    int max_num = -1;
    cin >> x >> y >> z;

    if (x == y && y == z) {
        cout << 10000 + x * 1000 << endl;
    }
    else if (x == y || x == z) {
        cout << 1000 + x * 100 << endl;
    }
    else if (y ==z) {
        cout << 1000 + y * 100 << endl;
    }
    else {
        max_num = max(x, y, z);
        cout << max_num * 100 << endl;
    }
}