"""PortKeeper (Python) 진입점.

레포 루트에서 실행한다: ``python main.py``
"""
from portkeeper.app import PortKeeperApp


def main() -> None:
    PortKeeperApp().run()


if __name__ == "__main__":
    main()
