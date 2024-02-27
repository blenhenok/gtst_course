# Cryptography 
#cryptography 
- Cryptography is technique of securing information and communications through use of codes so that only those person for whom the information is intended can understand it and process it. Thus preventing unauthorized access to information.
- - The term “cryptography” combines “crypt” (meaning “hidden”) and “graphy” (meaning “writing”).
- It has two main Components:
    - **Encryption**: Practice of hiding messages so that they can not be read by anyone other than the intended recipient
    - **Authentication & Integrity**: Ensuring that users of data/resources are the persons they claim to be and that a message has not been altered
# Encryption 
- Data Encryption is a method of preserving data confidentiality by transforming it into ciphertext, which can only be decoded using a unique decryption key produced at the time of the encryption or prior to it.
- Data encryption converts data into a different form (code) that can only be accessed by people who have a secret key (formally known as a decryption key) or password. 
- Encryption is a critical tool for maintaining data integrity, and its importance cannot be overstated. Almost everything on the internet has been encrypted at some point.
- **cipher** (or **cypher**) is an algorithm used for performing encryption or decryption. It involves a series of well-defined steps that can be followed as a procedure.
- A cipher converts plaintext (the original message) into ciphertext using a key to determine how the transformation is done.
- **Plaintext**: The original information, Data that has not been encrypted.
- **Ciphertext**: The encrypted form of the message.
- **Key**: Auxiliary information that determines the detailed operation of the cipher.
- Types of Ciphers:
    - **Symmetric Key Ciphers**: Use a single common key for both encryption and decryption. Examples: Data Encryption Standard (DES) and Advanced Encryption Standard (AES).
    - **Asymmetric Key Ciphers**: Use a pair of keys: a public key for encryption and a private key for decryption. Popular algorithm: RSA.
### Symmetric algorithm
- Algorithms in which the key for encryption and decryption are the same.
- Types:
    - **Block Ciphers**: Encrypt data one block at a time (typically 64 bits, or 128 bits) Used for a single message.
    - **Stream Ciphers**: Encrypt data one bit or one byte at a time. Used if data is a constant stream of information. 
## Substitution ciphers
1. **Caesar cipher**:  It involves shifting each letter in the plaintext by a fixed number (mostly shift of **3** ,commonly known as the Caesar shift ) of positions down the alphabet. 



