from typing import Dict

import _constants as const


class SSLCPayment:
    sslc_is_sandbox : bool
    sslc_store_id : str
    sslc_store_pass : str
    sslc_mode_name : str

    def __init__(self, sslc_is_sandbox=True, sslc_store_id='', sslc_store_pass='') -> None:
        self.sslc_mode_name = self.set_sslcommerz_mode(sslc_is_sandbox)
        self.sslc_is_sandbox = sslc_is_sandbox
        self.sslc_store_id = sslc_store_id
        self.sslc_store_pass = sslc_store_pass
        self.sslc_session_api = 'https://' + self.sslc_mode_name + '.' + const.SSLCZ_SESSION_API
        self.sslc_validation_api = 'https://' + self.sslc_mode_name + '.' + const.SSLCZ_VALIDATION_API

    @staticmethod
    def set_sslcommerz_mode(sslc_is_sandbox: bool) -> str:
        if sslc_is_sandbox is True or sslc_is_sandbox == 1:
            return 'sandbox'
        else:
            return 'securepay'