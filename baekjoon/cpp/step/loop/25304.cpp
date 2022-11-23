#include<iostream>
using namespace std;

int main() {
    int total_price, total_num;
    cin >> total_price >> total_num;
    int price, num;
    int total_true_price = 0;
    for (int i = 0; i < total_num; i++) {
        cin >> price >> num;
        total_true_price += (price * num);
    }
    if (total_price == total_true_price) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}