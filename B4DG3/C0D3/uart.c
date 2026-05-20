#define F_CPU 8000000UL

#include <avr/io.h>
#include <util/delay.h>

#define UART_TX PB1
#define BAUD_DELAY_US 104   // ~1/9600 sec = 104.17 us

static void uart_putc(char c) {
    uint8_t i;

    // Start bit: LOW
    PORTB &= ~(1 << UART_TX);
    _delay_us(BAUD_DELAY_US);

    // 8 data bits, LSB first
    for (i = 0; i < 8; i++) {
        if (c & 1)
            PORTB |= (1 << UART_TX);
        else
            PORTB &= ~(1 << UART_TX);

        c >>= 1;
        _delay_us(BAUD_DELAY_US);
    }

    // Stop bit: HIGH
    PORTB |= (1 << UART_TX);
    _delay_us(BAUD_DELAY_US);
}

static void uart_puts(const char *s) {
    while (*s)
        uart_putc(*s++);
}

int main(void) {
    // PB1 as output
    DDRB |= (1 << UART_TX);

    // Idle state for UART TX is HIGH
    PORTB |= (1 << UART_TX);

    _delay_ms(500);

    uart_puts("HELLO\r\n");

    while (1) {
    }
}
