from pinnacle.resources.baseresource import BaseResource


class AccountDetails(BaseResource):
    class Meta(BaseResource.Meta):
        attributes = {
            'availableBalance': 'availableBalance',
            'outstandingTransactions': 'outstandingTransactions',
            'givenCredit': 'givenCredit',
            'currency': 'currency',
        }
