#include<iostream>
using namespace std;

int main() {
    int num, target_val;
    cin >> num;
    int integer_arr[num] = {0, };
    for (int i = 0; i < num; i++) {
        cin >> integer_arr[i];
    }
    cin >> target_val;
    int count = 0;
    for (int i = 0; i < num; i++) {
        if (integer_arr[i] == target_val) {
            count++;
        }
    }
    cout << count << endl;
}