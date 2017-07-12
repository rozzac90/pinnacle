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