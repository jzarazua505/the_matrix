class MovieWatcher:
    def __init__(self):  
        self.front = None

class MovieColumn:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_seat = self.head
        out_string = ""
        while current_seat is not None:
            out_string += "o    "
            current_seat = current_seat.front
        out_string += "\n"
        current_seat = self.head
        while current_seat is not None:
            out_string += "∩ -> "
            current_seat = current_seat.front
        out_string += "SCREEN"
        return out_string

    def add_watcher(self, new_watcher):
        new_watcher.front = self.head
        self.head = new_watcher

if __name__ == "__main__":
    mc = MovieColumn()
    mc.add_watcher(MovieWatcher())
    print(mc)
    mc.add_watcher(MovieWatcher())
    mc.add_watcher(MovieWatcher())
    mc.add_watcher(MovieWatcher())
    print(mc)
