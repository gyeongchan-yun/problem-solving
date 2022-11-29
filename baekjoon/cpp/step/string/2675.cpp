#include<iostream>
#include<string>
using namespace std;

int main() {
    int T, R;
    string S, result;
    cin >> T;
    for (int i = 0; i < T; i++) {
        S = "";
        result = "";
        cin >> R >> S;
        for (int j = 0; j < S.size(); j++) {
            for (int k = 0; k < R; k++) {
                result += S[j];
            }
        }
        cout << result << endl;
    }
}