# SSLCOMMERZ Payment Gateway implementation in Python
Provides a python module to implement payment gateway in python based web apps.

## Projected use
```python
from sslcommerz_python import SSLCPayment

mypayment = SSLCPayment(sslc_is_sandbox=False, sslc_store_id='your_sslc_store_id', sslc_store_pass='your_sslc_store_passcode')

mypayment.set_urls(success_url='example.com/success', fail_url='example.com/failed', cancel_url='example.com/cancel', ipn_url='example.com/payment_notification')

mypayment.set_product_integration(total_amount=Decimal('20.20'), currency='BDT', product_category='clothing', product_name='demo-product', product_profile='None')

mypayment.set_customer_info(name='John Doe', email='johndoe@email.com', address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')
```
