#include<iostream>
using namespace std;

int main() {
    int student_id_arr[30] = {0, };
    int submit_id_arr[28] = {0, };
    for (int i = 0; i < 28; i++) {
        cin >> submit_id_arr[i];
        student_id_arr[submit_id_arr[i]-1] = submit_id_arr[i];
    }
    for (int i = 0; i < 30; i++) {
        if (student_id_arr[i] == 0) {
            cout << i+1 << endl;
        }
    }
}