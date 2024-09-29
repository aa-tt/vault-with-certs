import hvac

# Connect to the Vault server
client = hvac.Client(url='http://localhost:8300')

# Authenticate to the Vault server (if needed)
client.token = 'myroot'

# Retrieve the secret from the path
secret = client.secrets.kv.v2.read_secret_version(path='test/project1')

# Access the secret data
data = secret['data']['data']

# Print the secret value
print(data)
# Access the secret value
print(data)




























# Modify the secret value
# data['key'] = 'new_value'

# Update the secret in Vault
# client.secrets.kv.v2.create_or_update_secret(path='secret/test', secret=data)