"""
Represents a vehicle and its current state.
"""

from typing import List

from service import Service


class Vehicle:
    def __init__(self, vin: str, make: str, model: str, year: int, mileage: int, services: List[Service]):
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services = services

    def update_mileage(self, new_mileage: int):
        """
        Updates the current mileage.
        :param new_mileage: New mileage value.
        """
        if new_mileage <= self.mileage:
            raise ValueError("New mileage cannot be less than current mileage.")

        self.mileage = new_mileage

    def get_due_services(self) -> List[Service]:
        """
        :return: A list of services that the vehicle has due.
        """
        pass

    def add_service(self, service: Service):
        """

        :param service:
        :return:
        """
        pass
