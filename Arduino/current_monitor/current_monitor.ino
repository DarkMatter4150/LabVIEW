#include <Wire.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina219;

//LED setup
int redPin = 9;
int greenPin = 10;
int bluePin = 11;

void setup(void) 
{
  uint32_t currentFrequency;

  Serial.begin(115200);
  Serial.println("Hello!");

  Serial.println("Measuring voltage and current with INA219 ...");
  ina219.begin();
}

void loop(void) 
{
  float current = 0;

  current = ina219.getCurrent_mA();

  if (current >= 1000)
  {
    /*LEDs Red*/
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
    delay(3000);
  }
  else
  {
    /*LEDs Purple*/
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, HIGH);
  }

}

