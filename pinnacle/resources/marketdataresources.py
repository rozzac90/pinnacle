from pinnacle.resources.baseresource import BaseResource


class FixtureDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'sportId': 'sportId',
            'last': 'last',
            'leagues': 'leagues',
        }


class SettledFixtureDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'sportId': 'sportId',
            'last': 'last',
            'leagues': 'leagues',
        }


class SpecialFixtureDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'sportId': 'sportId',
            'last': 'last',
            'leagues': 'leagues',
        }


class SettledSpecialFixtureDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'sportId': 'sportId',
            'last': 'last',
            'leagues': 'leagues',
        }


class OddsDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'sportId': 'sportId',
            'last': 'last',
            'leagues': 'leagues',
        }


class SpecialOddsDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'sportId': 'sportId',
            'last': 'last',
            'leagues': 'leagues',
        }


class LineDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'status': 'status',
            'price': 'price',
            'lineId': 'lineId',
            'altLineId': 'altLineId',
            'team1Score': 'team1Score',
            'team2Score': 'team2Score',
            'team1RedCards': 'team1RedCards',
            'team2RedCards': 'team2RedCards',
            'maxRiskStake': 'maxRiskStake',
            'minRiskStake': 'minRiskStake',
            'maxWinStake': 'maxWinStake',
            'minWinStake': 'minWinStake',
            'effectiveAsOf': 'effectiveAsOf',
        }


class SpecialLineDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'status': 'status',
            'price': 'price',
            'lineId': 'lineId',
            'specialId': 'specialId',
            'contestantId': 'contestantId',
            'handicap': 'handicap',
            'maxRiskStake': 'maxRiskStake',
            'minRiskStake': 'minRiskStake',
            'maxWinStake': 'maxWinStake',
            'minWinStake': 'minWinStake',
        }


class InRunningDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'sports': 'sports',
        }
