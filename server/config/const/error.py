import secrets


def PARTICLES_STEP_ERROR() -> int:  # noqa: N802
    return secrets.choice(range(-10, 11))


def PARTICLES_ANGLE_ERROR() -> float:  # noqa: N802
    return secrets.choice(range(-10, 11))


def PARTICLES_DIRECTION_ERROR() -> float:  # noqa: N802
    return secrets.choice(range(-90, 91))
