from hass_client import HomeAssistantClient

from aiplusiot.sensors.standard_sensors.StandardSensor import StandardSensor
from aiplusiot.sensors.standard_sensors.SensorClasses import SensorClass


class NoiseSensor(StandardSensor):
    def __init__(self,hass_instance: HomeAssistantClient, sensor_info: dict) -> None:
        """
        | Initializes an object sensor using a sensor data dict

        :param hass_instance: Instance of the HomeAssistant Client
        :type hass_instance: HomeAssistantClient

        :param sensor_info: Sensor data dictionary
        :type sensor_info: dict
        """
        super().__init__(hass_instance, sensor_info)
        self.sensor_class = SensorClass.NOISE
        self.noise_level = sensor_info['state']

    def get_noise_level(self) -> int:
        """
        | Gets the current object count on the sensor


        :return: Current object count
        :rtype: int
        """
        return self.noise_level

    async def _update_fields(self, event_details: dict) -> None:
        await super(NoiseSensor, self)._update_fields(event_details)


        self.noise_level = event_details['new_state']['state']