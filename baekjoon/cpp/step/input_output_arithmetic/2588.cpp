#include<iostream>
#include<string>
using namespace std;

int main() {
    int a, b;
    cin >> a;
    cin >> b;
    string str_b = to_string(b);
    for (int i = 0; i < 3; i++) {
        cout << a * (str_b[2-i] - '0') << endl;
    }
    cout << a * b << endl;
}