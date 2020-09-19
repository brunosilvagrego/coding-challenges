#include <iostream>

using namespace std;

void fibIter (int n)
{
    int t1 = 0, t2 = 1, nextTerm = 0;

    for (int i = 1; i <= n; ++i)
    {
        // Prints the first two terms.
        if(i == 1)
        {
            cout << t1 << " ";
        }
        else if(i == 2)
        {
            cout << t2 << " ";
        }
        else
        {
            nextTerm = t1 + t2;
            t1 = t2;
            t2 = nextTerm;
            cout << nextTerm << " ";
        }
    }
}

int fib(int n)
{
    if (n <= 1)
    {
        return n;
    }

    return fib(n-1) + fib(n-2);
}

int main ()
{
    int n = 20;

    cout << "Fibonacci iterative:" << endl;
    fibIter(n);
    cout << endl;

    cout << "Fibonacci recursive:" << endl;
    for (int i = 0; i < n; ++i)
    {
        cout << fib(i) << " ";
    }

    cout << endl;

    return 0;
}
