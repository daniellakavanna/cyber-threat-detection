# import boto3
# import os 
# import logging
# from botocore.exceptions import ClientError

# logging.basicConfig(level=logging.DEBUG)

# def upload_file(file_name, bucket, object_name=None):
#     """Upload a file to an S3 bucket

#     :param file_name: File to upload
#     :param bucket: Bucket to upload to
#     :param object_name: S3 object name. If not specified then file_name is used
#     :return: True if file was uploaded, else False
#     """

#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = os.path.basename(file_name)

#     # Upload the file
#     s3_client = boto3.client('s3')
#     try:
#         response = s3_client.upload_file(file_name, bucket, object_name)
#         logging.info("File uploaded successfully")
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True


# if __name__ == "__main__":
#     # Set up logging

#     session = boto3.Session()
#     credentials = session.get_credentials()
#     logging.info(f"Using Access Key: {credentials.access_key}")
    
#     # Define the S3 bucket name and the model path
#     bucket_name = "threat-detection-models"
#     model_path = "models/model.pth"
#     object_name = "models/threat_detection_model_v1.pth"


#     # Upload the model to S3
#     if upload_file(model_path, bucket_name, object_name):
#         logging.info(f"Model uploaded successfully to {bucket_name}/{model_path}")
#     else:
#         logging.error("Model upload failed")