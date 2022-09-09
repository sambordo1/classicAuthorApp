#!/bin/bash

aws lambda update-function-code  --function-name classicAuthorApp  --zip-file fileb://lambda_function.py.zip  --region "us-east-1"