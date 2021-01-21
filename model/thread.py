from threading import Thread


class Thread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        count = 0
        for x in range(10):
            count += 1
            print(self.name, ':', count)