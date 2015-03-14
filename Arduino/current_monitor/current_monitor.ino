#include <Wire.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina219;

//LED setup
int redPin = 9;
int greenPin = 10;
int bluePin = 11;
int led = 13;

float current = 0;
float voltage = 0;

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
  current = 0;
  voltage = 0;
  
  current = ina219.getCurrent_mA();
  voltage = ina219.getBustVoltage_V();
  // Serial.print("Current Draw (mA): ");
  Serial.print(voltage);
  Serial.print("\t");
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
  
  delay(500);
  
}

