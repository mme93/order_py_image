from webdav3.client import Client

options = {
    'webdav_hostname': 'http://212.227.165.166/webdav/',
    'webdav_login': 'root',
    'webdav_password': '!Mameie93'
}


def mkdir(remote_path):
    client = Client(options)
    client.verify = False
    if not client.check(remote_path):
        client.mkdir(remote_path)
    else:
        print("Folder already exist!")


def downloadIMG(remote_path, local_path):
    client = Client(options)
    client.verify = False
    if client.check(remote_path):
        client.download(remote_path, local_path)
    else:
        print("File not found on the remote path")


def uploadIMG(remote_path, local_path):
    client = Client(options)
    client.verify = False
    if client.check(local_path):
        client.upload(remote_path, local_path)
    else:
        print("File not found on the local path")
