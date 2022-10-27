import sys
import pathlib

sys.path.append(pathlib.Path().resolve().__str__())
sys.path.append(pathlib.Path().resolve().joinpath("qbay").__str__())
sys.path.append(pathlib.Path().resolve().joinpath("qbay_test").__str__())
