#include<iostream>
using namespace std;

int reverse(string str) {
    int result;
    int digit = 100; // 세 자리수라는 가정이 있기 때문에
    for (int i = str.size() - 1; i >= 0; i--) {
        result += (str[i] - 48) * digit;
        digit /= 10;
    }
    return result;
}

int main() {
    string first, second;
    int rev_first, rev_second;
    cin >> first >> second;
    rev_first = reverse(first);
    rev_second = reverse(second);
    if (rev_first > rev_second) { 
        cout << rev_first << endl;
    } else {
        cout << rev_second << endl;
    }
}