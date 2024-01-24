import os
from cryptography.hazmat.primitives import serialization
from google.cloud import storage
from user import *

# def save_user(username, password):
#     user = User(username, password)

#     # Save user information to Google Cloud Storage
#     client = storage.Client()
#     bucket = client.bucket('your-cloud-bucket-name')
#     blob_user = bucket.blob(f'users/{username}.txt')
#     blob_user.upload_from_string(f'{user.username}\n{user.password_hash}')

# def authenticate_user(username, password):
#     # Retrieve user information from Google Cloud Storage
#     client = storage.Client()
#     bucket = client.bucket('your-cloud-bucket-name')
#     blob_user = bucket.blob(f'users/{username}.txt')

#     try:
#         user_data = blob_user.download_as_text().split('\n')
#         stored_username, stored_password_hash = user_data[0], user_data[1]

#         if stored_username == username and hashlib.sha256(password.encode()).hexdigest() == stored_password_hash:
#             return True
#     except Exception as e:
#         print(f"Error: {e}")

#     return False


def generateIV():
	iv1 = os.urandom(16)
	iv2 = os.urandom(8)
	f=open(os.path.join(os.getcwd()+"/Infos",'IV.txt'),'wb')
	f.write(iv1)
	f.write(b"::::")
	f.write(iv2)
	f.close()
	return iv1,iv2

def generateKey():
	key1 = os.urandom(16)
	key2 = os.urandom(32)
	f=open(os.path.join(os.getcwd()+"/Infos",'KEY1.txt'),'wb')
	f.write(key1)
	f.close()
	f=open(os.path.join(os.getcwd()+"/Infos",'KEY2.txt'),'wb')
	f.write(key2)
	f.close()
	return key1,key2
	
	# client = storage.Client()
	# bucket = client.get_bucket('your-cloud-bucket-name')
	# blob_key1 = bucket.blob('KEY1.txt')
	# blob_key1.upload_from_filename(os.path.join(os.getcwd(), "Infos", 'KEY1.txt'))
	# blob_key2 = bucket.blob('KEY2.txt')
	# blob_key2.upload_from_filename(os.path.join(os.getcwd(), "Infos", 'KEY2.txt'))



def FetchIV():
	f=open(os.path.join(os.getcwd()+"/Infos",'IV.txt'),'rb')
	cont=f.read()
	f.close()
	iv=cont.split(b"::::")
	return iv

def FetchKey():
	# client = storage.Client()
	# bucket = client.get_bucket('your-cloud-bucket-name')

	# blob_key1 = bucket.blob('KEY1.txt')
	# blob_key1.download_to_filename(os.path.join(os.getcwd(), "Infos", 'KEY1.txt'))

	# blob_key2 = bucket.blob('KEY2.txt')
	# blob_key2.download_to_filename(os.path.join(os.getcwd(), "Infos", 'KEY2.txt'))

	f=open(os.path.join(os.getcwd()+"/Infos",'KEY1.txt'),'rb')
	key1=f.read()
	f.close()
	f=open(os.path.join(os.getcwd()+"/Infos",'KEY2.txt'),'rb')
	key2=f.read()
	f.close()
	return key1,key2

def save_IV_and_key(iv1, iv2, key1, key2):
    # Save IV1 to file
    with open(os.path.join(os.getcwd(), "Infos", 'IV1.txt'), 'wb') as f:
        f.write(iv1)

    # Save IV2 to file
    with open(os.path.join(os.getcwd(), "Infos", 'IV2.txt'), 'wb') as f:
        f.write(iv2)

    # Save Key1 to file
    with open(os.path.join(os.getcwd(), "Infos", 'Key1.txt'), 'wb') as f:
        f.write(key1)

    # Save Key2 to file
    with open(os.path.join(os.getcwd(), "Infos", 'Key2.txt'), 'wb') as f:
        f.write(key2)

# Upload IV1 to Google Cloud Storage
    # client = storage.Client()
    # bucket = client.bucket('your-cloud-bucket-name')
    # blob_iv1 = bucket.blob('IV1.txt')
    # blob_iv1.upload_from_filename(os.path.join(os.getcwd(), "Infos", 'IV1.txt'))

    # # Upload IV2 to Google Cloud Storage
    # blob_iv2 = bucket.blob('IV2.txt')
    # blob_iv2.upload_from_filename(os.path.join(os.getcwd(), "Infos", 'IV2.txt'))

    # # Upload Key1 to Google Cloud Storage
    # blob_key1 = bucket.blob('Key1.txt')
    # blob_key1.upload_from_filename(os.path.join(os.getcwd(), "Infos", 'Key1.txt'))

    # # Upload Key2 to Google Cloud Storage
    # blob_key2 = bucket.blob('Key2.txt')
    # blob_key2.upload_from_filename(os.path.join(os.getcwd(), "Infos", 'Key2.txt'))