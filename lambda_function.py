import json

print('loading function')

def lambda_handler(event, context):
    
    #1. Parse out query string params
    authorId = event['queryStringParameters']['authorId']
    authorName = event['queryStringParameters']['authorName']
    quote = event['queryStringParameters']['quote']

    print('authorId = ' + authorId)
    print('authorName = ' + authorName)
    print('quote = ' + quote)
    
    
    #2. Construct body of response object
    
    classicAuthorResponse = {}
    classicAuthorResponse['authorId'] = authorId
    classicAuthorResponse['authorName'] = authorName
    classicAuthorResponse['quote'] = quote
    
    #3. construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(classicAuthorResponse)
    
    #4. Return the response object
    return responseObject
