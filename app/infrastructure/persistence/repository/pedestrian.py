from sqlmodel import Session, select

from app.infrastructure.persistence.models import Pedestrian, WalkingInformation


class PedestrianRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, pedestrian: Pedestrian) -> Pedestrian:
        self.session.add(pedestrian)
        return pedestrian


class WalkingInformationRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, walking_information: WalkingInformation) -> WalkingInformation:
        self.session.add(walking_information)
        return walking_information

    def get_by_pedestrian_id(self, pedestrian_id: int) -> list[WalkingInformation]:
        statement = select(WalkingInformation).where(
            WalkingInformation.pedestrian_id == pedestrian_id
        )
        return list(self.session.exec(statement).all())
