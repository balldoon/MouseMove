import ctypes, time

def move():
   ctypes.windll.user32.mouse_event(0x1, 20, 0, 0, 0)  # Mouse Moves 5 pixels to the right

#Every 60 seconds execute Move Function
while True:
    move()
    time.sleep(60)