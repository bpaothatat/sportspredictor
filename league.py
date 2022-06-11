from dataclasses import dataclass

@dataclass
class League:
    id: int
    name: str
    division_id: int
    division_name: str

    def __hash__(self) -> int:
        return hash((self.id, self.name, self.division_id, self.division_name))