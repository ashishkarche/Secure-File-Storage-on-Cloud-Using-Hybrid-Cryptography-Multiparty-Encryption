# File Encryptor

This is a simple file encryption application using Tkinter for the GUI and Python for the backend. It allows users to upload a file, encrypt it, and view encryption details.

## How to Run the Project

1. Make sure you have Python installed on your machine.


2. Navigate to the project directory:

    ```bash
    cd FileName
    ```

3. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the main script:

    ```bash
    python app.py
    ```

5. The GUI should appear, allowing you to upload a file and perform encryption.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Algorithm Working and Detail Information

The encryption algorithm used in this project is a hybrid approach using multiple cryptographic algorithms:
 `AES (Advanced Encryption Standard), RSA, and TripleDES`. The application generates random Initialization Vectors (IVs) and keys for each algorithm during the encryption process. The encryption details, including IVs and keys, are displayed in the GUI log.

The encryption process involves dividing the input file into segments, encrypting each segment separately using different algorithms, and merging them back together. The generated IVs and keys are saved to files for decryption.

This hybrid encryption approach enhances the security of the file encryption process.

# `Multiparty Method` - 
### The Three Most Common Types of Homomorphic Encryption ###
Encrypted data can be stored safely or transferred to a third party for analysis. Depending on the type of homomorphic encryption, certain processes are possible.

##### `Partial homomorphic encryption`: This method of encryption can perform one type of operation on encrypted data. For example, this type of encryption would allow data to be either added or multiplied, not both. The obvious drawback is that only one type of operation is possible.

##### `Somewhat homomorphic encryption`: This method of encryption can perform more than one type of operation. Data encrypted this way could be added and multiplied, but there is a limit to the number of operations that can be accomplished.

##### `Fully homomorphic encryption`: With this method of encryption, more than one type of secure computation can be performed. Additionally, there is no limit to the number of operations that can be performed.

#### An Example Of Multiparty Encryption
![Example](/image/1.png)
![Example](/image/2.png)
![Example](/image/3.png)
