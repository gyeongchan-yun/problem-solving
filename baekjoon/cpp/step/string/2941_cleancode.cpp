#include<iostream>
using namespace std;

int main() {
    string croatia_alphabet[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    string sentence = "";
    cin >> sentence;
    int idx = 0;
    for (int i = 0; i < 8; i++) {
        while (true) {
            idx = sentence.find(croatia_alphabet[i]);
            if (idx == string::npos) {
                break;
            }
            sentence.replace(idx, croatia_alphabet[i].length(), "#");
        }
    }
    cout << sentence.length() << endl;
}