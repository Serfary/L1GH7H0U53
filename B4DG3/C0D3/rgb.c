#define F_CPU 8000000UL

#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>

#define RED_PIN    PB0   // OC0A
#define GREEN_PIN  PB1   // OC0B
#define BLUE_PIN   PB4   // OC1B 

static inline void pwm_apply(uint8_t r, uint8_t g, uint8_t b) {
    OCR0A = r;   // Red duty   (0..255)
    OCR0B = g;   // Green duty
    OCR1B = b;   // Blue duty
}

static void setup_pwm(void) {
    // Timer0: Fast PWM, 8-bit, non-inverting on OC0A/OC0B, clk/1
    TCCR0A = (1 << WGM00) | (1 << WGM01) | (1 << COM0A1) | (1 << COM0B1);
    TCCR0B = (1 << CS00);

    // Timer1: 8-bit PWM on OC1B (PB4), TOP=OCR1C, clk/1
    OCR1C = 255;
    OCR1B = 0;
    GTCCR  = (1 << PWM1B) | (1 << COM1B1);
    TCCR1  = (1 << CS10);

    // Set pins as outputs
    DDRB |= (1 << RED_PIN) | (1 << GREEN_PIN) | (1 << BLUE_PIN);

    // Start off
    pwm_apply(0, 0, 0);
}

static void crossfade(uint8_t r0, uint8_t g0, uint8_t b0,uint8_t r1, uint8_t g1, uint8_t b1) {
    for (uint16_t i = 0; i <= 255; ++i) {
        uint8_t r = (uint8_t)(r0 + ((int16_t)(r1 - r0) * i) / 255);
        uint8_t g = (uint8_t)(g0 + ((int16_t)(g1 - g0) * i) / 255);
        uint8_t b = (uint8_t)(b0 + ((int16_t)(b1 - b0) * i) / 255);
        pwm_apply(r, g, b);
        _delay_ms(8);
    }
}

int main(void) {
    setup_pwm();

    while (1) {
        crossfade(255, 0,   0,   0, 255,   0); // Red > Green
        crossfade(0, 255,   0,   0,   0, 255); // Green > Blue
        crossfade(0,   0, 255, 255,   0,   0); // Blue > Red
    }
}
