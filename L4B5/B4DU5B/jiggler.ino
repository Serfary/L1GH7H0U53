#include <DigiMouse.h>

void setup(){
  DigiMouse.begin();
}

void loop() {
  for(float i=0; i<=2*3.1416; i+=0.09){
    DigiMouse.move(20*cos(i), 20*sin(i), 0);
    DigiMouse.delay(25);
  }
}
