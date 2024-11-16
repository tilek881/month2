class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value


    def make_computations(self):
        result = self.__cpu * self.__memory
        return f"Результат вычислений: {result}"


    def __str__(self):
        return f"Компьютер с CPU: {self.__cpu} и памятью: {self.__memory}"


    def __eq__(self, other):
        if isinstance(other, Computer):
            return self.__memory == other.memory
        return False

    def __lt__(self, other):
        if isinstance(other, Computer):
            return self.__memory < other.memory
        return False

    def __le__(self, other):
        if isinstance(other, Computer):
            return self.__memory <= other.memory
        return False

    def __gt__(self, other):
        if isinstance(other, Computer):
            return self.__memory > other.memory
        return False

    def __ge__(self, other):
        if isinstance(other, Computer):
            return self.__memory >= other.memory
        return False

    def __ne__(self, other):
        if isinstance(other, Computer):
            return self.__memory != other.memory
        return True


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value


    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number]
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number + 1} - {sim_card}")


    def __str__(self):
        return f"Телефон с сим-картами: {', '.join(self.__sim_cards_list)}"



class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)


    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")


    def __str__(self):
        return f"Смартфон с CPU: {self.cpu}, памятью: {self.memory} и сим-картами: {', '.join(self.sim_cards_list)}"



computer = Computer(cpu=5.0, memory=20)
phone = Phone(sim_cards_list=["Beeline", "MTS"])
smartphone1 = SmartPhone(cpu=2.8, memory=8, sim_cards_list=["Beeline", "Megafon"])
smartphone2 = SmartPhone(cpu=3.0, memory=12, sim_cards_list=["MTS", "Tele2"])


print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


print(computer.make_computations())
phone.call(0, "+996 705 87 98 29")
smartphone1.use_gps("Bishkek")


print(computer == phone)  # False
print(computer > smartphone1)  # True