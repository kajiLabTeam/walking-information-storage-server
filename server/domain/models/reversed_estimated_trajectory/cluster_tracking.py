from __future__ import annotations

from typing import TYPE_CHECKING

from config.const import REVERSE_RADIUS
from domain.dataclasses.coordinate import Coordinate, Pose

if TYPE_CHECKING:
    from domain.models.tracking_particle.tracking_particle import TrackingParticle


class ClusterTracking:
    @staticmethod
    def run(
        tracking_particle: TrackingParticle,
    ) -> list[Pose]:
        starting_pose = tracking_particle.last_estimated_pose()

        reversed_estimated_positions: list[Pose] = [
            starting_pose,
        ]

        tracking_particle.reverse()

        for (
            _,
            estimation_particles,
        ) in enumerate(tracking_particle):
            tracking_particle_collection = (
                estimation_particles.get_particles_within_radius(
                    coordinate=Coordinate(
                        x=reversed_estimated_positions[-1].coordinate.x,
                        y=reversed_estimated_positions[-1].coordinate.y,
                    ),
                    radius=REVERSE_RADIUS,
                )
            )

            reversed_estimated_positions.append(
                tracking_particle_collection.get_estimated_pose(),
            )

        tracking_particle.reverse()

        return reversed_estimated_positions
