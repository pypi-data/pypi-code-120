from enum import Enum


class SensorClass(Enum):
    APPARENT_POWER = "apparent_power",
    AQI ="aqi",
    BATTERY = "battery",
    CARBON_DIOXIDE = "carbon_dioxide",
    CARBON_MONOXIDE = "carbon_monoxide",
    CURRENT = "current",
    DATE = "date",
    ENERGY = "energy",
    FREQUENCY = "frequency",
    GAS = "gas",
    HUMIDITY = "humidity",
    ILLUMINANCE = "illuminance",
    MONETARY = "monetary",
    NITROGEN_DIOXIDE = "nitrogen_dioxide",
    NITROGEN_MONOXIDE = "nitrogen_monoxide",
    NITROUS_OXIDE = "nitrous_oxide",
    OZONE = "ozone",
    PM1 = "pm1",
    PM10 = "pm10",
    PM25 = "pm25",
    POWER_FACTOR = "power_factor",
    POWER = "power",
    PRESSURE = "pressure",
    REACTIVE_POWER = "reactive_power",
    SIGNAL_STRENGTH = "signal_strength",
    SULPHUR_DIOXIDE = "sulphur_dioxide",
    TEMPERATURE = "temperature",
    TIMESTAMP = "timestamp",
    VOLATILE_ORGANIC_COMPOUNDS = "volatile_organic_compounds",
    VOLATILE = "volatile",
    GENERIC = "",
    OBJECTS = "objects",
    NOISE = "noise",