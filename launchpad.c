/*
  Blink
  The basic Energia example.
  Turns on an LED on for one second, then off for one second, repeatedly.
  Change the LED define to blink other LEDs.
  
  Hardware Required:
  * LaunchPad with an LED
  
  This example code is in the public domain.
*/

#include "pitches.h"

volatile int state_P1_3 = HIGH;
volatile int state_P1_4 = HIGH;

char buff_last_WIN = '0';
char buff_last_SCORE = '0';
char buff_last_HIT = '0';
char buff_last_SF = 'a';
char buff_last_stock = 'a';



// most launchpads have a red LED
#define TONER 12
#define RLED RED_LED
#define GLED GREEN_LED
#define P1_3 5
#define P1_4 6
#define LED1 8  //GREEN
#define LED2 9  //YELLOW
#define LED3 15  //RED

  
// the setup routine runs once when you press reset:
void setup()
{
  // begin bluetooth communications
  Serial.begin(9600);
  // initialize the digital pin as an output.
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(RLED, OUTPUT);
  pinMode(GLED, OUTPUT);
  pinMode(P1_3, INPUT);
  pinMode(P1_4, INPUT); 
  digitalWrite(RLED, LOW);
  digitalWrite(GLED, LOW);
  digitalWrite(TONER, LOW);
  Serial.flush();
}

// the loop routine runs over and over again forever:
void loop() {
  
  state_P1_3=digitalRead(P1_3);
  state_P1_4=digitalRead(P1_4);

  int buf_size = Serial.available();
  if (buf_size > 4) {
    buff_last_WIN = Serial.read();
    buff_last_SCORE = Serial.read();
    buff_last_HIT = Serial.read();
    buff_last_SF = Serial.read();
    buff_last_stock = Serial.read();
  }
  if (buff_last_WIN - '0' == 1) {
    tone(12, NOTE_C4);
    delay(250);
    tone(12, NOTE_E4);
    delay(250);
    tone(12, NOTE_G4);
    delay(250);
    noTone(12);
    buff_last_WIN = '0';
    buff_last_SCORE = '0';
    buff_last_HIT = '0';
  }
  if (buff_last_HIT - '0' == 1) {
    tone(12, NOTE_C5);
    delay(500);
    noTone(12);
    delay(200);
    buff_last_HIT = '0';
  }

  if (!state_P1_3){
    digitalWrite(RLED, HIGH);
    switch (buff_last_SF){
      case '0':
        digitalWrite(LED3, HIGH);
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        break;
      case '1':
        digitalWrite(LED2, HIGH);
        digitalWrite(LED1, LOW);
        digitalWrite(LED3, LOW);
        break;
      case '2':
        digitalWrite(LED1, HIGH);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        break;
      default:
        digitalWrite(GLED, HIGH);
        break;
    }
    for (int i = 0; i < buff_last_SCORE - '0'; i++) {
      tone(12, NOTE_C4);
      delay(250);
      noTone(12);
      delay(250);
    }
  }
  if (!state_P1_4){
    
    switch (buff_last_stock){
      case '0':
        digitalWrite(LED3, HIGH);
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        break;
      case '1':
        digitalWrite(LED2, HIGH);
        digitalWrite(LED1, LOW);
        digitalWrite(LED3, LOW);
        break;
      case '2':
        digitalWrite(LED1, HIGH);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        break;
      default:
        digitalWrite(GLED, HIGH);
        break;
    }
  }
  if (state_P1_4 && state_P1_3){
    digitalWrite(GLED, LOW);
    digitalWrite(RLED, LOW);
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);
    digitalWrite(LED3, LOW);
    digitalWrite(TONER, LOW);
  }
}

///////////////////////////////////////////////////////////////////////////
//Blue Tooth Code
//int counter;
//#define LED RED_LED
//
//void setup()
//{
//  // put your setup code here, to run once:
////  counter = 0;
//  Serial.begin(9600);
//  pinMode(LED, OUTPUT);
//  digitalWrite(LED, LOW);
//}

//void loop()
//{
//  int buf_size = Serial.available();
//  if (buf_size > 0){
//    char input = Serial.read();
//    if (input == '0'){
//      digitalWrite(LED, LOW);
//    }
//    else if (input == '1'){
//      digitalWrite(LED, HIGH);
//    }
//    else if(input == '2'){
//      Serial.write("hello\n");
//    }
//  }
//}
