from pinnacle.resources.baseresource import BaseResource


class SportsDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'id': 'id',
            'name': 'name',
            'hasOfferings': 'hasOfferings',
            'leagueSpecialsCount': 'leagueSpecialsCount',
            'eventSpecialsCount': 'eventSpecialsCount',
            'eventCount': 'eventCount',
        }


class CurrencyDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'code': 'code',
            'name': 'name',
            'rate': 'rate',
        }


class PeriodDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'number': 'number',
            'description': 'description',
            'shortDescription': 'shortDescription',
            'spreadDescription': 'spreadDescription',
            'moneylineDescription': 'moneylineDescription',
            'totalDescription': 'totalDescription',
            'team1TotalDescription': 'team1TotalDescription',
            'team2TotalDescription': 'team2TotalDescription',
            'spreadShortDescription': 'spreadShortDescription',
            'moneylineShortDescription': 'moneylineShortDescription',
            'totalShortDescription': 'totalShortDescription',
            'team1TotalShortDescription': 'team1TotalShortDescription',
            'team2TotalShortDescription': 'team2TotalShortDescription',
        }


class LeagueDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'id': 'id',
            'name': 'name',
            'homeTeamType': 'homeTeamType',
            'hasOfferings': 'hasOfferings',
            'allowRoundRobins': 'allowRoundRobins',
            'leagueSpecialsCount': 'leagueSpecialsCount',
            'eventSpecialsCount': 'eventSpecialsCount',
            'eventCount': 'eventCount',
        }
