class Device:
    def __inti__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name!r} ({self.connected_by})'

    def disconnected(self):
        self.connected = False
        print('Disconnected.')


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__inti__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining)'

    def print(self, pages):
        if not self.connected:
            print('Your printer is not connected dude')
        else:
            print(f'Printing {pages} pages')
            self.remaining_pages -= pages


printer = Printer('Adams Printer', 'USB', 20)
printer.print(5)
print(printer)
printer.disconnected()
printer.print(1)