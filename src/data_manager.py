"""
Responsible for loading and saving vehicle and service data using JSON.
"""

from typing import List

from vehicle import Vehicle


class DataManager:
    def __init__(self, data_file_path: str, vehicles: List[Vehicle]):
        self.data_file_path = data_file_path
        self.vehicles = vehicles

    def load_data(self) -> List[Vehicle]:
        """
        Loads data from JSON file and returns it.
        :return:
        """
        pass

    def save_data(self, vehicles: List[Vehicle]):
        """
        Saves data from JSON file and returns it.
        :param vehicles:
        :return:
        """
        pass

    def initialize_sample_data(self):
        """

        :return:
        """
        pass
