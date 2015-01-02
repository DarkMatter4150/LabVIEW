#include <SD.h>
#include <SPI.h>
#include <Wire.h>
#include <RTClib.h>
 
/*Custom definitions*/
#define log_interval 1000 //in milliseconds
#define echo_to_serial 1 //echo data to serial port

#define redLED 3
#define greenLED 4

#define batteryPin 0 //analog 0

 
RTC_DS1307 RTC; //Define Real Time Clock Object
 
const int chipSelect = 10;

File logfile;

void error(char *str) {
  Serial.print("error: ");
  Serial.println(str);
  
  digitalWrite(redLED, HIGH);
  while(1);
}

void setup(void) {
  
  Serial.begin(9600);
  Serial.println("Program has begun");
  
  Serial.print("Initializing SD Card...");
  pinMode(10, OUTPUT);
  
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed or not present");
    return;
  }
  Serial.println("Card Initialized");
  
//  /*Create new file*/
//  char filename[] = "BAT_LOG00.CSV";
//  for (uint8_t i = 0; i < 100; i++) {
//    filename[7] = i / 100 + '0';
//    filename[8] = i % 10 + '0';
//    if (! SD.exists(filename)) {
//      logfile = SD.open(filename, FILE_WRITE);
//      break;
//    }
//  }

  logfile = SD.open("batlog.csv", FILE_WRITE);
  
  if (! logfile) {
    error("Could not create file");
  }
  
  logfile.println("File initialized");
  
  Serial.print("Logging to: ");  
  Serial.println("batLog.csv");
  
  Wire.begin();
  if (!RTC.begin()) {
    logfile.println("RTC failed");
  }
  
  logfile.println("Logging Battery voltage");
  
//  if (logfile.writeError || !logfile.sync()) {
//    error("Write Header");
//  }
  
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  
}

void loop() {
    // create a new file
  char filename[] = "LOGGER00.CSV";
  for (uint8_t i = 0; i < 100; i++) {
    filename[6] = i/10 + '0';
    filename[7] = i%10 + '0';
    if (! SD.exists(filename)) {
      // only open a new file if it doesn't exist
      logfile = SD.open(filename, FILE_WRITE); 
      break;  // leave the loop!
    }
  }
  
  Serial.println("Program has begun");
  File myFile = SD.open(filename, FILE_WRITE);
  myFile.println("New loop");
  for (int i = 0; i < 10; i++) {
    Serial.println("Program has begun");
    myFile.println("New Data!!");
  }
  myFile.close();
}


