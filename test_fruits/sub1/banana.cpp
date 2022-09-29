#include <iostream>
#include "sub1/banana.h"
#include "sub2/orange.h"
#include "sub2/coconut.h"
#include "sub1/blueberry.h"
using namespace std;

int callBanana() {
  cout << "Hello Banana!";
  callOrange();
  callCoconut();
  callBlueberry();
  return 0;
}
