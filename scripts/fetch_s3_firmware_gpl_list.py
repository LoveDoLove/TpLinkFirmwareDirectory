import boto3
from botocore.handlers import disable_signing
import tarfile
import os

def export_gpl_source_list_s3(bucket_name, object_key, export_dir):
    # Create S3 resource and disable signing
    s3 = boto3.resource('s3')
    s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
    bucket = s3.Bucket(bucket_name)
    # Download the tar.gz file
    local_filename = os.path.basename(object_key)
    bucket.download_file(object_key, local_filename)
    # Export file list
    os.makedirs(export_dir, exist_ok=True)
    base_name = os.path.splitext(local_filename)[0]
    # Use bucket and object path for better naming
    safe_object_key = object_key.replace('/', '_')
    export_txt = os.path.join(export_dir, f"{bucket_name}_{safe_object_key}_filelist.txt")
    with tarfile.open(local_filename, "r:gz") as tar:
        with open(export_txt, "w", encoding="utf-8") as f:
            for member in tar.getmembers():
                f.write(member.name + "\n")
    print(f"Exported file list to: {export_txt}")

if __name__ == "__main__":
    # Example usage for ArcherC5v_GPL.tar.gz in S3
    export_gpl_source_list_s3(
        'static.tp-link.com',
        'upload/gpl-code/2022/202209/20220902/ArcherC5v_GPL.tar.gz',
        'lists'
    )
