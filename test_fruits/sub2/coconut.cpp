#include <iostream>
#include "sub2/coconut.h"
#include "sub1/apple.h"
using namespace std;

int callCoconut() {
  cout << "Hello Coconut!";
  callApple();
  return 0;
}
