#include<iostream>
using namespace std;

int main() {
    string croatia_alphabet[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    string sentence, window_word = "";
    int count = 0;
    cin >> sentence;
    int i = 0;
    bool is_croatia = false;
    while (i < sentence.size()) {
        window_word += sentence[i];
        window_word += sentence[i+1];
        if (window_word.compare("dz") == 0 && i+2 < sentence.size()) {
            window_word += sentence[i+2];
        }
        for (int j = 0; j < 8; j++) {
            if (window_word.compare(croatia_alphabet[j]) == 0) {
                is_croatia = true;
                count++;
                i = i + window_word.size();
                break;
            }
        }
        window_word = "";
        if (!is_croatia) {
            count++;
            i++;
        } else {
            is_croatia = false;
        }
    }
    cout << count << endl;
}