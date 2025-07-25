import boto3
from botocore.handlers import disable_signing

def list_all_s3_objects(bucket_name):
    # Create S3 resource and disable signing
    s3 = boto3.resource('s3')
    s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
    bucket = s3.Bucket(bucket_name)
    
    # Use paginator for stability and performance
    client = boto3.client('s3')
    client.meta.events.register('choose-signer.s3.*', disable_signing)
    paginator = client.get_paginator('list_objects_v2')
    
    with open('all_keys.txt', 'w', encoding='utf-8') as f:
        for page in paginator.paginate(Bucket=bucket_name):
            for obj in page.get('Contents', []):
                key = obj['Key']
                print(key, flush=True)
                f.write(key + '\n')
                f.flush()

if __name__ == "__main__":
    list_all_s3_objects('download.tplinkcloud.com')
