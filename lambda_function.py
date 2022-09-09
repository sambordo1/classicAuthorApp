import json
import boto3
import random
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    
    client = boto3.resource('dynamodb')
    table = client.Table('classicAuthor')
    
    # Taking in parameters 
    
    authorName = event['queryStringParameters']['authorName']
    
    
    # Query by partition key author_name
    
    response = table.query(
        KeyConditionExpression=Key('author_name').eq(authorName)
    )
    
    # select random item in list and extract quote
    
    items = response['Items']
    selection = random.choice(tuple(items))
    for attributes in selection:
        quote = selection['quote']
        
    # construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(quote)
    
    #4. Return the response object
    return responseObject
