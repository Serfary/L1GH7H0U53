
#include "DigiKeyboard.h"
void setup() {
}

void loop() {
  //DigiKeyboard.delay(1000);
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(500);
  DigiKeyboard.print("cd ~/ && python ~/L1GH7H0U53/L4B5/H45H_CR4CK1NG/generate_hashes.py && echo dGVzdA== | base64 -d > message.txt && zip -P $(shuf -n1 ~/wordlist.txt) ~/secure.zip message.txt && rm message.txt && rm ~/.local/share/hashcat/hashcat.potfile");
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  for(;;){ /*empty*/ }
}
