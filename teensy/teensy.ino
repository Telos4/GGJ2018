/*
ser = serial.Serial("/dev/cu.usbmodem3297371", 115200, timeout=10)
ser.write(((0<<31)+(0<<30)+(3000<<16)+4000).to_bytes(4,'big'))
ser.close()
*/

#include <SPI.h>

const short daccspin = 10;
const short dacldacpin = 2;

struct {unsigned short x=0,y=0;} currentpos;

unsigned int lines[1000];
unsigned int linecount = 0;

unsigned int lastframe=0;


void setup() {
  pinMode(daccspin, OUTPUT);
  digitalWrite(daccspin, HIGH);
  pinMode(dacldacpin, OUTPUT);
  digitalWrite(dacldacpin, LOW);
  SPI.begin();
  // Serial.begin(9600);
  Serial.begin(115200);
  // while (!Serial) {}
}

void loop() {
  // int t=micros();
  // for (int i=0; i<10; i++)
  // smallsquare();
  serialline();
  // bigsquare();
  // square(50,50,2000,3000);
  // smallsquare();
  // Serial.println(micros()-t);
  // delay(10);
  
}

void square(int x1, int y1, int x2, int y2){
mylineto(1,x1,y1);
mylineto(0,x2,y1);
mylineto(0,x2,y2);
mylineto(0,x1,y2);
mylineto(0,x1,y1);
}
void bigsquare(){
  square(0,0,4095,4095);
}
void smallsquare(){
  square(500,500,1000,1000);
}



short line2x(const unsigned int line){
return (line >> 16) & 0xFFF;
}
short line2y(const unsigned int line){
return line & 0xFFF; // just to be sure
}
bool line2b(const unsigned int line){
return (line >> 30) & 0x1;
}


void serialline() {
  unsigned int thisframe=millis();
  if(thisframe-lastframe >= 20){
    lastframe=thisframe;
    mylineto(1,0,0);
    for (unsigned int i = 0; i < linecount; i++) {
      lineto(lines[i]);
    }
  }
  
  if (Serial.available() >= 4) {
    unsigned int t = Serial.read() << 24;
    t |= Serial.read() << 16;
    t |= Serial.read() << 8;
    t |= Serial.read();
    if (t&(1<<31)) {
      linecount = 0;
      dac2(0, 0); // Zeiger auf Oszi nach unten links bewegen
      return;
    }
    if (linecount < 1000-1) {
      lines[linecount++] = t;
    }
  }
}

void lineto(const unsigned int line) {


const short x2 = line2x(line);
const short y2 = line2y(line);
const bool b = line2b(line);

if(b){ // 1 = moveto
currentpos.x=x2;
currentpos.y=y2;
dac2(x2,y2);
return;
}

short x1 = currentpos.x;
short y1 = currentpos.y;

// Serial.println("cur  " + String(x1)+" "+String(y1));
// Serial.println("y1   " + String(y1));
// Serial.println("y2   " + String(y2));

const int len = abs(x2-x1)+abs(y2-y1);
// const int len = sqrt(sq(x2-x1)+sq(y2-y1));
// Serial.println(len);
const int steplen = 30;
// Serial.print('_');
const int shift=10;
const int stepx = ((((int)(x2-x1))*steplen)<<shift)/len;
// Serial.println(stepx);
const int stepy = ((((int)(y2-y1))*steplen)<<shift)/len;
// Serial.println(y2-y1);
// Serial.println(stepy);

while(true){

if(stepx >= 0 && x1>x2) break;
if(stepx <  0 && x1<x2) break;
if(stepy >= 0 && y1>y2) break;
if(stepy <  0 && y1<y2) break;

dac2(x1,y1);
x1=((x1<<shift)+stepx)>>shift;
y1=((y1<<shift)+stepy)>>shift;
// Serial.println(String(x1)+" "+String(y1));
}

// dac2(x2,y2);

currentpos.x=x2;
currentpos.y=y2;

}

void mylineto(int b, int x, int y) {
unsigned int line = y;
line |= x<<16;
line |= b<<30;
lineto(line);
}



void dac2(const unsigned short val0, const unsigned short val1) {
  // digitalWrite(dacldacpin, HIGH);
  dacsingle(val0, 0);
  dacsingle(val1, 1);
  // digitalWrite(dacldacpin, LOW);
}

void dacsingle(const unsigned short val, const bool chan) {
  byte b1 = 0b00110000;
  b1 |= val >> 8;
  if (chan == 1) b1 |= 1 << 7;
  const byte b2 = val & 0b11111111;
  SPI.beginTransaction(SPISettings(20000000, MSBFIRST, SPI_MODE0));
  digitalWrite(daccspin, LOW);
  SPI.transfer(b1);
  SPI.transfer(b2);
  digitalWrite(daccspin, HIGH);
  SPI.endTransaction();
}

