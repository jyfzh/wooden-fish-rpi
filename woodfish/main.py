from core import Core

if __name__ == "__main__":
    try:
        core = Core()
        core.run()
    except OSError:
        print("OSError")
        del core
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        del core
