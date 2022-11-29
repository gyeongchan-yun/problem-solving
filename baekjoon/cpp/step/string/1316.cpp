#include<iostream>
#include<string>
using namespace std;

int main() {
    int N;
    int count = 0;
    string appear_str;
    bool is_group;
    cin >> N;
    string input_word;
    for (int i = 0; i < N; i++) {
        input_word = "";
        appear_str = "";
        is_group = true;

        cin >> input_word;

        for (int j = 0; j < input_word.size(); j++) {
            if (appear_str.find(input_word[j]) == string::npos) {
                appear_str += input_word[j];
            } else if (appear_str[appear_str.size()-1] != input_word[j]) {
                is_group = false;
                break;
            }
        }
        if (is_group) {
            count++;
        }
    }
    cout << count << endl;
}