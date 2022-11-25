#include<iostream>
using namespace std;

int main() {
    int arr[9] = {0, };
    int max = -1;
    int index = 0;
    for (int i = 0; i < 9; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < 9; i++) {
        if (arr[i] > max) {
            max = arr[i];
            index = i+1;
        }
    }
    cout << max << endl;
    cout << index << endl;
}