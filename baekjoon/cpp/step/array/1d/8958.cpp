#include<iostream>
using namespace std;

int main() {
    int num;
    string test_case;
    int score, total_score;;
    bool is_prev_correct = false;

    cin >> num;

    for (int i = 0; i < num; i++) {
        // Initialize for every test case
        total_score = 0;
        is_prev_correct = false;
        cin >> test_case;
        for (int j = 0; j < test_case.length(); j++) {
            if (is_prev_correct == false && test_case[j] == 'O') {
                is_prev_correct = true;
                score = 1;
            }
            else if (is_prev_correct == true && test_case[j] == 'O') {
                score++;
            }
            else if (test_case[j] == 'X') {
                is_prev_correct = false;
                score = 0;
            }
            else {
                cout << "[ERROR] Unexpected case" << endl;
            }
            total_score += score;
        }
        cout << total_score << endl;
    }
}