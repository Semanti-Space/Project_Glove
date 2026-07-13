void setup() 
  // void setup()
{
    Serial.begin(115200);
    analogSetAttenuation(ADC_11db);
}

void loop() 
{
  int reader = 0;
  long c = 0;
  int average = 0;
  for (int i = 1; i<=20; i++)
  {
    reader = analogRead(34);
    c = c + reader;
    delay(2);
  }
  average = c/20;
  Serial.print(" Reading of Pin34 "); Serial.println(average);
  if (average>1500)
  {
    Serial.print(" Finger is  "); Serial.println("BENT");
  }
  if (average<1500)
  {
    Serial.print(" Finger is "); Serial.println("STRAIGHT");
  }
  
  delay(300);
}
