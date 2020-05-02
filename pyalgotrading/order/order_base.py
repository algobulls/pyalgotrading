from abc import ABCMeta


class OrderBase(metaclass=ABCMeta):

    def get_order_status(self):
        pass

    def exit_position(self):
        pass

    def cancel_order(self):
        pass
