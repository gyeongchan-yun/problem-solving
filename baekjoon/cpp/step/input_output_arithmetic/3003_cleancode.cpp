// Reference: https://velog.io/@kkily55/%EB%B0%B1%EC%A4%80-3003-%ED%82%B9-%ED%80%B8-%EB%A3%A9-%EB%B9%84%EC%88%8D-%EB%82%98%EC%9D%B4%ED%8A%B8-%ED%8F%B0c
#include<iostream>
using namespace std;

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n[6];
    int chess[6] = {1,1,2,2,2,8};

    for (int i = 0; i < 6; i++) {
        cin >> n[i];
        cout << chess[i] - n[i] << " ";
    }
    cout << endl;
}