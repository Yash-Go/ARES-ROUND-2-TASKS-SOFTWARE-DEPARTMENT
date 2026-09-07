# Task 2


def get_distance():

    '''Here it is set so that to show that in practical 
    the sensor would keep sending the distance from here'''

    distance = float(input("Enter distance from sensor: "))
    return distance


def move_forward():

    'Showing that the robot is moving forward'

    print("Robot is moving forward")


def stop_robot():

    'Showing that the robot is stopped'

    print("Robot stopped")


def turn_robot():
    'showing that the robot is turning'

    print("Robot is turning")


safe_distance = 20

while True:

    # Step 1: SENSE

    distance = get_distance()

    # Step 2: DECIDE

    if distance < safe_distance:

        # Step 3: ACT

        stop_robot()
        turn_robot()

    else:
        move_forward()
