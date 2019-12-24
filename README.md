# SSLCOMMERZ Payment Gateway implementation in Python
Provides a python module to implement payment gateway in python based web apps.

## Projected use
```python
from sslcommerz_python import SSLCPayment

mypayment = SSLCPayment(sslc_is_sandbox=False, sslc_store_id='your_sslc_store_id', sslc_store_pass='your_sslc_store_passcode')

set_integration(total_amount=Decimal('20.20'), currency='BDT', product_category='clothing', success_url='example.com/success', fail_url='fail.com', cancel_url='cancel.com', ipn_url='ipn.com')
```
