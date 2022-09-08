import json
import boto3
import random
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    
    client = boto3.resource('dynamodb')
    table = client.Table('classicAuthors')
    
    # Get item from dynamodb by id
    
    response = table.get_item(
        Key={
            'author_id': 1 ,
            'quote_id': 1
        }
    )
    
    print(response['Item'])
    
    # Query by partition key
    
    response2 = table.query(
        KeyConditionExpression=Key('author_id').eq(1)
    )
    
    items = response2['Items']
    for item in items:
        print(item)
    
    # scan table for author name
    
    response3 = table.scan(
        FilterExpression=Attr('author_name').eq('Dickens')    
    )
    
    items = response3['Items']
    for item in items:
        print(item)
        
    selection = random.choice(tuple(items))
    print("Random selection: ")
    print(selection)
    
    
    # Taking in parameters 
    authorName = event['queryStringParameters']['authorName']
    quote = ""
    
    if authorName == 'Dickens':
        quote = 'Dickens quote'
    elif authorName == 'Shakespeare':
        quote = 'Shakespeare quote'
    else:
        quote = 'Please input Shakespeare or Dickens'
   
    #2. Construct body of response object
    
    classicAuthorResponse = {}
    classicAuthorResponse['author'] = authorName
    classicAuthorResponse['quote'] = quote

    
    #3. construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(classicAuthorResponse)
    
    #4. Return the response object
    return responseObject
