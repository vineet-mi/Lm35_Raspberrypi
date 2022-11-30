float vref=3.3;
float resolution = vref/1023;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
  Serial.println("HI");

}

void loop() {
  // put your main code here, to run repeatedly:
  float temp=analogRead(A0);
  temp=resolution*temp;
  temp=0.5*temp*1000;
  Serial.println(temp);
  delay(1000);
}
