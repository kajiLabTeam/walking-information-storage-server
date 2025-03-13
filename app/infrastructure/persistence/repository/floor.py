from sqlmodel import Session, select

from app.infrastructure.persistence.models import Floor, FloorInformation


class FloorRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, floor: Floor) -> Floor:
        self.session.add(floor)
        self.session.refresh(floor)
        return floor

    def get_by_building_id(self, building_id: str) -> list[Floor]:
        statement = select(Floor).where(Floor.building_id == building_id)
        return list(self.session.exec(statement).all())


class FloorInformationRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, floor_information: FloorInformation) -> FloorInformation:
        self.session.add(floor_information)
        self.session.refresh(floor_information)
        return floor_information

    def get_by_floor_id(self, floor_id: str) -> list[FloorInformation]:
        statement = select(FloorInformation).where(FloorInformation.floor_id == floor_id)
        return list(self.session.exec(statement).all())

    def get_latest_by_floor_id(self, floor_id: str) -> FloorInformation | None:
        statement = select(FloorInformation).where(FloorInformation.floor_id == floor_id).limit(1)
        return self.session.exec(statement).first()
