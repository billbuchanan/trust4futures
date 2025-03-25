# Workshop 1

The first workshop is 26 March 2025 at 10 am (CET). If you are registered on Moodle, the link is [here](https://moodlecommunity.napier.ac.uk/course/view.php?id=960), and you can take a test [here](https://moodlecommunity.napier.ac.uk/mod/quiz/view.php?id=52669).

## 10-12pm (CET): Cryptography Fundamentals
Presentator: Prof Bill Buchanan OBE
* Intro/Cryptography Fundamentals. Presentation: [here](https://github.com/billbuchanan/trust4futures/blob/main/workshop_01/workshop_01_cryptography.pdf). Video recording [here](https://www.youtube.com/watch?v=dQqzrf0dh0k).

## 12-1pm (CET): Break

## 1-1:30pm (CET): Panel "Trust4Futures - Why is it for You?"
* Moderator: Ayşegül Şensoy
* Panelists: Çağla Gül Şenkardeş, Leyla Arsan, Bill Buchanan
* Co-host: Hisham Ali
  
## 1:30-2pm (CET): Voices4Futures #1
* Moderator: Dr Burcu Sakiz
* Guest speaker: Çağla Gül Şenkardeş (Turkish Technology - Information Security Governance and Compliance
* Co-host: Dr Hisham Ali

## 2-3pm (CET): Practical and Mentimeter Interactive Test
* Moderator: Prof Bill Buchanan OBE
* Mentimeter test and practical hands-on.

## 3-4pm (CET): Guest speaker: Whitfield Diffie
* Chair: Prof Bill Buchanan OBE
* Whitfield Diffie guest talk.

# Key Principles of Cryptography

## Cyber actors
* Bob and Alice are typically used to describe the passing of data between two entities.
* Eve is the passive adversary.
* Mallory is the active adversary.
* Trent is trusted by both Bob and Alice.
* Peggy proves something and Victor verifies it.

## Famous inventors
* Whitfield Diffie and Marty Hellman created the Diffie-Hellman method in 1976.
* Ron Rivest, Adi Shamir and Len Adleman created the RSA method in 1977.
* Ralph Merkle created the Merkle Tree method, and which is used in blockchain applications.
* Neal Koblitz co-created Elliptic Curve Cryptography.

## Symmetric Key Encryption
* With symmetric key encryption, we use the same key to encrypt and decrypt.

## Hashing Methods
* With MD5, we have a 128-bit hash, with SHA-1, we have a 160-bit hash, and SHA-256 has a 256-bit hash.

## Key Derivation Functions (KDF)
* KDFs are used to generate encryption keys or hashed passwords.
* For hashed passwords, we can use the relatively slow methods of PBKDF2, bcrypt, scryt or Argon 2.
* We can slow down a hashing method by putting it through a number of rounds.
* Argon 2 aims to slow down password cracking within GPUs.

## Asymmetric (Public) Key Methods
* With asymmetric key, we have two keys: public key (pk) and a private key (sk).
* To encrypt data, we encrypt with the public key, and decrypt with the private key.
* To sign data, we sign a hash of the message with our private key and verify with the public key.
