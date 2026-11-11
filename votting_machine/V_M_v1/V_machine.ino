void setup() {

    pinMode(2, INPUT);
    pinMode(3, INPUT);
    pinMode(4, INPUT);

    Serial.begin(9600);

}

void loop() {

    if(digitalRead(2) == HIGH) {
        Serial.println("candidate 1");
        delay(1000);
    }

    if(digitalRead(3) == HIGH) {
        Serial.println("candidate 2");
        delay(1000);
    }

    if(digitalRead(4) == HIGH) {
        Serial.println("candidate 3");
        delay(1000);
    }
    
}
