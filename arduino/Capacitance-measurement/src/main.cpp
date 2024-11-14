#include <Arduino.h>

#define MEASURE_PIN 10
#define CHARGE_PIN 4

uint32_t measureChargeTime();

void setup() {
    Serial.begin(9600);
    pinMode(MEASURE_PIN, INPUT);
    pinMode(CHARGE_PIN, OUTPUT);
    digitalWrite(CHARGE_PIN, LOW);
}

void loop() {
    Serial.println(measureChargeTime());
    delay(100);
}

uint32_t measureChargeTime() {
    uint32_t counter = 0;
    digitalWrite(CHARGE_PIN, HIGH);
    while (!digitalRead(MEASURE_PIN)) {
        ++counter;
    }
    digitalWrite(CHARGE_PIN, LOW);
    while (digitalRead(MEASURE_PIN)) {
    }
    return counter;
}