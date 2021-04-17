#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cout.tie(nullptr);

    string input;

    getline(cin, input);

    cout << "hello, " << input << "\n";
}