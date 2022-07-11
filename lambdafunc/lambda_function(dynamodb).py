import boto3

dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    table = dynamodb.create_table(
        TableName='datatesttable',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },

        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        },
    )
    
    print("Table status", table.table_status)