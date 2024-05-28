import random


def PARTICLES_STEP_ERROR() -> int:
    return random.randint(-10, 10)


def PARTICLES_ANGLE_ERROR() -> float:
    return random.randint(-10, 10)


def PARTICLES_DIRECTION_ERROR() -> float:
    return random.randint(-90, 90)
