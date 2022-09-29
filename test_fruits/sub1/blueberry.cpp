#include <iostream>
#include "sub2/lemon.h"
#include "sub1/apple.h"
#include "sub1/blueberry.h"
using namespace std;

int callBlueberry() {
  cout << "Hello Blueberry!";
  callApple();
  callLemon();
  return 0;
}
