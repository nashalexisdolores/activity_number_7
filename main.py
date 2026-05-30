from fan import Fan

def main():
    fan1 = Fan()
    fan1.set_speed(Fan.FAST)
    fan1.set_radius(10)
    fan1.set_color("yellow")
    fan1.set_on(True)

    fan2 = Fan()
    fan2.set_speed(Fan.MEDIUM)
    fan2.set_radius(5)
    fan2.set_color("blue")
    fan2.set_on(False)

    print("--- Fan 1 ---")
    print(fan1)