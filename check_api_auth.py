import boto3

client = boto3.client('apigateway', region_name='us-west-2')

for item in client.get_rest_apis(limit=500)["items"]:
  for resources in client.get_resources(restApiId=item["id"])["items"]:
    if 'resourceMethods' in resources:
      method = list(resources['resourceMethods'].keys() - {'OPTIONS'})
      for m in method:
        response = client.get_method(restApiId=item["id"],resourceId=resources['id'],httpMethod=m)
        if response['apiKeyRequired'] == False and response['authorizationType'] == 'NONE':
          print("No authentication for API GW " + item["name"] + ' resource path ' + resources['path'] )
    else:
      pass
