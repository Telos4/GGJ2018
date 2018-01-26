#include <SPI.h>

const short daccspin=10;

void setup(){
pinMode(daccspin,OUTPUT);
digitalWrite(daccspin,HIGH);
SPI.begin();
// SPI.beginTransaction(SPISettings(20000000, MSBFIRST, SPI_MODE0));
// Serial.begin(9600);
Serial.begin(115200);
}

void loop(){
// Serial.println(sizeof(short));
serialline();
}

#define NUM 5000
unsigned short lines_x1[NUM], lines_x2[NUM], lines_y1[NUM], lines_y2[NUM]; // short = 2 Byte
unsigned int linecount=0;

void serialline(){
if(Serial.available() >= 8) { // 2 Byte je Endpunkt
const short x1 = (Serial.read()<<8) | Serial.read();
const short y1 = (Serial.read()<<8) | Serial.read();
const short x2 = (Serial.read()<<8) | Serial.read();
const short y2 = (Serial.read()<<8) | Serial.read();
if(x1&(1<<15)){
linecount=0;
dacsingle(0,0); // Zeiger auf Oszi nach unten links bewegen
dacsingle(0,1);
return;
}
if(linecount<NUM){
lines_x1[linecount]=x1;
lines_y1[linecount]=y1;
lines_x2[linecount]=x2;
lines_y2[linecount]=y2;
linecount++;
}
}
for(int i=0; i<linecount; i++){
line(lines_x1[i],lines_y1[i],lines_x2[i],lines_y2[i],200);
}
/*
if(Serial.available() >= 9) { // "1 1 1 1\n\r"
const int x1 = Serial.parseInt();
const int y1 = Serial.parseInt();
const int x2 = Serial.parseInt();
const int y2 = Serial.parseInt();
lines_x1[linecount]=x1;
lines_y1[linecount]=y1;
lines_x2[linecount]=x2;
lines_y2[linecount]=y2;
linecount++;
}
for(int i=0; i<linecount; i++){
line(lines_x1[i],lines_y1[i],lines_x2[i],lines_y2[i],200);
}
*/
}

void sine(){
float i=0;
while(true){
dacsingle(map(sin(i),-1,1,0,4095),0);
dacsingle(map(tan(i),-1,1,0,4095),1);
i+=0.01;
}
}

void square(){
line(0,0,100,0,500);
line(100,0,100,100,500);
line(100,100,0,100,500);
line(0,100,0,0,500);
}

void line(const unsigned short x0, const unsigned short y0, const unsigned short x1, const unsigned short y1, const unsigned int steps){
for(int i=0; i< steps; i++){
dac2((x0*(steps-i)+x1*i)/steps,(y0*(steps-i)+y1*i)/steps);
}
}

void dac2(const unsigned short val0, const unsigned short val1){
dacsingle(val0,0);
dacsingle(val1,1);
}

void dacsingle(const unsigned short val, const bool chan){

byte b1=0b00110000;
b1 |= val >> 8;
if(chan==1) b1 |= 1 << 7;
const byte b2=val & 0b11111111;
SPI.beginTransaction(SPISettings(20000000, MSBFIRST, SPI_MODE0));
digitalWrite(daccspin,LOW);
SPI.transfer(b1);
SPI.transfer(b2);
digitalWrite(daccspin,HIGH);
SPI.endTransaction();
}
