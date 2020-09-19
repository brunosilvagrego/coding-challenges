#include <iostream>

using namespace std;


int division(int a, int b)
{
    int result = 0;

    for (int i = b; i <= a; i += b)
    {
        result++;
    }

    return result;
}


int main ()
{
    cout << division(2, 3) << endl;
    cout << division(4, 3) << endl;
    cout << division(6, 3) << endl;
    cout << division(8, 3) << endl;
    cout << division(32, 3) << "\n" << endl;

    return 0;
}
