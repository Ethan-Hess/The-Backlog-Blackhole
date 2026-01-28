"""
Handles user interaction via the terminal.
"""

from typing import List

from data_manager import DataManager
from vehicle import Vehicle


class InteractionController:
    def __init__(self, vehicles: List[Vehicle], data_manager: DataManager):
        self.vehicles = vehicles
        self.data_manager = data_manager

    def display_menu(self):
        """

        :return:
        """
        pass

    def handle_user_input(self):
        """

        :return:
        """
        pass

    def display_vehicle_info(self, vehicle: Vehicle):
        """

        :param vehicle:
        :return:
        """
        pass

    def display_service_recommendations(self, vehicle: Vehicle):
        """

        :param vehicle:
        :return:
        """
        pass
