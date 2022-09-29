#include <iostream>
#include <stdlib.h> 
#include "sub2/lemon.h"
#include "sub2/orange.h"
using namespace std;

int callLemon() {
  cout << "Hello Lemon!";
  int num = rand() % 10 + 1;

  if (num > 5) {
    callOrange();
  }

  return 0;
}
