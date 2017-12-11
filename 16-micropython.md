# MicroPython

[MicroPython tutorial for ESP8266][esp-micropython]
[MicroPython tutorial][micropython]


Zkuste z desky poslat při stisknutí tlačítka FLASH vygenerovat HTTP
požadavek a blikne diodou.

Pokročilá verze: Až to bude fungovat, zkuste místo HTTP posílat MQTT zprávu a na jiné
desce  reagovat rozsvícením diody.

## Předpoklady

Nainstalujte si do počítače terminál (např. `picocom`, a do
virtualenvu přidejte balíček [ampy][ampy] (`pip3 install adafruit-ampy`).

## Připojení k NodeMCU (Linux)

Připojte desku k USB. Deska emuluje sériový port
a v počítači by se měl objevit nový port, u mne `/dev/ttyUSB0`

Připojit picocom je možné pomocí

```bash
    picocom /dev/ttyUSB0 -b 115200
```

Terminál odpojíte pomocí `Ctrl+A, Ctrl+X`.

Po stisku Enter by se měl ukázat Python REPL prompt. Zkuste naimportovat
modul `time` a použít funkci `sleep`, `sleep_us`


```python
import time
time.sleep(5)
time.sleep_us(100)
```

## Připojení desky k WiFi síti

ESP8266 (základ NodeMCU desky) se umí připojit k WiFi.

Je připravená síť `robot` s heslem `12345678`. Připojíte se pomocí
modulu `network`

```python
import network
wifi = network.WLAN(network.STA_IF)
# zapnout WiFi část
wifi.active(True)
wifi.connect('robot', '12345678')
print(wifi.isconnected())
print(wifi.ifconfig())
```

Deska si ukládá nastavení sítě do paměti, takže po restartu desky
se zkusí znovu připojit.

## Piny a LED dioda

Najděte si na webu **NodeMCU pinout**. Různé piny procesoru jsou
připojené k různým vývodům desky.

U této desky na pinu 2 je LED dioda, která je připojená k HIGH. Pokud
pin 2 nastavíme na LOW, dioda se rozsvítí.

```python
import machine
led = machine.Pin(2, machine.Pin.OUT)
led.low()
led.high()

# zablikat
for i in range(20):
    led.value(i % 2)
    time.sleep_ms(250)
```

Tlačítko FLASH je zapojené na pinu 0. Spíná k LOW.

```python
b = machine.Pin(0, machine.Pin.IN)
print("Waiting for press")
while b.value():
    time.sleep_ms(50)
```

## HTTP požadavky

Deska umí posílat HTTP požadavky pomocí modulu `urequests`.

```python
import urequests
urequests.get('https:// .///')
```

Otestovat `urequests` můžete např. pomocí služby [requestbin]

## Nahrání kódu

Na flash paměti počítače je malý filesystém. Je možné z něho číst a
zapisovat na něj souboru.

Když deska nastartuje, zkouší spustit skript `main.py`.

Soubory do desky se nahrávají pomocí nástroje `ampy`

```bash
ampy -p /dev/ttyUSB0 put filename.py
```

Zkuste do desky nahrát program, který počká na stisknutí tlačítka
a někam pošle HTTP request.

##

[ampy]: https://github.com/adafruit/ampy
[utime]: https://docs.micropython.org/en/latest/pyboard/library/utime.html
[machine]: https://docs.micropython.org/en/latest/pyboard/library/machine.html
[esp-micropython]: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
[micropython]: https://docs.micropython.org/en/latest/pyboard/
[requestbin]: https://requestb.in/