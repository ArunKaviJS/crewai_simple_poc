# tools/weather_tools.py


def get_weather(city):
    """
    Get weather information for a city.

    This is a dummy implementation for learning.
    In a real application this could call a weather API.
    """

    print(f"\n🔧 TOOL CALLED: get_weather(city='{city}')")

    weather_data = {
        "Chennai": {
            "temperature": 32,
            "condition": "Cloudy"
        },
        "Bangalore": {
            "temperature": 26,
            "condition": "Rainy"
        },
        "Mumbai": {
            "temperature": 29,
            "condition": "Sunny"
        }
    }

    result = weather_data.get(
        city,
        {
            "temperature": 30,
            "condition": "Unknown"
        }
    )

    return {
        "city": city,
        **result
    }