#include <iostream>
#include "sub2/peanut.h"
using namespace std;

int callPeanut() {
  int x;
  cout << "Hello Peanut!";
  cout << "Type a number: "; // Type a number and press enter
  cin >> x; // Get user input from the keyboard
  cout << "Your number is: " << x;
  return 0;
}
