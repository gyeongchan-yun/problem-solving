#include<iostream>
#include<iomanip>
using namespace std;

int main() {
    int a, b;
    double result;
    cin >> a >> b;
    result = a / (double) b;
    cout.precision(11);
    cout << result << endl;
}