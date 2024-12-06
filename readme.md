## self-signed certificate
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout myvault.key -out myvault.crt -subj "/CN=myvault" -extensions SAN -config <(cat /etc/ssl/openssl.cnf <(printf "[SAN]\nsubjectAltName=IP:0.0.0.0"))
```

## start vault in dev mode
    ```bash
    docker run --name=aavault-dev -p 8300:8200 --cap-add=IPC_LOCK -e 'VAULT_DEV_ROOT_TOKEN_ID=myroot' -e 'VAULT_DEV_LISTEN_ADDRES=http://0.0.0.0:8200' -e 'VAULT_ADDR=http://0.0.0.0:8200' hashicorp/vault
    ```
## start vault in production mode with certificate

docker network create vault-network

    ```bash
    docker run --name=aavault -p 8200:8200 --network="vault-network" --cap-add=IPC_LOCK -e 'VAULT_LOCAL_CONFIG={"listener": {"tcp": {"address": "0.0.0.0:8200", "tls_cert_file": "/vault/certs/myvault.crt", "tls_key_file": "/vault/certs/myvault.key"}}, "ui": true, "disable_mlock": "true", "backend": {"file": {"path": "/vault/data"}}}' -e 'VAULT_ADDR=https://0.0.0.0:8200' -e 'VAULT_CACERT=/vault/certs/myvault.crt' -v ./vault-certs:/vault/certs -v ./vault-data:/vault/data hashicorp/vault server
    ```

## # export VAULT_ADDR='https://0.0.0.0:8200'
## # export VAULT_CACERT=/vault/certs/myvault.crt
## # vault operator init > /vault/file/keys
## # cat /vault/file/keys 
## # vault operator unseal $(grep 'Key 1:' /vault/file/keys | awk '{print $NF}')
## # vault operator unseal $(grep 'Key 2:' /vault/file/keys | awk '{print $NF}')
## # vault operator unseal $(grep 'Key 3:' /vault/file/keys | awk '{print $NF}')
