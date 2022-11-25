#include<iostream>
using namespace std;

int main() {
    int N, X;
    cin >> N >> X;
    int num_arr[N] = {0, };
    for (int i = 0; i < N; i++) {
        cin >> num_arr[i];
    }
    for (int i = 0; i < N; i++) {
        if (num_arr[i] < X) {
            cout << num_arr[i] << " ";
        }
    }
    cout << endl;
}