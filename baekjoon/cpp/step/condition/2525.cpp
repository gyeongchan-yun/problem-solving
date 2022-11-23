#include<iostream>
using namespace std;

int main() {
    int hour, min, cook_time;
    cin >> hour >> min >> cook_time;
    int add_hour;
    add_hour = (min + cook_time) / 60;
    hour += add_hour;
    if (hour >= 24) {
        hour -= 24;
    }
    min = (min + cook_time) % 60;
    cout << hour << " " << min << endl;
}