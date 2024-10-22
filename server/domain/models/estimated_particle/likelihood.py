from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from domain.models.particle.particle import Particle


class Likelihood:
    def __init__(
        self,
        particles: list[Particle],
    ) -> None:
        self.__particles = particles
        self.__mean_x = sum(
            particle.get_coordinate().x for particle in self.__particles
        ) / len(
            self.__particles,
        )
        self.__mean_y = sum(
            particle.get_coordinate().y for particle in self.__particles
        ) / len(
            self.__particles,
        )
        self.__std_dev_x = float(
            np.std([particle.get_coordinate().x for particle in self.__particles]),
        )
        self.__std_dev_y = float(
            np.std([particle.get_coordinate().y for particle in self.__particles]),
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
    ) -> list[float]:
        probability_densities: list[float] = [
            self.__calculate_probability_density(
                x=particle.get_coordinate().x,
                y=particle.get_coordinate().y,
            )
            for particle in self.__particles
        ]

        probability_densities_sum = np.sum(probability_densities)

        return [
            probability_density / probability_densities_sum
            for probability_density in probability_densities
        ]

    def __calculate_probability_density(
        self,
        x: int,
        y: int,
    ) -> float:
        return (1.0 / (2 * np.pi * self.__std_dev_x * self.__std_dev_y)) * np.exp(
            -(
                (x - self.__mean_x) ** 2 / (2 * self.__std_dev_x**2)
                + (y - self.__mean_y) ** 2 / (2 * self.__std_dev_y**2)
            ),
        )
