from pinnacle.resources.baseresource import BaseResource


class BetDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'betId': 'betId',
            'wagerNumber': 'wagerNumber',
            'placedAt': 'placedAt',
            'win': 'win',
            'risk': 'risk',
            'winLoss': 'winLoss',
            'betStatus': 'betStatus',
            'betType': 'betType',
            'sportId': 'sportId',
            'leagueId': 'leagueId',
            'eventId': 'eventId',
            'handicap': 'handicap',
            'price': 'price',
            'teamName': 'teamName',
            'side': 'side',
            'oddsFormat': 'oddsFormat',
            'customerCommission': 'customerCommission',
            'pitcher1': 'pitcher1',
            'pitcher2': 'pitcher2',
            'pitcher1MustStart': 'pitcher1MustStart',
            'pitcher2MustStart': 'pitcher2MustStart',
            'team1': 'team1',
            'team2': 'team2',
            'isLive': 'isLive',
            'periodNumber': 'periodNumber',
            'team1Score': 'team1Score',
            'team2Score': 'team2Score',
            'ftTeam1Score': 'ftTeam1Score',
            'ftTeam2Score': 'ftTeam2Score',
            'pTeam1Score': 'pTeam1Score',
            'pTeam2Score': 'pTeam2Score',
            'cancellationReason': 'cancellationReason',
            'updateSequence': 'updateSequence',
        }


class PlaceBetDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'status': 'status',
            'errorCode': 'errorCode',
            'betId': 'betId',
            'uniqueRequestId': 'uniqueRequestId',
            'betterLineWasAccepted': 'betterLineWasAccepted',
            'price': 'price',
        }


class PlaceSpecialBetDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'status': 'status',
            'errorCode': 'errorCode',
            'betId': 'betId',
            'uniqueRequestId': 'uniqueRequestId',
            'betterLineWasAccepted': 'betterLineWasAccepted',
        }
