import boto3

client = boto3.client('s3')

bucket_name='datatestbucket12'

#Bucket Name argument is mandatory and bucket name should be unique
def lambda_handler(event, context):
    response1 = client.create_bucket(
        ACL='private',
        Bucket=bucket_name
        )
    
    print(response1['Location'])
    
    tag_resp='y'
    
    if tag_resp == 'y':
        tag_key="test"
        tag_value = "s3-bucket"
        response2 = client.put_bucket_tagging(
        Bucket=bucket_name,
        Tagging={
            'TagSet': [
                {
                    'Key': tag_key,
                    'Value': tag_value
                }
            ]
        })