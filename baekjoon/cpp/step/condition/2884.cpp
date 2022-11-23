#include<iostream>
using namespace std;

int main() {
    int hour, min;
    cin >> hour >> min;
    if (min < 45) {
        if (hour == 0) {
            hour = 24;
        }
        min += 15;
        hour -= 1;
    } else {
        min -= 45;
    }
    cout << hour << " " << min << endl;
}