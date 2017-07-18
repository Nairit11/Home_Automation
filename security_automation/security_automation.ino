const int trigPin = 2;
const int echoPin = 3;
 
int time = 60; // how many minimum seconds gap you wanna keep between two e-mails
 
long lastSend = -time * 1000;
int distance=0;

void setup() {

  Serial.begin(9600);
  pinMode(6,OUTPUT); //buzzer pin
   Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop()
{
  long duration, cm;
   long now = millis();

  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(2);
  digitalWrite(trigPin, LOW);  
  duration = pulseIn(echoPin, HIGH);
  distance = duration/58.2;
  Serial.println(distance);
  delay(1000);
  if(distance<20)
    {
      digitalWrite(6, HIGH);
      delay(2000); 
      if (now > (lastSend + time * 1000))
    {
      Serial.println("Doorstep Detection");
      lastSend = now;
    }
    else
    {
      Serial.println("");
  }

    }
    else
    {digitalWrite(6,LOW);}
 delay(1000);

}
