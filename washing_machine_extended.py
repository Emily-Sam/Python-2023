def pump_water(
    accumulated_energy_consumption: int, accumulated_time: int, is_eco_mode: bool
) -> tuple[int, int]:
    print("Pump water: 10 minutes")
    energy_consumption: int
    if is_eco_mode:
        energy_consumption = 5
    else:
        energy_consumption = 5
    return (accumulated_energy_consumption + energy_consumption, accumulated_time + 10)


def spin_1(
    accumulated_energy_consumption: int, accumulated_time: int, is_eco_mode: bool
) -> tuple[int, int]:
    print("Spin: 5 minutes")
    energy_consumption: int
    if is_eco_mode:
        energy_consumption = 15
    else:
        energy_consumption = 15
    return (accumulated_energy_consumption + energy_consumption, accumulated_time + 5)


def heat_water(
    accumulated_energy_consumption: int, accumulated_time: int, is_eco_mode: bool
) -> tuple[int, int]:
    print("Heat water: 20 minutes")
    energy_consumption: int
    if is_eco_mode:
        energy_consumption = 900
    else:
        energy_consumption = 1300
    return (accumulated_energy_consumption + energy_consumption, accumulated_time + 20)


def rinse(
    accumulated_energy_consumption: int, accumulated_time: int, is_eco_mode: bool
) -> tuple[int, int]:
    print("Rinse: 15 minutes")
    energy_consumption: int
    if is_eco_mode:
        energy_consumption = 40
    else:
        energy_consumption = 80
    return (accumulated_energy_consumption + energy_consumption, accumulated_time + 15)


def spin_2(
    accumulated_energy_consumption: int, accumulated_time: int, is_eco_mode: bool
) -> tuple[int, int]:
    print("Spin: 40 minutes")
    energy_consumption: int
    if is_eco_mode:
        energy_consumption = 800
    else:
        energy_consumption = 500
    return (accumulated_energy_consumption + energy_consumption, accumulated_time + 40)


def start_washing() -> int:
    mode: str = input("Type 'e' for eco mode, otherwise normal mode:")

    is_eco_mode: bool = mode == "e"

    tuple_1: int = pump_water(0, 0, is_eco_mode)
    tuple_2: int = spin_1(tuple_1[0], tuple_1[1], is_eco_mode)
    tuple_3: int = heat_water(tuple_2[0], tuple_2[1], is_eco_mode)
    tuple_4: int = rinse(tuple_3[0], tuple_3[1], is_eco_mode)
    tuple_5: int = spin_2(tuple_4[0], tuple_4[1], is_eco_mode)
    print(
        "Energy comsumption: "
        + str(tuple_5[0])
        + " Jules, duration: "
        + str(tuple_5[1])
        + " minutes."
    )
    return tuple_5


start_washing()
