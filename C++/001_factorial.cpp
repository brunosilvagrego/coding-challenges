#include <iostream>

using namespace std;

// NOTE: There must always be a path through a recursive function that does not involve a
//       recursive call; otherwise, the function will recurse “forever,” meaning that the function
//       will continue to call itself until the program stack is exhausted. Such functions are
//       sometimes described as containing a recursion loop. In the case of factorial, the
//       stopping condition occurs when val is 1.

// factorial of val is val * (val - 1) * (val - 2) . . . * ((val - (val - 1)) * 1)
int factorial(int val)
{
    if (val > 1)
    {
        return factorial(val-1) * val;
    }

    return 1;
}

int factorialIter(int val)
{
    int fact = 1;

    for (int i = 1; i <= val; i++)
    {
        fact = fact * i;
    }

    return fact;
}

// NOTE: The main function may not call itself.

int main()
{
    cout << "Factorial recursive:" << endl;

    for (int i = 1; i <= 9; i++)
    {
        cout << i << "! = " << factorial(i) << endl;
    }

    cout << "\nFactorial iterative:" << endl;

    for (int i = 1; i <= 9; i++)
    {
        cout << i << "! = " << factorialIter(i) << endl;
    }


	return 0;
}
