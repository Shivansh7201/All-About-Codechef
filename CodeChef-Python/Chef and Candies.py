#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int x, y;
        cin >> x >> y;
        if (x < y) cout << 0 << "\n";
        else if ((x-y)%4 == 0) cout << (x-y)/4 << "\n";
        else cout << ((x-y)/4)+1 << "\n";
    }
    return 0;
}
