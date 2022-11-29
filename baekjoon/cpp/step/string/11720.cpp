#include<iostream>
using namespace std;

int main() {
    int N;
    int sum = 0;
    cin >> N;
    char str[N];
    cin >> str;
    for (int j = 0; j < N; j++) {
        sum += (int(str[j]) - 48);
    }
    cout << sum << endl;
}