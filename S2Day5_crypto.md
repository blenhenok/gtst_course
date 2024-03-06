# Cryptography 
#cryptography 
- Cryptography is technique of securing information and communications through use of codes so that only those person for whom the information is intended can understand it and process it. Thus preventing unauthorized access to information.
- - The term “cryptography” combines “crypt” (meaning “hidden”) and “graphy” (meaning “writing”).
- It has two main Components:
    - **Encryption**: Practice of hiding messages so that they can not be read by anyone other than the intended recipient
    - **Authentication & Integrity**: Ensuring that users of data/resources are the persons they claim to be and that a message has not been altered
- **plain text**  ---> **Encryption** ---> **cipher text** ---> **Decryption** ---> **plain text**
# Encryption 
- Data Encryption is a method of preserving data confidentiality by transforming it into ciphertext, which can only be decoded using a unique decryption key produced at the time of the encryption or prior to it.
- Data encryption converts data into a different form (code) that can only be accessed by people who have a secret key (formally known as a decryption key) or password. 
- Encryption is a critical tool for maintaining data integrity, and its importance cannot be overstated. Almost everything on the internet has been encrypted at some point.
### Cipher
- **cipher** (or **cypher**) is an algorithm used for performing encryption or decryption. It involves a series of well-defined steps that can be followed as a procedure.
- A cipher converts plaintext (the original message) into ciphertext using a key to determine how the transformation is done.
- **Plaintext**: The original information, Data that has not been encrypted.
- **Ciphertext**: The encrypted form of the message.
- **Key**: Auxiliary information that determines the detailed operation of the cipher.
- Types of Ciphers:
    - **Symmetric Key Ciphers**: Use a single common key for both encryption and decryption. Examples: Data Encryption Standard (DES) and Advanced Encryption Standard (AES).
    - **Asymmetric Key Ciphers**: Use a pair of keys: a public key for encryption and a private key for decryption. Popular algorithm: RSA.
# Symmetric algorithm
- Algorithms in which the key for encryption and decryption are the same.
- **How it works**:
    - The sender and receiver share the same secret key.
    - The sender uses this key to encrypt the message.
    - The receiver uses the same key to decrypt the message.
- Types:
    - **Block Ciphers**: Encrypt data one block at a time (typically 64 bits, or 128 bits) Used for a single message.
    - **Stream Ciphers**: Encrypt data one bit or one byte at a time. Used if data is a constant stream of information. 
### Substitution ciphers
#### Caesar cipher
- It involves shifting each letter in the plaintext by a fixed number (mostly shift of **3** ,commonly known as the Caesar shift ) of positions down the alphabet. 
- encryption
    plain text "attack on dawn"  --->  Caesar cider  --->  cipher text "dwwdfn dw gdyq"
- Decryption                                             -key 3-
    cipher text "dwwdfn dw gdyq"  --->  Caesar cider  --->  plain text "attack on dawn"
#### Using a key to shift alphabet
- Obtain a key to for the algorithm and then shift the alphabets
- For instance if the key is word we will shift all the letters by four and remove the letters w, o, r, & d from the encryption
- We have to ensure that the mapping is one-to-one 
    - no single letter in plain text can map to two different letters in cipher text
    - no single letter in cipher text can map to two different letters in plain text
- Replacing the letters by 1 shift we can get different rotations. To do this we can use this website *rot13.com* . this encoding is called rot encoding
# Asymmetric Encryption 
- - asymmetric encryption uses two distinct keys:
    - **Public key**: Used for encryption.
    - **Private key**: Used for decryption.
- **How it works**:
    - The sender encrypts the message using the recipient’s public key.
    - The recipient decrypts the message using their private key.
- Secret transmission of key for decryption is not required
- Public key can be exposed so, if i need to send you a message i just ask you for your public key and i will encrypt the message with your public key. When you get the ciphertext you can decrypt it with your private key.
- Every entity can generate a key pair(private & public) and release its public key
### Types of asymmetric encryption 
- Two most popular algorithms are RSA & El Gamal
-  **RSA**
    - Developed by Ron Rivest, Adi Shamir, Len Adelman
    - Both public and private key are interchangeable
    - Variable Key Size (512, 1024, or 2048 bits)
    - It have a math formulas for generating the keys.
- **El Gamal**
    - Developed by Taher ElGamal
    - Variable key size (512 or 1024 bits)
## Terms of Cryptography
- **Encoding/ decoding**
    - Encoding is used to change data into a different format, ensuring its integrity and usability.
    - This can be done by doing math on the given input/substitution
    - Example: Base64 encoding is commonly used for data transfer between systems or applications.
- **Encrypting/Decrypting**
    - This is method of creating Cipher text with keys.
    - To decrypts this kind u need to have the private key.
    -  Encryption secures data by converting it into an unreadable format.
    - Encryption is reversible using a specific key.
    - Example: DES,AES,RSA 
- **Hashing**
    - This is a method of creating Cipher text with respect to a created hash
    - Hashing transforms data into a fixed-length alphanumeric string (hash or message digest).
    - Hashing is a one-way process; the original data cannot be derived from the hash.
    - To reverse the hash, you just search for some match, you don't decrypt/decode it.
    - Salt: is a random string used for data modification for password protection.
    - Example: MD5,sha254,... 
- **Encoding** preserves usability.
- **Hashing** ensures data integrity.
- **Encryption** protects data confidentiality.
## Kinds of encodings/encryptions
- **Base64 Encoding**: Converts binary data into a text format using a set of 64 characters (A-Z, a-z, 0-9, and + / -).
- **URL Encoding**: Replaces special characters in URLs with percent-encoded representations (e.g., space becomes `%20`).
- **HTML Entities**: Represents special characters in HTML (e.g., `&lt;` for `<`).
- **UTF-8 Encoding**: Represents Unicode characters using variable-length byte sequences.
# Tools
- There are lots of encodings/encryption, To identify this we will need some tools/sites
### hashid
- hashID is a versatile tool used for identifying different types of hashes used to encrypt data and passwords.
- To install hashID, use the following command:`sudo apt install hashid`
- Identify the hash type for a given input: `hashid <input>`
### Cyberchef
-  Link : https://gchq.github.io/CyberChef/ 
- Search for **magic**, drag and drop it, to the recipe.
- Add your text to the input. Look at the output it is the guess of what the hash can be

# Python for cryptography
- We can use programming to do tools that can do our own encryption and encoding hash type. There are so many methods, even you can do the encoding/decoding for the base64.

## Obfuscation
- 