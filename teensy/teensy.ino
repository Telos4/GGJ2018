#include <SPI.h>

const short daccspin = 10;
const short dacldacpin = 2;

typedef struct {short c:1; short b:1; short pad:2; short x:12;
  short pad2:4; short y:12;} linedata_t;
typedef union {linedata_t linedata; unsigned int serial;} lineunion_t;
struct {unsigned short x,y;} currentpos;

linedata_t lines[1000];
unsigned int linecount = 0;



void setup() {
  pinMode(daccspin, OUTPUT);
  digitalWrite(daccspin, HIGH);
  pinMode(dacldacpin, OUTPUT);
  digitalWrite(dacldacpin, LOW);
  SPI.begin();
  // Serial.begin(9600);
  Serial.begin(115200);
  while (!Serial) {}
}

void loop() {
  int t=micros();
  // Serial.print('A');
  // Serial.println(sizeof(short));
  // serialline();
  // delay(10);
  // bigsquare();
  square(50,50,2000,3000);
  smallsquare();
  // delay(10);
  Serial.println(micros()-t);
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
//#define NUM 5000
//unsigned short lines_x1[NUM], lines_x2[NUM], lines_y1[NUM], lines_y2[NUM]; // short = 2 Byte
//unsigned int linecount = 0;


/*
short line2x(const unsigned int line){
return (line >> 16) & 0xFFF;
}
short line2y(const unsigned int line){
return line & 0xFFF; // just to be sure
}
bool line2b(const unsigned int line){
return (line >> 30) & 0x1;
}
*/

void serialline() {
  if (Serial.available() >= 4) {
    unsigned int t = Serial.read() << 24;
    t |= Serial.read() << 16;
    t |= Serial.read() << 8;
    t |= Serial.read();
    lineunion_t line;
    line.serial = t;
    if (line.linedata.c) {
      linecount = 0;
      dac2(0, 0); // Zeiger auf Oszi nach unten links bewegen
      return;
    }
    if (linecount < 1000-1) {
      lines[linecount++] = line.linedata;
    }
  }
  for (unsigned int i = 0; i < linecount; i++) {
    lineto(lines[i]);
  }
}

void lineto(const linedata_t line) {

const short x2 = line.x & 0xFFF;
const short y2 = line.y & 0xFFF;
const bool b = line.b;

if (b){ // 1 = moveto
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

if(stepx >= 0){
  if(x1>x2){
    break;
  }
}
if(stepx < 0){
  if(x1<x2){
    break;
  }
}
if(stepy >= 0){
  if(y1>y2){
    break;
  }
}
if(stepy < 0){
  if(y1<y2){
    break;
  }
}


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
linedata_t line;
line.x=x;
line.y=y;
line.b=b;
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

