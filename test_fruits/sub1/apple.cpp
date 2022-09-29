#include <iostream>
#include "sub1/apple.h"
#include "sub1/banana.h"
using namespace std;

int callApple() {
  cout << "Hello Apple!";
  callBanana();
  return 0;
}
