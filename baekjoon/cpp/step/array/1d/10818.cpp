#include<iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int num_arr[N] = {0, };
    for (int i = 0; i < N; i++) {
        cin >> num_arr[i];
    }
    int max = -1000000;
    int min = 1000000;
    for (int i = 0; i < N; i++) {
        if (num_arr[i] >= max) {
            max = num_arr[i];
        }
        if (num_arr[i] <= min) {
            min = num_arr[i];
        }
    }
    cout << min << " " << max << endl;
}