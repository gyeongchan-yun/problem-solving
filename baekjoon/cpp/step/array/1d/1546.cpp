#include<iostream>
#include<iomanip>
using namespace std;


int main() {
    int N;
    cin >> N;
    int scores[N] = {0, };
    double max = -1;
    for (int i = 0; i < N; i++) {
        cin >> scores[i];
        if (scores[i] > max) {
            max = scores[i];
        }
    }
    double sum = 0;
    for (int i = 0; i < N; i++) {
        sum += (scores[i]/max) * 100;
    }
    cout << setprecision(15) << sum/(double)N << endl;
}