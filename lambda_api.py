import json
import boto3

def lambda_handler(event, context):

    print("Recieved event:")
    print(event)

    method = event['context']['http-method']

    if method == "GET":
        dynamo_client = boto3.client('dynamodb')

        in_customerID = event['params']['querystring']['CustomerID']
        print(f"Getting data for customer ID: {in_customerID}")
        response = dynamo_client.get_item(
            TableName = 'Customers', Key = {'CustomerID':{'N': in_customerID}}
        )
        print(f"Got item: {response['Item']}")
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
           }

    elif method == "POST":
        p_record = event['body-json']
        recordstring = json.dumps(p_record)

        client = boto3.client('kinesis')
        response = client.put_record(
            StreamName='APIData',
            Data= recordstring,
            PartitionKey='string'
        )
        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }