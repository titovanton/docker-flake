import subprocess

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


def run_flake(event):
    cmd = ['flake8',  '--config', '/watch_dir/setup.cfg', event.src_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    print(result.stdout.decode())
    print("-----")


class Watcher:
    def __init__(self, path):
        self.path = path

    def run(self):
        event_handler = PatternMatchingEventHandler(patterns=["*.py"])
        event_handler.on_modified = run_flake
        observer = Observer()
        observer.schedule(event_handler, self.path, recursive=True)
        observer.start()
        observer.join()


if __name__ == '__main__':
    watcher = Watcher('/watch_dir')
    watcher.run()
