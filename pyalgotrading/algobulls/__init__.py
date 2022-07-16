"""
Package for interacting with the [AlgoBulls](https://www.algobulls.com) backend
"""

from .connection import AlgoBullsConnection

MESSAGE_REALTRADING_FORBIDDEN = 'Forbidden. As per the new policy, directly running a strategy in RT mode is prohibited. ' \
                                'To run this strategy in RT mode, you need to get an approval. You can get an approval for your strategy by writing to support@algobulls.com. ' \
                                'Once approved, you can START the strategy in REALTRADING mode directly from the website. The AlgoBulls support team will guide you for a process on the same.'
