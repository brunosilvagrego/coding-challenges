#include <iostream>
#include <string>

using namespace std;


void palindrome (string str)
{
    char temp;
    string comp = str;
    int n = str.length();

    // Reverse string
    for (int i = 0; i < n / 2; i++)
    {
        temp = comp[i];
        comp[i] = comp[n - i - 1];
        comp[n - i - 1] = temp;
    }

    cout << endl;
    cout << "str = " << str << endl;
    cout << "comp = " << comp << endl;


    if (str == comp)
    {
        cout << "\"" << str << "\" is a palindrome" << endl;
    }
    else
    {
        cout << "\"" << str << "\" is not a palindrome" << endl;
    }
}

int main ()
{
    char str1[] = "Test String";
    char str2[] = "rotator";

    palindrome(str1);
    palindrome(str2);

    return 0;
}
