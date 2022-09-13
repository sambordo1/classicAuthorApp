#!/bin/bash

aws dynamodb batch-write-item --request-items file://../quotesByAuthor/shakespeareQuotes.json
aws dynamodb batch-write-item --request-items file://../quotesByAuthor/dickensQuotes.json
aws dynamodb batch-write-item --request-items file://../quotesByAuthor/twainQuotes.json
aws dynamodb batch-write-item --request-items file://../quotesByAuthor/AustenQuotes.json