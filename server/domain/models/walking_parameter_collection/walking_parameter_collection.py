from typing import (
    List,
)

from domain.models.walking_parameter.walking_parameter import (
    WalkingParameter,
)


class WalkingParameterCollection:
    def __init__(
        self,
    ):
        self.__walking_parameters: List[WalkingParameter] = []

    def get_walking_parameters(
        self,
    ) -> List[WalkingParameter]:
        return self.__walking_parameters

    def add(
        self,
        walking_parameter: WalkingParameter,
    ):
        self.__walking_parameters.append(walking_parameter)

    def remove(
        self,
        walking_parameter: WalkingParameter,
    ):
        self.__walking_parameters.remove(walking_parameter)

    def __iter__(
        self,
    ):
        return iter(self.__walking_parameters)

    def __len__(
        self,
    ):
        return len(self.__walking_parameters)

    def __getitem__(
        self,
        index,
    ):
        return self.__walking_parameters[index]
