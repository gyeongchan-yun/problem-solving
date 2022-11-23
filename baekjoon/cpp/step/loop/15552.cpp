#include<iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int number;
    cin >> number;
    int a,b;
    for (int i = 0; i < number; i++) {
        cin >> a >> b;
        cout << a + b << '\n';
    }
}