
from enum import Enum


class BetType(Enum):
    MoneyLine = 'MONEYLINE'
    TeamTotal = 'TEAM_TOTAL_POINTS'
    Spread = 'SPREAD'
    Total = 'TOTAL_POINTS'


class Boolean(Enum):
    TRUE = 1
    FALSE = 0


class Side(Enum):
    Over = 'OVER'
    Under = 'UNDER'


class TeamType(Enum):
    Team1 = 'Team1'
    Team2 = 'Team2'
    Draw = 'Draw'


class BetListType(Enum):
    Settled = 'SETTLED'
    Running = 'RUNNING'
    Cancelled = 'CANCELLED'


class EventStatus(Enum):
    Unavailable = 'H'
    LowerMax = 'I'
    Open = 'O'


class OddsFormat(Enum):
    Decimal = 'DECIMAL'
    American = 'AMERICAN'
    HongKong = 'HONGKONG'
    Indonesian = 'INDONESIAN'
    Malay = 'MALAY'


class WinRiskType(Enum):
    Win = 'WIN'
    Risk = 'RISK'
