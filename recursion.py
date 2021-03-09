from theater import MovieWatcher, MovieColumn

def row_num(movie_watcher):
    if movie_watcher.front == None:
        return 1
    return row_num(movie_watcher.front) + 1

def hello(num):
    if num == 0:
        return
    hello(num - 1)
    print("hello")

def power(num, exp):
    if exp == 0:
        return 1
    if num == 0:
        return 0
    if num == 1:
        return 1
    if exp == 1:
        return num
    return num * power(num, exp - 1)

if __name__ == "__main__":
    mc = MovieColumn()
    mc.add_watcher(MovieWatcher())
    print(mc)
    mw = MovieWatcher()
    mc.add_watcher(mw)
    mc.add_watcher(MovieWatcher())
    mc.add_watcher(MovieWatcher())
    print(mc)
    print(row_num(mc.head))
    print(row_num(mw))
    