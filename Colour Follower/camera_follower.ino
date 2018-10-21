#include<Servo.h>

// define servo instances
Servo base;
Servo top;

int i = 0;
char receivedchar;
int basedeg = 90;
int *basepos = &basedeg;
int topdeg = 90;
int *toppos = &topdeg;

void setup() {
  // put your setup code here, to run once:
  base.attach(9);
  top.attach(10);
  base.write(basedeg);
  top.write(topdeg);
  Serial.begin(9600);
}

void receiver(){
  if(Serial.available() > 0){
    receivedchar = Serial.read();
  }
  else{
    receivedchar = 'k';
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  receiver();

  if (receivedchar == 'j'){
    while(*basepos < 180){
      *basepos += 1;
      base.write(basedeg);
      delay(5);
      receiver();
      if (receivedchar == 'k'){
        break;
      }
    }
  }

  if (receivedchar == 'l'){
      while(*basepos > 10){
      *basepos -= 1;
      base.write(basedeg);
      delay(5);
      receiver();
      if (receivedchar == 'k'){
        break;
      }
    }
  }
  
   if (receivedchar == ','){
    while(*toppos < 180){
      *toppos += 1;
      top.write(topdeg);
      delay(5);
      receiver();
      if(receivedchar == 'k'){
        break;
      }
    }
  }

  if (receivedchar == 'i'){
    while(*toppos >= 10){
      *toppos -= 1;
      top.write(topdeg);
      delay(5);
      receiver();
      if(receivedchar == 'k'){
        break;
      }
    }
  }

  if (receivedchar == 'o'){
    *basepos = 90;
    *toppos = 90;
    top.write(90);
    base.write(90);
  }
  
}
