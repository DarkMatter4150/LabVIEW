#include <Wire.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina219;

//LED setup
int redPin = 9;
int greenPin = 10;
int bluePin = 11;
int led = 13;

void setup(void) {
  uint32_t currentFrequency;
  Serial.begin(9600);
  // Serial.println("Hello!");
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(led, OUTPUT);
  Serial.println("Measuring voltage and current with INA219 ...");
  ina219.begin();
}

void loop(void) {
  
  float current = 0;
  current = ina219.getCurrent_mA();
  // Serial.print("Current Draw (mA): ");
  Serial.println(current);
  
  if (current >= 2000) {
    /*LEDs Red*/
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
    digitalWrite(led, HIGH);
    // delay(3000);
  } else {
    /*LEDs Purple*/
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, HIGH);
    digitalWrite(led, LOW);
  }
  
}

