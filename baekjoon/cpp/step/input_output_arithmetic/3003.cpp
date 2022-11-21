#include<iostream>
using namespace std;

int main() {
    int k, q, l, b, n, p;
    int piece[6] = {1, 1, 2, 2, 2, 8};
    cin >> k >> q >> l >> b >> n >> p;
    piece[0] -= k;
    piece[1] -= q;
    piece[2] -= l;
    piece[3] -= b;
    piece[4] -= n;
    piece[5] -= p;
    for (int i = 0 ; i < 6; i++) {
        cout << piece[i] << " ";
    }
    cout << endl;
}