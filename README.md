# bcrypt-api
Small flask app to generate hash pw with py-bcrypt 

### Usage

Once Container is running:

```bash 
$ curl -XGET http://localhost:5000/pwdncrypt/<your_password>
```

*Notes:*
- If you bind the port to a diff port make sure to update the url 
- The salt log_rounds is hardcoded to 4 

i.e 

```bash 
$ curl -XGET http://localhost:5000/pwdncrypt/password
$04$FCDjDCjTjkZNfYSaD9OS..aZyMzca7wZyKrWPtrHlt01qKNCb2Y5m
```

### DockerHub

Docker Hub: [wcampos]("https://hub.docker.com/r/wcampos/bcrypt-api/")

```bash
docker pull wcampos/bcrypt-api
```
