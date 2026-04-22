import network
import socket
from machine import Pin, PWM
import time

# --- SAFETY ---
time.sleep(3)

safe = Pin(0, Pin.IN, Pin.PULL_UP)
if safe.value() == 0:
    print("SAFE MODE")
    while True:
        time.sleep(1)

# --- MOTOR PINS ---
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(22, Pin.OUT)
IN4 = Pin(23, Pin.OUT)

# --- PWM ---
ENA = PWM(Pin(25), freq=1000)
ENB = PWM(Pin(26), freq=1000)

# --- SPEED ---
MIN_SPEED = 450
BASE_SPEED = 780
RIGHT_SCALE = 1.04

# --- FAILSAFE TIMER ---
last_command_time = time.ticks_ms()
TIMEOUT = 200   # ms → auto stop if no signal

def apply_speed(pwm, scale=1.0):
    if pwm == 0:
        return 0
    pwm = int(pwm * scale)
    return max(MIN_SPEED, min(900, pwm))

def set_motor(left_pwm, right_pwm):
    ENA.duty(apply_speed(abs(left_pwm)))
    ENB.duty(apply_speed(abs(right_pwm), RIGHT_SCALE))

    # LEFT MOTOR
    if left_pwm > 0:
        IN1.on(); IN2.off()
    elif left_pwm < 0:
        IN1.off(); IN2.on()
    else:
        IN1.off(); IN2.off()

    # RIGHT MOTOR
    if right_pwm > 0:
        IN3.on(); IN4.off()
    elif right_pwm < 0:
        IN3.off(); IN4.on()
    else:
        IN3.off(); IN4.off()

def stop():
    ENA.duty(0)
    ENB.duty(0)
    IN1.off(); IN2.off(); IN3.off(); IN4.off()

# --- MOVEMENT ---
def forward():
    set_motor(BASE_SPEED, BASE_SPEED)

def back():
    set_motor(-BASE_SPEED, -BASE_SPEED)

def left():
    # rotate in place
    set_motor(-BASE_SPEED, BASE_SPEED)

def right():
    # rotate in place
    set_motor(BASE_SPEED, -BASE_SPEED)
    
# --- WIFI ---
ssid = "ESP32_CAR"
password = "12345678"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

print("AP IP:", ap.ifconfig()[0])

# --- UI (NO STOP BUTTON) ---
html = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    margin: 0;
    background: #111;
    color: white;
    font-family: Arial;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.grid {
    display: grid;
    grid-template-columns: 100px 100px 100px;
    grid-template-rows: 100px 100px 100px;
    gap: 15px;
}
button {
    font-size: 16px;
    border: none;
    border-radius: 15px;
    background: #333;
    color: white;
}
button:active {
    background: #00aaff;
}
.empty {
    background: transparent;
}
</style>
</head>

<body>

<div class="grid">
    <div class="empty"></div>
    <button onmousedown="start('forward')" onmouseup="stop()"
            ontouchstart="start('forward')" ontouchend="stop()">FWD</button>
    <div class="empty"></div>

    <button onmousedown="start('left')" onmouseup="stop()"
            ontouchstart="start('left')" ontouchend="stop()">LEFT</button>

    <div class="empty"></div>

    <button onmousedown="start('right')" onmouseup="stop()"
            ontouchstart="start('right')" ontouchend="stop()">RIGHT</button>

    <div class="empty"></div>
    <button onmousedown="start('back')" onmouseup="stop()"
            ontouchstart="start('back')" ontouchend="stop()">BACK</button>
    <div class="empty"></div>
</div>

<script>
let interval;

function start(cmd){
    stop();
    interval = setInterval(() => {
        fetch('/' + cmd);
    }, 100);
}

function stop(){
    clearInterval(interval);
    fetch('/stop');
}
</script>

</body>
</html>
"""

# --- SERVER ---
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
s.settimeout(0.05)

print("Listening on", addr)

# --- LOOP ---
while True:

    # --- FAILSAFE AUTO STOP ---
    if time.ticks_diff(time.ticks_ms(), last_command_time) > TIMEOUT:
        stop()

    try:
        cl, addr = s.accept()
    except:
        continue

    try:
        request = cl.recv(1024).decode()

        last_command_time = time.ticks_ms()

        if '/forward' in request:
            forward()
        elif '/back' in request:
            back()
        elif '/left' in request:
            left()
        elif '/right' in request:
            right()
        elif '/stop' in request:
            stop()

        cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        cl.send(html)

    except Exception as e:
        print("Error:", e)

    finally:
        cl.close()


