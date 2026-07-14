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
  int reader2 = 0;
  long c2 = 0;
  int avg2 = 0;
  int reader3 = 0;
  long c3 = 0;
  int avg3 = 0;
  for (int i = 1; i<=20; i++)
  {
    reader = analogRead(34);
    c = c + reader;
    delay(2);
  }
  average = c/20;
  Serial.print(" Reading of Pin34 "); Serial.println(average);
  if (average>1800)
  {
    Serial.print(" Finger is  "); Serial.println("BENT");
  }
  if (average<1650)
  {
    Serial.print(" Finger is "); Serial.println("STRAIGHT");
  }
  for (int j = 1; j<=20; j++)
  {
    reader2 = analogRead(32);
    c2 = c2 + reader2;
    delay(2);
  }
  avg2 = c2/20;
  Serial.print(" Reading of Pin32 "); Serial.println(avg2);
  if (avg2>1400)
  {
    Serial.print(" Finger is  "); Serial.println("BENT");
  }
  if (avg2<1200)
  {
    Serial.print(" Finger is "); Serial.println("STRAIGHT");
  }
  for (int k = 1; k<=20; k++)
  {
    reader3 = analogRead(35);
    c3 = c3 + reader3;
    delay(2);
  }
  avg3 = c3/20;
  Serial.print(" Reading of Pin35 "); Serial.println(avg3);
  delay(300);
}
