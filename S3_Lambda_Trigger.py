# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:55:38 2018

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
        