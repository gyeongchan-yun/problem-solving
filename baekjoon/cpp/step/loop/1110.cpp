#include<iostream>
using namespace std;

int main() {
    int num, cycle = 0;
    cin >> num;
    int a, b, c;
    c = num;
    while (true) {
        a = c / 10;
        b = c % 10;
        c = b * 10 + ((a + b) % 10);
        cycle++;
        if (c == num) {
            break;
        }
    }
    cout << cycle << endl;
}