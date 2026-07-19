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

  int reader4 = 0;
  long c4 = 0;
  int avg4 = 0;

  int reader5 = 0;
  long c5 = 0;
  int avg5 = 0;



//FLEX SENSOR 1
  for (int i = 1; i<=20; i++)
  {
    reader = analogRead(34);
    c = c + reader;
    delay(2);
  }
  average = c/20;
  //Serial.print(" Reading of Pin34 "); Serial.println(average);
  if (average>1800)
  {
    //Serial.print(" Finger is  "); Serial.println("BENT");
  }
  if (average<1650)
  {
    //Serial.print(" Finger is "); Serial.println("STRAIGHT");
  }


//FLEX SENSOR 2 
  for (int j = 1; j<=20; j++)
  {
    reader2 = analogRead(32);
    c2 = c2 + reader2;
    delay(2);
  }
  avg2 = c2/20;
  //Serial.print(" Reading of Pin32 "); Serial.println(avg2);
  if (avg2>1400)
  {
    //Serial.print(" Finger is  "); Serial.println("BENT");
  }
  if (avg2<1200)
  {
    //Serial.print(" Finger is "); Serial.println("STRAIGHT");
  }

//FLEX SENSOR 3
  for (int k = 1; k<=20; k++)
  {
    reader3 = analogRead(35);
    c3 = c3 + reader3;
    delay(2);
  }
  avg3 = c3/20;
  //Serial.print(" Reading of Pin35 "); Serial.println(avg3);
  if (avg3>1100)
  {
    //Serial.print(" Finger is  "); Serial.println("BENT");
  }
  if (avg3<1000)
  {
    //Serial.print(" Finger is "); Serial.println("STRAIGHT");
  }


  //FLEX SENSOR 4
  for (int l = 1; l<=20; l++)
  {
    reader4 = analogRead(33);
    c4 = c4 + reader4;
    delay(2);
  }
  avg4 = c4/20;
  //Serial.print(" Reading of Pin33 "); Serial.println(avg4);
  if (avg4>1300)
  {
   // Serial.print(" Finger is  "); Serial.println("BENT");
  }
  if (avg4<1200)
  {
    //Serial.print(" Finger is "); Serial.println("STRAIGHT");
  }
  


  //FLEX SENSOR 5
  for (int n = 1; n<=20; n++)
  {
    reader5 = analogRead(39);
    c5 = c5 + reader5;
    delay(2);
  }
  avg5 = c5/20;
  //Serial.print(" Reading of Pin27 "); Serial.println(avg5);
  

  Serial.print("F1:"); Serial.print(average);Serial.print(",");Serial.print("F2:"); Serial.print(avg2);Serial.print(",");Serial.print("F3:");Serial.print(avg3);Serial.print(",");Serial.print("F4:");Serial.print(avg4);Serial.print(",");Serial.print("F5:");Serial.print(avg5);Serial.println();

  
  delay(300);

}
