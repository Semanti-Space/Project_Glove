void setup() 
  // void setup()
{
    Serial.begin(115200);
    analogSetAttenuation(ADC_11db);
}

void loop() 
{
  int reader = 0;
  int c = 0;
  int average = 0;
  for (int i = 1; i<=10; i++)
  {
    reader = analogRead(34);
    c = c + reader;
  }
  average = c/10;
  Serial.print(" Reading of Pin34 "); Serial.println(average);
  delay(100);
}
