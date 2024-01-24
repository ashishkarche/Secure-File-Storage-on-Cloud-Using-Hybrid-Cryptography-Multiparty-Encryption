from Encrypt import *
from IVsKeys import *
import threading

def HybridCrypt():
    iv1, iv2 = generateIV()
    key1, key2 = generateKey()
    HybridCryptKeys()

    # Upload encrypted file segments to Google Cloud Storage
    # client = storage.Client()
    # bucket = client.bucket('your-cloud-bucket-name')

    # for i in range(0, 3):
    #     segment_name = str(i) + ".txt"
    #     blob_segment = bucket.blob(segment_name)
    #     blob_segment.upload_from_filename(os.path.join(os.getcwd() + "/Segments", segment_name))
        
    # Display encryption information on the command line
    print("Encryption Information:")
    print(f"IV1: {iv1}")
    print(f"IV2: {iv2}")
    print(f"Key1: {key1}")
    print(f"Key2: {key2}")

    t1 = threading.Thread(target=AES, args=(key1, iv1,))
    t2 = threading.Thread(target=RSA, args=(key1, iv2,))
    t3 = threading.Thread(target=TrippleDES, args=(key1, iv2,))

    # Starting the Encryption Process
    t1.start()
    t2.start()
    t3.start()

    # Thread Sync.
    t1.join()
    t2.join()
    t3.join()  



	
