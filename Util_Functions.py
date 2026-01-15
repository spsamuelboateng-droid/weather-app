from datetime import datetime

def wind_degree_to_direction(deg: float) -> str:
    """
    Convert numerical degree into cardinal wind direction.
    Example: 270 -> 'W'
    """
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    idx = round(deg / 45) % 8
    return directions[idx]


def unix_timestamp_to_localtime(ts: int, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Convert Unix timestamp to human-readable local time.
    Example: 1705341248 -> '2024-01-15 14:20:48'
    """
    return datetime.fromtimestamp(ts).strftime(fmt)


def convert_temperature(value: float, from_unit: str = "K", to_unit: str = "C") -> float:
    """
    Convert temperature between Kelvin, Celsius, and Fahrenheit.
    Default: Kelvin -> Celsius

    Supported:
    - K -> C
    - K -> F
    - C -> K
    - F -> C
    - C -> F
    - F -> K
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Convert to Kelvin first
    if from_unit == "K":
        kelvin = value
    elif from_unit == "C":
        kelvin = value + 273.15
    elif from_unit == "F":
        kelvin = (value - 32) * 5/9 + 273.15
    else:
        raise ValueError(f"Unsupported from_unit: {from_unit}")

    # Convert Kelvin to target
    if to_unit == "K":
        return kelvin
    elif to_unit == "C":
        return kelvin - 273.15
    elif to_unit == "F":
        return (kelvin - 273.15) * 9/5 + 32
    else:
        raise ValueError(f"Unsupported to_unit: {to_unit}")

