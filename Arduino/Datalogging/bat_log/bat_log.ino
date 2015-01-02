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

/*Initialize LEDs*/
//State setup
int nextState;
int currState;
int byebye;

//Button Setup
int NXTSignal;
int modeChange;
int upsideDown;
int off;

//Variables for Mode changing
String modeList[] = {"solid","fade","colorFade","colorFlash"};
String mode;
int modeIndex = 0;
int currMode;

//LED setup
int redPin = 9;
int greenPin = 10;
int bluePin = 11;

int redVal;
int greenVal;
int blueVal;

//Variables for Color Fade mode
int rgbFade[3];
int colorOut = 0;
int i = 0;

//Variables for Color Flash mode
int lastTime;
int currTime;
int elapsedTime;
int colorVals[][3] = {
  {255,0,0}, //Red
  {255,255,0}, //Yellow
  {0,255,0}, //Green
  {0,255,255}, //Blue-Green
  {0,0,255}, //Blue
  {255,0,255} //Purplechar filename[] = "BATLOG00.CSV";
};
int colorIndex = 0;

//Variables for End Game mode
int blinkSpeed = 3000;

//Variables for Purple Fade mode
int fadeAmount = 5;
int fadeBrightness = 0;

//Variables for uhOh mode
int SOS = true;
int iteration = 0;

//Setup enum
enum cases{
  solid,
  fade,
  colorFade,
  colorFlash,
  initialize,
  idle,
  updateMode,
  updateLEDs,
  endGame,
  uhOh,
  writefile,
  leave
};

char filename[] = "batlog00.csv";

void setup(void) {
  
  Serial.begin(9600);
  Serial.println("Program has begun");
  
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  
  /*Initializes filename*/
  for (int i = 0; i < 100; i++) {
    filename[6] = i/10 + '0';
    filename[7] = i%10 + '0';
    Serial.println("Tens: " + i/10);
    Serial.println("Ones: " + i%10);
    Serial.println("i: " + i);
    if (!SD.exists(filename)) {
      // only open a new file if it doesn't exist
      logfile = SD.open(filename, FILE_WRITE); 
      break;  // leave the loop!
    }
  }
  logfile.close();
  currState = initialize;
  Serial.print("Filename: ");
  Serial.println(filename);
}

