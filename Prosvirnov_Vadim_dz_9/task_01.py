import time


class TrafficLight:
    __color = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        for clr, delay in self.__color.items():
            print(f'{clr}, {delay} сек')
            time.sleep(delay)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()