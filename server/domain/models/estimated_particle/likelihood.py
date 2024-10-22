from typing import (
    List,
)

import numpy as np
from domain.models.particle.particle import (
    Particle,
)


class Likelihood:
    def __init__(
        self,
        particles: List[Particle],
    ):
        self.__particles = particles
        self.__mean_x = sum(
            particle.get_x() for particle in self.__particles
        ) / len(self.__particles)
        self.__mean_y = sum(
            particle.get_y() for particle in self.__particles
        ) / len(self.__particles)
        self.__std_dev_x = float(
            np.std([particle.get_x() for particle in self.__particles])
        )
        self.__std_dev_y = float(
            np.std([particle.get_y() for particle in self.__particles])
        )

    def get_mean_x(
        self,
    ) -> float:
        return self.__mean_x

    def get_mean_y(
        self,
    ) -> float:
        return self.__mean_y

    def get_std_dev_x(
        self,
    ) -> float:
        return self.__std_dev_x

    def get_std_dev_y(
        self,
    ) -> float:
        return self.__std_dev_y

    def calculate_normalized_probability_densities(
        self,
    ) -> List[float]:
        probability_densities: List[float] = []

        for particle in self.__particles:
            probability_densities.append(
                self.__calculate_probability_density(
                    x=particle.get_x(),
                    y=particle.get_y(),
                ),
            )

        probability_densities_sum = np.sum(probability_densities)

        normalized_probability_densities_sum = [
            probability_density / probability_densities_sum
            for probability_density in probability_densities
        ]

        return normalized_probability_densities_sum

    def __calculate_probability_density(
        self,
        x: int,
        y: int,
    ) -> float:
        return (
            1.0 / (2 * np.pi * self.__std_dev_x * self.__std_dev_y)
        ) * np.exp(
            -(
                (x - self.__mean_x) ** 2 / (2 * self.__std_dev_x**2)
                + (y - self.__mean_y) ** 2 / (2 * self.__std_dev_y**2)
            )
        )
