from typing import (
    List,
)

from config.const import (
    REVERSE_RADIUS,
)
from domain.models.estimated_position.estimated_position import (
    EstimatedPosition,
)
from domain.models.tracking_particle.tracking_particle import (
    TrackingParticle,
)


class ClusterTracking:
    @staticmethod
    def run(
        tracking_particle: TrackingParticle,
    ) -> List[EstimatedPosition]:
        starting_point = tracking_particle.last_estimated_position()

        reversed_estimated_positions: List[EstimatedPosition] = [
            EstimatedPosition(
                x=starting_point.get_x(),
                y=starting_point.get_y(),
                direction=starting_point.get_direction(),
            )
        ]

        tracking_particle.reverse()

        for (
            _,
            estimation_particles,
        ) in enumerate(tracking_particle):
            tracking_particle_collection = (
                estimation_particles.get_particles_within_radius(
                    x=reversed_estimated_positions[-1].get_x(),
                    y=reversed_estimated_positions[-1].get_y(),
                    radius=REVERSE_RADIUS,
                )
            )

            reversed_estimated_positions.append(
                tracking_particle_collection.get_estimated_pose()
            )

        tracking_particle.reverse()

        return reversed_estimated_positions
