from djitellopy import Tello

# Uzdevums: Iziet trasi ar koda palidzību
# Noteikumi:
# - secīgi jaiziet cauri visiem vārtiem
# - jaapmeklē visas platformas
# - jaātgriezas atpakaļ
# - caur vārtiem drīkst līdot tikai taisni (ar kāmeru priekšā)

# Dokumentācija un piemēri
# https://github.com/damiafuentes/DJITelloPy/tree/master
# https://github.com/damiafuentes/DJITelloPy/blob/master/examples/simple.py

tello = Tello()

tello.connect()
tello.takeoff()
tello.move_down(5)
tello.set_speed(20)

tello.rotate_clockwise(180)

tello.move_forward(123)
tello.land()
tello.time.sleep(3)
tello.takeoff()
tello.move_down(20)
tello.rotate_counter_clockwise(90)
tello.move_forward(95)
tello.rotate_clockwise(90)
tello.move_forward(63)
tello.land()
tello.time.sleep(3)
tello.takeoff()
tello.move_down(20)
tello.rotate_clockwise(90)
tello.move_forward(95)
tello.rotate_clockwise(90)
tello.move_forward(186)
tello.land()