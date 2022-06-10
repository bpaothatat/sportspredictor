from dataclasses import dataclass

@dataclass
class Team:
    """Class for storing team data"""
    id: int
    name: str
    league: str
    division: str