def pump_water(accumulated_energy_consumption: int) -> int:
    print("Pump water: 10 minutes")
    return accumulated_energy_consumption + 5


def spin_1(accumulated_energy_consumption: int) -> int:
    print("Spin: 5 minutes")
    return accumulated_energy_consumption + 15


def heat_water(accumulated_energy_consumption: int) -> int:
    print("Heat water: 20 minutes")
    return accumulated_energy_consumption + 1300


def rinse(accumulated_energy_consumption: int) -> int:
    print("Rinse: 15 minutes")
    return accumulated_energy_consumption + 80


def spin_2(accumulated_energy_consumption: int) -> int:
    print("Spin: 40 minutes")
    return accumulated_energy_consumption + 500


def start_washing() -> int:
    energy_consumption_1: int = pump_water(0)
    energy_consumption_2: int = spin_1(energy_consumption_1)
    energy_consumption_3: int = heat_water(energy_consumption_2)
    energy_consumption_4: int = rinse(energy_consumption_3)
    energy_consumption_5: int = spin_2(energy_consumption_4)
    print("Energy comsumption: " + str(energy_consumption_5) + " Jules")
    return energy_consumption_5


start_washing()
