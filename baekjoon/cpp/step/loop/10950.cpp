#include<iostream>
using namespace std;

int main() {
    int number;
    cin >> number;

    int count = 0;
    int a, b;
    while (count < number) {
        cin >> a >> b;
        cout << a + b << endl;
        count++;
    }
}