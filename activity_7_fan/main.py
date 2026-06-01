from activity_7_fan import fan_class

def main():
    fan_one = fan_class()
    fan_one.set_speed(fan_class.FAST)
    fan_one.set_radius(10)
    fan_one.set_color("yellow")
    fan_one.set_on(True)

    fan_two = fan_class()
    fan_two.set_speed(fan_class.MEDIUM)
    fan_two.set_radius(5)
    fan_two.set_color("blue")
    fan_two.set_on(False)

    print("--- Object 1 ---")
    print(fan_one)
    
    print("\n--- Object 2 ---")
    print(fan_two)

if __name__ == "__main__":
    main()