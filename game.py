from dataclasses import dataclass

@dataclass
class Game:
    id: int
    date: str
    away_id: int
    home_id: int
    away_pitcher: str
    home_pitcher: str
    away_score: int
    home_score: int
    double_header: bool

    def __hash__(self) -> int:
        return hash((self.id, self.away_id, self.home_id, self.away_pitcher, self.home_pitcher, self.away_score, self.home_score))
    

    
