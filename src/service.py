"""
Represents a maintenance service and its rules.
"""


class Service:
    def __init__(self, service_name: str, interval_miles: int, last_performed_mileage: int):
        self.serviceName = service_name
        self.intervalMiles = interval_miles
        self.lastPerformedMileage = last_performed_mileage

    def is_due(self, current_mileage: int) -> bool:
        """

        :param current_mileage:
        :return:
        """
        pass

    def perform_service(self, mileage: int):
        """

        :param mileage:
        :return:
        """
        pass
