import os
from pathlib import Path
from dotenv import load_dotenv

current_dir = Path(__file__).resolve().parent		
ven = current_dir / ".env"
load_dotenv(ven)

class EmailAuth:
	email_sender = os.getenv("WC_EMAIL_USER")
	email_passwd = os.getenv('WC_EMAIL_PASSWORD')
	email_host = os.getenv('WC_EMAIL_HOST')
	email_port = os.getenv('WC_EMAIL_PORT')
	email_imap_host = os.getenv('IMAP_HOST')
	email_imap_port = os.getenv('IMAP_PORT')

class CloudFlareCDN:
	cdn_key = os.getenv('WC_CFCDN_KEY')
	cdn_name =os.getenv('WC_CFCDN_NAME')
	cdn_id =os.getenv('WC_CFCDN_ID')
 
	
class CloudFlareR2:
	r2_token = os.getenv('WC_CFR2_TOKEN')
	r2_id = os.getenv('WC_CFR2_ACC_ID')
	r2_key = os.getenv('WC_CFR2_ACC_KEY')
	r2_endpoint = os.getenv('WC_CFR2_ENDPOINT')
	r2_bucket = os.getenv('WC_CFR2_BUCKET')

class SQLServer:
	db_host = os.getenv('WC_DB_HOST')
	db_user = os.getenv('WC_DB_USER')
	db_passwd = os.getenv('WC_DB_PSSWORD')
	db_name = os.getenv('WC_DB_NAME')

class CloudFlareAnalytics:
    gql_token = os.getenv('GQL_TOKEN')
    cf_core_token = os.getenv('CF_CORE_TOKEN')
    cf_core_key = os.getenv('CF_CORE_KEY')
    
class APItoken:
    api_name = os.getenv('WC_API_NAME')
    api_key = os.getenv('WC_API_KEY')
    api_layer_key = os.getenv("API_LAYER_KEY")