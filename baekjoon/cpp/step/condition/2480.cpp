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
    cin >> x >> y >> z;
    int equal_count = 0;
    int equal_val = -1;
    int max_num = -1;
    if (x == y) {
        equal_count += 1;
        equal_val = x;
    }
    if (y == z) {
        equal_count += 1;
        equal_val = y;
    }
    if (x == z) {
        equal_count += 1;
        equal_val = z;
    }

    if (equal_count == 0) {
        max_num = max(x, y, z);
        cout << max_num * 100 << endl;
    }
    else if (equal_count == 1) {
        cout << 1000 + equal_val * 100 << endl;
    }
    else if (equal_count == 3) {
        cout << 10000 + x * 1000 << endl;
    }
}