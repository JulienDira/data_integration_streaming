from pyspark.sql.types import StructType, StringType, DoubleType, StructField, IntegerType

def get_table_schema(table_name: str):
    
    schema = {
        'ALL_TRANSACTIONS_ANONYMIZED':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True)
        ]),

        'ALL_TRANSACTIONS_FLATTENED':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID", StringType(), True),
            StructField("USER_NAME", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("DEVICE_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True)
        ]),

        'TRANSACTIONS_BLACKLIST':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True),
            StructField("AMOUNT_USD", DoubleType(), True)
        ]),

        'TRANSACTIONS_CANCELLED':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True),
            StructField("AMOUNT_USD", DoubleType(), True)
        ]),

        'TRANSACTIONS_COMPLETED':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True),
            StructField("AMOUNT_USD", DoubleType(), True)
        ]),

        'TRANSACTIONS_CONVERTED_CLEANED':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True),
            StructField("AMOUNT_USD", DoubleType(), True)
        ]),

        'TRANSACTIONS_CONVERTED':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True),
            StructField("AMOUNT_USD", DoubleType(), True)
        ]),

        'TRANSACTIONS_FAILED':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True),
            StructField("AMOUNT_USD", DoubleType(), True)
        ]),

        'TRANSACTIONS_IMPORTANTES_700':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True)
        ]),

        'TRANSACTIONS_PENDING':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True),
            StructField("AMOUNT_USD", DoubleType(), True)
        ]),

        'TRANSACTIONS_PROCESSING':
        StructType([
            StructField("TRANSACTION_ID", StringType(), True),
            StructField("TIMESTAMP", StringType(), True),
            StructField("USER_ID_HASHED", StringType(), True),
            StructField("USER_NAME_HASHED", StringType(), True),
            StructField("PRODUCT_ID", StringType(), True),
            StructField("AMOUNT", DoubleType(), True),
            StructField("CURRENCY", StringType(), True),
            StructField("TRANSACTION_TYPE", StringType(), True),
            StructField("STATUS", StringType(), True),
            StructField("CITY", StringType(), True),
            StructField("COUNTRY", StringType(), True),
            StructField("PAYMENT_METHOD", StringType(), True),
            StructField("PRODUCT_CATEGORY", StringType(), True),
            StructField("QUANTITY", IntegerType(), True),
            StructField("SHIPPING_STREET", StringType(), True),
            StructField("SHIPPING_ZIP", StringType(), True),
            StructField("SHIPPING_CITY", StringType(), True),
            StructField("SHIPPING_COUNTRY", StringType(), True),
            StructField("DEVICE_OS", StringType(), True),
            StructField("DEVICE_BROWSER", StringType(), True),
            StructField("MASKED_IP", StringType(), True),
            StructField("CUSTOMER_RATING", IntegerType(), True),
            StructField("DISCOUNT_CODE", StringType(), True),
            StructField("TAX_AMOUNT", DoubleType(), True),
            StructField("THREAD", IntegerType(), True),
            StructField("MESSAGE_NUMBER", IntegerType(), True),
            StructField("TIMESTAMP_OF_RECEPTION_LOG", StringType(), True),
            StructField("AMOUNT_USD", DoubleType(), True)
        ])
    }
    return schema.get(table_name)