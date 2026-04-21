# # 포함 관계 - has-a 관계
# # Composition

class Engine():
    def __init__(self):
        pass

class Car():
    def __init__(self):
        self.engine = Engine()

if __name__ == "__main__":
    car_composited = Car()

# # Aggregation

class Engine():
    def __init__(self):
        pass

class Car():
    def __init__(self, engine: Engine):
        self.engine = engine

if __name__ == "__main__":
    engine = Engine() 
    car_aggregated = Car(engine)

# 상속 관계 - is-a 관계

class Engine():
    def __init__(self, power):
        self.power = power

    def __string__(self):
        return f"Engine with power {self.power}"

class Car(Engine):
    def __init__(self, power):
        super().__init__(power)
        self.power = 20

    def __str__(self):
        return f"Car with power - inherited {self.power}"

if __name__ == "__main__":
    car_inherited = Car(100)
    print(car_inherited)


# 의존성 - use-a 관계

class Engine():
    def __init__(self, power):
        self.power = power
    

class Car():
    def __init__(self):
        pass

    def velocity(self, engine: Engine):
        return engine.power * 2

if __name__=="__main__":
    engine = Engine(100)
    car_dependent = Car()
    velocity = car_dependent.velocity(engine)
    print(velocity)