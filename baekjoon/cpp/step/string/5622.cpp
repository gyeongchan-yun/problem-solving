#include<iostream>
using namespace std;

int main() {
    string word;
    int time = 0;
    int number;
    cin >> word;
    for (int i = 0; i < word.size(); i++) {
        if (word[i] == 'S') {
            number = 7;
        } else if (word[i] == 'V') { 
            number = 8;
        } else if (word[i] == 'Y' || word[i] == 'Z') {
            number = 9;
        } else {
            number = (word[i] - 65) / 3 + 2;
        }
        time += (2 + (number - 1));
    }
    cout << time << endl;
}