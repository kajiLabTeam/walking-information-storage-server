from typing import list

from domain.dataclasses.coordinate import Pose
from domain.errors.domain_error import DomainError, DomainErrorType
from domain.models.estimated_particle.estimated_particle import EstimatedParticle
from domain.models.tracking_particle.tracking_particle import TrackingParticle


class ReversedEstimationParticleFilter:
    @staticmethod
    def run(
        tracking_particle: TrackingParticle,
    ) -> list[Pose]:
        try:
            (
                starting_point,
                coverage_count,
            ) = tracking_particle.get_coverage_position()

            print(
                "逆推定開始点",
                "x:",
                starting_point.get_x(),
                "y:",
                starting_point.get_y(),
                "方向:",
                starting_point.get_direction(),
                "収束回数:",
                coverage_count,
            )

            reversed_estimated_positions: list[Pose] = [
                Pose(
                    x=starting_point.get_x(),
                    y=starting_point.get_y(),
                    direction=starting_point.get_direction(),
                ),
            ]
            reversed_estimation_particles: list[EstimatedParticle] = [
                EstimatedParticle.reverse_initialize(
                    floor_map=tracking_particle.last_estimation_particles().get_floor_map(),
                    final_position=starting_point,
                    walking_parameter=tracking_particle.last_walking_parameter(),
                ),
            ]

            reversed_walking_parameter = (
                tracking_particle.get_walking_parameter_reverse(
                    index=coverage_count,
                )
            )

            for (
                _,
                reversed_walking_parameter,
            ) in enumerate(reversed_walking_parameter):
                estimation_particles = reversed_estimation_particles[-1]
                estimation_particles.remove_by_floor_map()
                move_estimation_particles = estimation_particles.move(
                    current_walking_parameter=reversed_walking_parameter,
                )

                estimation_particles.remove_by_floor_map()
                estimation_particles.remove_by_direction(
                    step=reversed_walking_parameter.get_step(),
                )
                # estimation_particles.update_weight()
                move_estimation_particles.resampling(
                    step=reversed_walking_parameter.get_step(),
                    mode="reversed",
                )

                reversed_estimation_particles.append(move_estimation_particles)
                reversed_estimated_positions.append(
                    move_estimation_particles.get_estimated_pose(),
                )

            tracking_particle.set_estimation_particles(
                reversed_estimation_particles,
            )

            return reversed_estimated_positions

        except DomainError as e:
            raise DomainError(
                error_type=DomainErrorType.REVERSED_ESTIMATION_PARTICLE_FILTER,
                status_code=e.status_code,
                detail=e.detail,
            )
