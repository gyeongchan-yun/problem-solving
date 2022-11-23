#include<iostream>
using namespace std;

int main() {
    int num;
    cin >> num;
    int a,b;
    for (int i = 1; i <= num; i++) {
        cin >> a >> b;
        cout << "Case #" << i << ": " << a << " + " << b << " = " << a + b << endl;
    }
}