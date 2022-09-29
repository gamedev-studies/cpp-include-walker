#include <iostream>
#include <stdlib.h> 
#include "sub2/orange.h"
#include "sub2/lemon.h"
using namespace std;

int callOrange() {
  cout << "Hello Orange!";
  int num = rand() % 10 + 1;

  if (num > 5) {
    callLemon();
  }
  
  return 0;
}
