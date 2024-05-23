#include <Servo.h>
Servo servo;

int echoPin=2;
int trigPin=3;
int pump=5;
int temp=6;

void setup() 
{ Serial.begin (9600);
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT);
pinMode(pump, OUTPUT);
pinMode(temp, OUTPUT);

servo.attach(4);
}

void loop() 
{digitalWrite(pump,1);
    int duration, sm;
  digitalWrite(trigPin, 0); 
  delay(2);
  digitalWrite(trigPin, 1);
  delay(100); 
  digitalWrite(trigPin, 0);

  duration = pulseIn(echoPin, 1);    

  sm = duration/58;

  Serial.print(sm); 
  Serial.println(" sm");

 
if(sm<=12) {digitalWrite(temp,0); delay(50);digitalWrite(pump,0);digitalWrite(temp,1);servo.write(140); delay(250);
digitalWrite(pump,1); servo.write(95); delay(800);}
  }
  