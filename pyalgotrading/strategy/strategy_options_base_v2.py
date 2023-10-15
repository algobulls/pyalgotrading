from pyalgotrading.strategy.strategy_base import StrategyBase
from pyalgotrading.constants import *


class OptionsStrikeDirection(Enum):
    ITM = 'ITM'
    ATM = 'ATM'
    OTM = 'OTM'


class OptionsTradingsymbolSuffix(Enum):
    CE = 'CE'
    PE = 'PE'


class OptionsExpiryKey(Enum):
    WEEKLY_CURRENT = 'WEEKLY_CURRENT'
    WEEKLY_NEXT = 'WEEKLY_NEXT'
    MONTHLY_CURRENT = 'MONTHLY_CURRENT'
    MONTHLY_NEXT = 'MONTHLY_NEXT'


class OptionsInstrumentDirection(Enum):
    EXACT = 'EXACT'
    ROUNDUP = 'ROUNDUP'
    ROUNDDOWN = 'ROUNDDOWN'


class StrategyOptionsBaseV2(StrategyBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.flag_fetch_instruments_for_expiry_weekly_current = self.strategy_parameters.get('FLAG_FETCH_INSTRUMENTS_FOR_EXPIRY_WEEKLY_CURRENT', 1)
        self.flag_fetch_instruments_for_expiry_weekly_next = self.strategy_parameters.get('FLAG_FETCH_INSTRUMENTS_FOR_EXPIRY_WEEKLY_NEXT', 0)
        self.flag_fetch_instruments_for_expiry_monthly_current = self.strategy_parameters.get('FLAG_FETCH_INSTRUMENTS_FOR_EXPIRY_MONTHLY_CURRENT', 0)
        self.flag_fetch_instruments_for_expiry_monthly_next = self.strategy_parameters.get('FLAG_FETCH_INSTRUMENTS_FOR_EXPIRY_MONTHLY_NEXT', 0)

        _ = [self.flag_fetch_instruments_for_expiry_weekly_current, self.flag_fetch_instruments_for_expiry_weekly_next,
             self.flag_fetch_instruments_for_expiry_monthly_current, self.flag_fetch_instruments_for_expiry_monthly_next]

        self.instrument_nifty_bank_string = 'NIFTY BANK'
        self.instrument_nifty_50_string = 'NIFTY 50'
        self.instrument_fin_nifty_string = 'NIFTY FIN SERVICE'
        self.instruments_list_ce = None
        self.instruments_list_pe = None
        self.instruments_ce_df = None
        self.instruments_ce_itm = None
        self.instruments_ce_atm = None
        self.instruments_ce_otm = None
        self.instruments_pe_df = None
        self.instruments_pe_itm = None
        self.instruments_pe_atm = None
        self.instruments_pe_otm = None
        self.weekly_expiry_date_current = None
        self.monthly_expiry_date_current = None
        self.weekly_expiry_date_next = None
        self.monthly_expiry_date_next = None
        self.expirykey_expirydate_map = None
        self.flag_expirydate_map = None
        self.instruments_mapper = IntrumentsMappingManager()

    def initialize(self):
        self.instruments_list_ce = {}
        self.instruments_list_pe = {}
        self.instruments_ce_df = {}
        self.instruments_ce_itm = {}
        self.instruments_ce_atm = {}
        self.instruments_ce_otm = {}
        self.instruments_pe_df = {}
        self.instruments_pe_itm = {}
        self.instruments_pe_atm = {}
        self.instruments_pe_otm = {}

    @staticmethod
    def get_options_ref_key(instrument, expiry_date):
        _expiry_date = expiry_date if isinstance(expiry_date, str) else expiry_date.strftime("%y-%m-%d")
        return f'{instrument}_{_expiry_date}'

    def initialize_instrument(self, instrument):
        pass

    def get_allowed_expiry_dates(self):
        return []

    def options_instruments_set_up(self, base_instrument, instrument_direction, expiry_date, tradingsymbol_suffix, ltp=None, apply_modulo=False, modulo_value=100):
        pass

    def get_options_instruments(self, base_instrument, expiry_date, tradingsymbol_suffix, instrument_direction, ltp, apply_modulo=False, modulo_value=100):
        instrument_details_df, instruments_itm, instrument_atm, instruments_otm = None, None, None, None
        return instrument_details_df, instruments_itm, instrument_atm, instruments_otm

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
