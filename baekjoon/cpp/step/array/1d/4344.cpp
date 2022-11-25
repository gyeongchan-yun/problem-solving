#include<iostream>
using namespace std;

int main() {
    int num;
    int student_num;
    double average, great_student_num;

    cin >> num;
    
    for (int i = 0; i < num; i++) {
        average = 0;
        great_student_num = 0;
        cin >> student_num;
        int score_arr[student_num] = {0, };
        for (int j = 0; j < student_num; j++) {
            cin >> score_arr[j];
            average += score_arr[j];
        }
        average /= (double)student_num;
        for (int k = 0; k < student_num; k++) {
            if (score_arr[k] > average) {
                great_student_num++;
            }
        }
        cout << fixed;
        cout.precision(3);
        cout << (great_student_num / (double)student_num) * 100 << "%" << endl;
    }
}