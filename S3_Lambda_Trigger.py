# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:55:38 2018

This program is supposed to trigger the lambda function if there is an object uploaded to the identified S3

Taken from Building Serverless Applications using Python by Jalem Raj Purohit, Pakt Publishing

@author: sramesh
"""

from __future__ import print_function
import json
import urllib
import boto3
import botocore.client import Config

print('loading Function')
sts_client = boto3.client('sts', use_ssl=True)

ObjectRole = sts_client.assume_role(RoleArn="arn:aws:iam::080983167913:role/service-role/objectrole",RoleSessionName="AssumeRoleSession1")

credentials = assumedRoleObject['Credentials']
region = 'us-east-1'

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        session = boto3.session(credentials['AccessKeyID'], credentials['SecretAccessKey'], aws_session_token=credentials['SessionToken'], region_name=region)
        s3 = session.resource('s3', config=Config(signature_version='s3v4'), use_ssl=True)
        client = session.client('s3', config=Config(signature_version = 's3v4'), use_ssl=True)
        response = client.list_objects(Bucket=bucket)
        destination_bucket = 'reciever-bucket'
        source_bucket = 'sender-bucket'
        keys = []
        if 'Contents' in response:
        	for item in response['Contents']:
        		keys.append(item['Key']);

        for key in keys:
        	path = source_bucket + '/' + key
        	print(key)
        s3.Object(destination_bucket, key).copy_from(CopySource=path)

        Exception as e:
            print(e)
        print('Error getting object {} from bucket {}'.format(key,bucket))
        raise e



        