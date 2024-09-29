import hvac

# Connect to the Vault server
client = hvac.Client(
    url='https://0.0.0.0:8200',
    token='hvs.H6HX0CKDs5HsoLXIVPcTaLdt',
    verify='./vault-certs/myvault.crt',
)

# Retrieve the secret from the path
secret = client.secrets.kv.v2.read_secret_version(path='test/project2')
# Access the secret data
data = secret['data']['data']

# Print the secret value
print(data)

# Modify the secret value
# data['key'] = 'new_value'

# Update the secret in Vault
# client.secrets.kv.v2.create_or_update_secret(path='secret/test', secret=data)