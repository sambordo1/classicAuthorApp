import json

print('loading function')

def lambda_handler(event, context):
    
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
