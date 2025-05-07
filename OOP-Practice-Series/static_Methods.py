class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

temp_c = 30
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)

print(f"{temp_c}°C is equal to {temp_f}°F")
