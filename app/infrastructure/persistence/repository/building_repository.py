from sqlmodel import Session, select

from app.infrastructure.persistence.models import Building


class BuildingRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, building: Building) -> Building:
        self.session.add(building)
        self.session.commit()
        return building

    def get_all(self) -> list[Building]:
        return list(self.session.exec(select(Building)).all())
