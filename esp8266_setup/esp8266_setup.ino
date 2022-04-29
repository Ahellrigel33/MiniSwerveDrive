#include "ESP_MICRO.h"
#include <SoftwareSerial.h>

#define CTRL_CNT 3  // number of floats sent by Python over Wi-Fi
#define GPIO_RX 13  // ESP8266 RX pin
#define GPIO_TX 15  // ESP8266 TX pin
String network_name = "ChenSpotNuc";  // name of the Wi-Fi network ESP8266 will connect to 
String network_pass = "numberonevictoryroyale"; // password of the Wi-Fi network ESP8266 will connect to 

SoftwareSerial espSerial(GPIO_RX, GPIO_TX); // RX, TX
float send_data[CTRL_CNT] = {0.0};  
char separator = '_'; // separator between commands sent by python

 
void setup(){
  Serial.begin(9600);
  espSerial.begin(9600);
  start(network_name,network_pass); // Wifi details to connect to
}

void loop(){
  CheckNewReq();  // checks for a new command sent by Python
  if (isReqCame) {
    String recv_data = getPath();   // gets the data sent from Python
    isReqCame = !isReqCame;
    recv_data.remove(0,1);    // removes the '/' character 
    Serial.println(recv_data);  // prints data sent by Python for debugging

    /* 
     *  parses string data sent by python into floats
    */
    int curr_ind = 0;
    int sep_ind = 0;
    for (int ctrl_ind = 0; ctrl_ind < CTRL_CNT; ctrl_ind++) {     
      String string_val = "";
      sep_ind = recv_data.indexOf(separator,curr_ind);
      string_val = recv_data.substring(curr_ind,sep_ind);
      send_data[ctrl_ind] = string_val.toFloat();
      curr_ind = sep_ind+1;
    }

    /* 
     *  sends byte array to MBED over serial
    */
    byte *p = (byte*)send_data;
    for(byte i = 0; i < sizeof(send_data); i++){
      espSerial.write(p[i]);    // write each byte of the control data to the mbed 
    }
    espSerial.write('a');   // send a character to indicate start of command message
  }
}
