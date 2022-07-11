# ETLPROCESS
We have a lambdafunction.yaml CloudFormation file that is use to create 3 different lambda function which are:
    - data_load_trigger
    - s3_bucket
    - dynamo_db
    - IamRrole

you will need to create stack on cloudformation in other to create the lambda function.

data_load_trigger: This lambda function get data from your s3 bucket and load it into your dynamodb. 
this lambda function will be set to trigger whenever you drop specific in object in your s3 bucket.
s3_bucket: This lambda function will create a s3 bucket(datatestbucket12) where were your csv file will be stored.
dynamo_db: This lambda function will create a dynamodb service where the csv data will be ingested. 
IAM Role: This will create an IAM role that will be used by the 3 lambda function.

Note: A folder(s3_bucket_zip_file) is where the zip file for the python code that works for each lambda function lives, you can also find sample
of such data in this folder(lambdafunc).

ETL:
Once, csv file is uploaded into your s3 bucket this will trigger lambda function(data_load_trigger), which will get the data and load the data into your dynamodb.

link for reference https://dheeraj3choudhary.com/aws-lambda-and-s3or-automate-csv-file-processing-from-s3-bucket-and-push-in-dynamodb-using-lambda-python
