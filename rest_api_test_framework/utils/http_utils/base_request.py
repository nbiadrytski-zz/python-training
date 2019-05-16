from abc import ABCMeta, abstractmethod


class BaseRequest(metaclass=ABCMeta):
    """
    Provides call abstractmethod to be implemented by child classes.
    """

    @abstractmethod
    def call(self, *args, **kwargs):
        """
        Obligatory method for each HTTP request.

        Parameters:
            args: request params, e.g. query params, headers, request_body.
            kwargs request key-value params, e.g. query params, headers, request_body.

        Raises:
            NotImplementedError: if call method is not implemented by child class.
        """
        raise NotImplementedError
