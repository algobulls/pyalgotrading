from pyalgotrading.strategy.strategy_base import StrategyBase
from pyalgotrading.constants import *


class StrategyOptionsBaseV2(StrategyBase):
    """
    Dummy placeholder class. Here to ensure all required methods are implemented and as per requirements.

    Once uploaded, this strategy will be replaced with the real base class strategy
    """

    @staticmethod
    def get_options_ref_key(instrument, expiry_date):
        pass

    def initialize_instrument(self, instrument):
        pass

    def get_allowed_expiry_dates(self):
        """
        Gives the allowed expiry date, depending on the selection of monthly expiry or weekly expiry.
        Checkout the documentation to understand in more detail
        """
        return []

    def options_instruments_set_up(self, base_instrument, instrument_direction, expiry_date, tradingsymbol_suffix, ltp=None, apply_modulo=False, modulo_value=100):
        pass

    def get_options_instruments(self, base_instrument, expiry_date, tradingsymbol_suffix, instrument_direction, ltp, apply_modulo=False, modulo_value=100):
        pass

    def get_options_instrument_with_strike_direction(self, base_instrument, expiry_date, tradingsymbol_suffix, strike_direction, no_of_strikes):
        instrument = None
        return instrument


class IntrumentsMappingManager:
    def __init__(self):
        self.base_instrument_to_instrument_map_list = {}
        self.instrument_to_base_instrument_map = {}

    def add_mappings(self, base_instrument, child_instruments):
        pass

    def is_base_instrument(self, instrument):
        return

    def is_child_instrument(self, instrument):
        return

    def get_base_instrument(self, instrument):
        return

    def get_child_instruments_list(self, instrument):
        return


class OrderTagManager:

    def add_order(self, order, tags=None):
        """
        Adds an order to tags extracted from the order object as well as given tags (if any)
        """
        return

    # take 1 or more tags; return 1 or more items if many=True; return only 1 item if many=False;
    def get_orders(self, tags, many=False, ignore_errors=False):
        """
        Takes 1 or more tags; returns 1 or more orders if many=True; returns only 1 order if many=False
        """
        return

    def remove_tags(self, tags):
        """
        Removes 1 or more tags from the data structure
        """
        return

    def remove_order(self, order):
        """
        Removes an order from the data structure
        """
        return

    def get_internals(self):
        """
        Returns the complete data structure
        The developer should use this for debugging, but remove its usages before finalizing
        """
        return
