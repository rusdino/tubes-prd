#define SURFACE_SENSOR_PIN 4  // Sensor 1 - for black/white detection
#define SPEED_SENSOR_PIN 5
int lastState = HIGH;
volatile unsigned long pulseCount = 0;
unsigned long lastTime = 0;
const int pulsesPerRevolution = 43;  // Adjust this to your actual setup
float rpm = 0.0;
String surfaceStatus = "";
const int pwmPin = 22;      // GPIO15 or any PWM-capable pin
const int pwmChannel = 0;
const int pwmFreq = 5000;   // PWM frequency in Hz
const int pwmResolution = 8; // 8-bit resolution → values from 0–255

void IRAM_ATTR onSpeedPulse() {
  pulseCount++;
}

void setup() {
  Serial.begin(115200);

  pinMode(SURFACE_SENSOR_PIN, INPUT_PULLUP);
  pinMode(SPEED_SENSOR_PIN, INPUT_PULLUP);
  ledcSetup(pwmChannel, pwmFreq, pwmResolution);
  ledcAttach(pwmPin, pwmChannel);
  // Interrupt for RPM sensor
  attachInterrupt(digitalPinToInterrupt(SPEED_SENSOR_PIN), onSpeedPulse, FALLING);
}

void loop() {
  unsigned long currentTime = millis();
  ledcWrite(pwmChannel, 64);  // 128/255 = 0.5
  // Read surface sensor
  int surfaceValue = digitalRead(SURFACE_SENSOR_PIN);
  surfaceStatus = (surfaceValue == LOW) ? "BLACK detected" : "WHITE detected";
  int currentState = digitalRead(SPEED_SENSOR_PIN);
  // Print RPM every 1 second
  if (currentTime - lastTime >= 1000) {
    float rpm = (pulseCount * 60.0) / pulsesPerRevolution;
    Serial.print("RPM: ");
    Serial.println(rpm);
    pulseCount = 0;
    lastTime = currentTime;

    Serial.print("RPM: ");
    Serial.print(rpm);
    Serial.print(" | Surface: ");
    Serial.println(surfaceStatus);

    lastTime = currentTime;
  }
}