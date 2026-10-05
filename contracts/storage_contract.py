from genlayer import *

@contract
class SmartStorage:
    data: str

    def __init__(self, initial_data: str):
        self.data = initial_data

    @public
    def set_data(self, new_data: str) -> None:
        self.data = new_data

    @public
    def get_data(self) -> str:
        return self.data
