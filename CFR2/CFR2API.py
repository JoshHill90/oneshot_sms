import boto3
import json
import io

class CloudflareR2API:
    
    def __init__(self, r2_token, r2_id, r2_key, r2_endpoint, r2_bucket):

        self.CFR2_TOKEN = r2_token
        self.CFR2_ACC_ID = r2_id
        self.CFR2_ACC_KEY = r2_key
        self.CFR2_ENDPOINT = r2_endpoint
        self.CFR2_BUCKET = r2_bucket

        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self.CFR2_ACC_ID,
            aws_secret_access_key=self.CFR2_ACC_KEY,
            endpoint_url=self.CFR2_ENDPOINT
        )
         
    #-------------------------------------------------------------------------------------------------------#
    # JSON Object up load fucntions
    #-------------------------------------------------------------------------------------------------------#
    # put an object:
    def put_json_object(self, json_object, path_key):

        json_data_str = json.dumps(json_object).encode("UTF-8")
        try:
            self.s3.put_object(Body=json_data_str, Bucket=self.CFR2_BUCKET, Key=path_key)
            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "exception": e}

    # read objects
    def read_r2_object(self, object_name):

        print("s3",object_name)
        try:
            resp_data = self.s3.get_object(Bucket=self.CFR2_BUCKET, Key=object_name)
            resp = resp_data["Body"].read()
            resp_da= json.loads(resp)
            return {"status": "success", "results": resp_da}
        
        except Exception as e:
            return {"status": "error", "exception": e}
        
    # Delete a object:
    def delete_r2_object(self, object_path):
        try:
            self.s3.delete_object(Bucket=self.CFR2_BUCKET, Key=object_path)
            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "exception": e}  
    
    # List objects         
    def list_r2_object(self):
        try:
            resp_data = self.s3.list_objects_v2(Bucket=self.CFR2_BUCKET)
            resp = resp_data["Contents"]
           
            return {"status": "success", "results": resp}
        except Exception as e:
            return {"status": "error", "exception": e}   
    #-------------------------------------------------------------------------------------------------------#
    # Document up load fucntions
    #-------------------------------------------------------------------------------------------------------#
    # Upload a Document:
    def upload_r2_document(self, object_name, file_path):

        self.s3.upload_file(file_path, self.CFR2_BUCKET, object_name)

    # Download a Document:
    def download_r2_document(self, object_name, download_path):

        self.s3.download_file(self.CFR2_BUCKET, object_name, download_path)

    # Update (Put) a Document:
    def update_r2_document(self, object_name, file_path):
        self.upload_r2_document(object_name, file_path) 

    # Delete a Document:
    def delete_r2_document(self, object_name):

        self.s3.delete_object(Bucket=self.CFR2_BUCKET, Key=object_name)

    # Generate Presigned URL:
    def generate_presigned_url(self, object_name, expiration=3600):

        url = self.s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.CFR2_BUCKET, 'Key': object_name},
            ExpiresIn=expiration
        )
        return url