void loop() {
  Serial.println("Program has begun");
  while(currState != leave){
    
    modeChange = digitalRead(2);
    NXTSignal = digitalRead(3);
    upsideDown = digitalRead(7);
    mode = modeList[modeIndex];
        
    switch(currState){
        
      case initialize: //Initialize
        /*Initialize SD card*/
        Serial.println("Current Case: Initialize");
        
        logfile = SD.open(filename, FILE_WRITE);
        
        Serial.print("Initializing SD Card...");
        pinMode(10, OUTPUT);
        
        if (!SD.begin(chipSelect)) {
          Serial.println("Card failed or not present");
          return;
        }
        Serial.println("Card Initialized");
        logfile.println("Card initialized");      
        
        Serial.print("Logging to: ");  
        Serial.println(filename);
  
        Wire.begin();
        if (!RTC.begin()) {
          logfile.println("RTC not initiailized");
        }
        logfile.println("Begin logging");
        logfile.close();
        nextState = idle;
        break;
        
      case idle://Idle
        if(modeChange == HIGH){
          nextState = updateMode; //Update Mode
        }else if(NXTSignal == HIGH){
          nextState = endGame;
//        }else if(upsideDown == LOW){
//          nextState = uhOh;
        }else{
          nextState = currMode;
        }
        Serial.println("Current Case: Idle");
        
        logfile = SD.open(filename, FILE_WRITE);
        logfile.println("Battery data");
        logfile.close();
        Serial.println("Wrote to file");
        break;
        
      case updateMode:
        if (modeIndex == 3){
          modeIndex = 0;
        }else{
          modeIndex++;
        } 
        delay(500);
                
        currMode = modeIndex;
        nextState = currMode;
        Serial.println("Current Case: Update Mode");
        break;
        
      case updateLEDs: //Update LEDs
        analogWrite(redPin,redVal);
        analogWrite(greenPin,greenVal);
        analogWrite(bluePin,blueVal);
        
        nextState = idle; //Idle State
        Serial.println("Current Case: Update LEDs");
        break;
      
      case endGame:
        if (blinkSpeed > 2){
          //Blinks the LEDs at an increacing pace
          analogWrite(redPin,255);
          analogWrite(greenPin,255);
          analogWrite(bluePin,255);
          delay(blinkSpeed);
          
          analogWrite(redPin,0);
          analogWrite(greenPin,0);
          analogWrite(bluePin,0);
          delay(blinkSpeed);
          
          blinkSpeed = blinkSpeed * .7; //Shortens then next blink
          Serial.print(blinkSpeed);
        }else{
          analogWrite(redPin,255);
          analogWrite(greenPin,0);
          analogWrite(bluePin,0);
        }
      
      case leave:
        byebye = 1;
        Serial.println("LEDs are now turned off");
        delay(500);        
        break;
        
      case uhOh:
        if (SOS == false){
          if (redVal == 0){
            redVal = 255;
            greenVal = 0;
            blueVal = 0;
          }else{
            redVal = 0;
            greenVal = 0;
            blueVal = 0;
          }
          delay(100);
        }else{
          while (iteration < 3){
            digitalWrite(redPin,HIGH);
            digitalWrite(greenPin,LOW);
            digitalWrite(bluePin,LOW);
            
            delay(100);
            
            digitalWrite(redPin,LOW);
            digitalWrite(greenPin,LOW);
            digitalWrite(bluePin,LOW);
            
            delay(100);
            
            Serial.print(iteration);
            Serial.println("Dot");
            iteration++;
          }
          iteration = 0;
          while (iteration < 3){
            digitalWrite(redPin,HIGH);
            digitalWrite(greenPin,LOW);
            digitalWrite(bluePin,LOW);
            
            delay(300);
            
            digitalWrite(redPin,LOW);
            digitalWrite(greenPin,LOW);
            digitalWrite(bluePin,LOW);
            
            delay(300);
            
            Serial.print(iteration);
            Serial.println("Dash");
            iteration++;
          }
          iteration = 0;
          while (iteration < 3){
            digitalWrite(redPin,HIGH);
            digitalWrite(greenPin,LOW);
            digitalWrite(bluePin,LOW);
            
            delay(100);
            
            digitalWrite(redPin,LOW);
            digitalWrite(greenPin,LOW);
            digitalWrite(bluePin,LOW);
            
            delay(100);
            
            Serial.print(iteration);
            Serial.println("Dot");
            iteration++;
          }
          iteration = 0;
          delay(500);
        }
        if (digitalRead(7) == HIGH){
          nextState = updateLEDs;
        }
        Serial.println("Current Case: uhOh");
        Serial.println(digitalRead(7));
        break;
      
      case solid: //Mode: Solid purple
        redVal = 255;
        greenVal = 0;
        blueVal = 255;
        
        nextState = updateLEDs;
        currMode = solid;
        Serial.println("Current Case: Mode: Solid Purple");
        break;
      
      case fade: //Fade Purple
        
        fadeBrightness = fadeBrightness + fadeAmount;
        
        // reverse the direction of the fading 
        if (fadeBrightness == 0 || fadeBrightness == 255) {
          fadeAmount = -fadeAmount;
        }
        
        redVal = fadeBrightness;
        greenVal = 0;
        blueVal = fadeBrightness;
        
        nextState = updateLEDs;
        currMode = fade;
        Serial.println("Current Case: Mode: Fade Purple");
        break;
      
      case colorFade://colorFade
        
        if(colorOut < 3){
  
          int colorIn = colorOut == 2 ? 0 : colorOut + 1;
          
          //variable i is set to 255/increment to RGB
          if(i < 51){
            
            //Increments 5 up and down each loop
            rgbFade[colorOut] -= 5;
            rgbFade[colorIn] += 5;
          
            //Write RGB values
            redVal = rgbFade[0];
            greenVal = rgbFade[1];
            blueVal = rgbFade[2];
         
            delay(5);
            i++;      
          }else{
            i = 0;
            colorOut++; 
          }
          
        }else{
          colorOut = 0;
        }
      
        nextState = updateLEDs;
        currMode = colorFade;
        Serial.println("Current Case: Mode: Color Fade");
        break;
        
    case colorFlash:

      currTime = millis();
      elapsedTime = currTime - lastTime;
      
      if (elapsedTime < 1000){
        //Continue current color
        redVal = colorVals[colorIndex][0];
        greenVal = colorVals[colorIndex][1];
        blueVal = colorVals[colorIndex][2];
      }else{
        lastTime = millis();
        //Change to next color
        if (colorIndex != 5){
          colorIndex++;
        }else{
          colorIndex = 0;
        }
      }
      
      nextState = updateLEDs;
      currMode = colorFlash;
      Serial.println("Current Case: Mode: Color Flash");
      break;
    
    }
    
    currState = nextState;
    
  }
  
  digitalWrite(redPin,LOW);
  digitalWrite(greenPin,LOW);
  digitalWrite(bluePin,LOW);
  
}


