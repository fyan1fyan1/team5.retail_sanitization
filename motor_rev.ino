
#include <MultiStepper.h>

#include <AccelStepper.h>

#define dirPinBR 2//Top Right
#define stepPinBR 3
#define dirPinBL 4//Top Left
#define stepPinBL 5
#define motorInterfaceTypeBR 1
#define motorInterfaceTypeBL 1
AccelStepper BRStepper = AccelStepper(motorInterfaceTypeBR,stepPinBR,dirPinBR);
AccelStepper BLStepper = AccelStepper(motorInterfaceTypeBL,stepPinBL,dirPinBL);



#define dirPinTR 6//Top Right
#define stepPinTR 7
#define dirPinTL 8//Top Left
#define stepPinTL 9
#define powerPin 10
#define motorInterfaceTypeTR 1
#define motorInterfaceTypeTL 1
AccelStepper TRStepper = AccelStepper(motorInterfaceTypeTR,stepPinTR,dirPinTR);
AccelStepper TLStepper = AccelStepper(motorInterfaceTypeTL,stepPinTL,dirPinTL);
bool jobdone = false;
String signal="a";
const int TRDis=8200.0;
const int TLDis=8200.0;
const int BRDis=-1400.0;
const int BLDis=1400.0;
int curSpeed=100.0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // stepper motor setup:
  TRStepper.setMaxSpeed(800);
  TRStepper.setCurrentPosition(0);
  TLStepper.setMaxSpeed(800);
  TLStepper.setCurrentPosition(0);
  BRStepper.setMaxSpeed(100);
  BRStepper.setCurrentPosition(0);
  BLStepper.setMaxSpeed(100);
  BLStepper.setCurrentPosition(0);
  pinMode(powerPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    char signal=Serial.read();
    if (signal=='c'){
         BRStepper.moveTo(BRDis);
         BLStepper.moveTo(BLDis);
         while(BRStepper.distanceToGo()!=0 ||BLStepper.distanceToGo()!=0 ){
          curSpeed=100;
          
          BRStepper.setSpeed(curSpeed);
          BRStepper.runSpeedToPosition();
          
          BLStepper.setSpeed(curSpeed);
          BLStepper.runSpeedToPosition();
         }
      }
    else if(signal=='d'){
      BRStepper.moveTo(0);
      BLStepper.moveTo(0);
      while(BRStepper.distanceToGo()!=0 ||BLStepper.distanceToGo()!=0 ){
          curSpeed=100;
          
          BRStepper.setSpeed(curSpeed);
          BRStepper.runSpeedToPosition();
          
          BLStepper.setSpeed(curSpeed);
          BLStepper.runSpeedToPosition();
      }
    }
    else if(signal=='f'){
      curSpeed=800;
      digitalWrite(powerPin,HIGH);
      TRStepper.moveTo(TRDis);
      TLStepper.moveTo(TLDis);
      while(TRStepper.distanceToGo()!=0 ||TLStepper.distanceToGo()!=0 ){
        
        TRStepper.setSpeed(curSpeed);
        TRStepper.runSpeedToPosition();
        
        TLStepper.setSpeed(curSpeed);
        TLStepper.runSpeedToPosition();
      }
    }
    else if(signal=='g'){
      curSpeed=100;
      BRStepper.moveTo(BRDis);
      BLStepper.moveTo(BLDis);
      digitalWrite(powerPin,LOW);
      while(BRStepper.distanceToGo()!=0 ||BLStepper.distanceToGo()!=0 ){
        
        BRStepper.setSpeed(curSpeed);
        BRStepper.runSpeedToPosition();
        
        BLStepper.setSpeed(curSpeed);
        BLStepper.runSpeedToPosition();
      }
    }
    else if(signal=='h'){
      BRStepper.moveTo(0);
      BLStepper.moveTo(0);
      TRStepper.moveTo(0);
      TLStepper.moveTo(0);
      while(BRStepper.distanceToGo()!=0 ||BLStepper.distanceToGo()!=0 || TRStepper.distanceToGo()!=0 || TLStepper.distanceToGo()!=0 ){

        BRStepper.setSpeed(100);
        BRStepper.runSpeedToPosition();
        
        BLStepper.setSpeed(100);
        BLStepper.runSpeedToPosition();
        
        TRStepper.setSpeed(800);
        TRStepper.runSpeedToPosition();
        
        TLStepper.setSpeed(800);
        TLStepper.runSpeedToPosition();
      }
     }
    }
}
  

