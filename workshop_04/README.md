# Workshop 4

The fourth workshop is on 4 June 2025 at 10 am (CET). If you are registered on Moodle, the link is [here](https://moodlecommunity.napier.ac.uk/course/view.php?id=960).

## 10-11am (CET) Zero Knowledge Proofs and Fully Homomorphic Encryption

The topic covered is Zero Knowledge Proofs and Fully Homomorphic Encryption. The presentation on ZKPs and Fully Homomorphic Encryption is [here](https://youtu.be/J03UE89Qw8E).

Some examples are here:

* ZKP [link](https://asecuritysite.com/zero).
* OpenFHE [link](https://asecuritysite.com/openfhe).
  
## 11-12pm (CET) Guest speakers

* Kazım Rıfat Özyılmaz - Co - Founder of Arf [here](https://www.linkedin.com/in/kazimozyilmaz/) (20 mins). (Bill)
* Ibrahim Kushchu  CEO, TheNextMinds UK [here](https://scholar.google.com/citations?user=ERPjK2AAAAAJ&hl=en) (Gonca).
* Aditya Shetty - Lead of Superteam India [here](https://www.linkedin.com/in/aditya-shetty-97ab5258/) (Aysegul).
 
## 12-1pm (CET) Break.

## 1-2pm (CET) ZKP/FHE Demos and Quiz
This will provide some demos and a quiz.

ZKP examples:

* Fiat-Shamir. This implements the Fiat-Shamir method with the secp256k1 curve [here](https://asecuritysite.com/zero/nizkp).
* Accumulators. This implements an elliptic curve method of implementing an accumulator [here](https://asecuritysite.com/zero/witness).
* zkSnark. This implements a ZKP [here](https://asecuritysite.com/zero/go_qap) and proof with R1CS [here](https://asecuritysite.com/zero/go_r1cs).
* Pedersen Commitment. This implements a simple Pedersen Commitment [here](https://asecuritysite.com/encryption/ped).

Full Homomorphic Encryption:

* BFV/BGV adding two numbers [here](https://asecuritysite.com/openfhe/openfhe_02cpp).
* BFV/BGV batching [here](https://asecuritysite.com/openfhe/openfhe_08cpp).
* CKKS adding/subtracting [here](https://asecuritysite.com/openfhe/openfhe_05cpp).
* CKKS Chebyshev approximations [here](https://asecuritysite.com/openfhe/openfhe_18cpp).
* CKKS Matrix multiplication [here](https://asecuritysite.com/openfhe/openfhe_27cpp).
* DM Boolean circuit [here](https://asecuritysite.com/openfhe/openfhe_09cpp).
  
## 2-3pm (CET) Guest speaker

* Madjid Golparvaran Tehrani. PQC and Quantum Computing.
 
## 3-4pm (CET) World-leaders in Cryptography: Chris Peikert, University of Michigan.
Chris is a Professor in the Computer Science and Engineering department at the University of Michigan. He completed his PhD in 2006 at the MIT Computer Science and AI Laboratory under the mentorship of Silvio Micali.  He received a Test of Time award at Crypto 2008 for a paper entitled "A Framework for Efficient and Composable Oblivious Transfer" and also a TCC Test of Time award for his paper on “Efficient Collision-Resistant Hashing from Worst-Case Assumptions on Cyclic Lattices,” in 2006.  In 2024, Chris was elected a Fellow of the International Association for Cryptologic Research and is recognised as one of the world's leading experts in lattice-based methods.

# Test 
The test is [here](https://moodlecommunity.napier.ac.uk/mod/quiz/view.php?id=53965).

# Key Principles of ZKP and FHE
Zero Knowledge Proofs:

* An accumulator is a fixed-length register which stores data elements using a private key, and then a witness can be created with the private key and provided with the associated public key.
* The Fiat-Shamir method can implement a Non-interactive zero-knowledge proof (NI-ZKP) method.
* A range proof allows for verification if a value is within a given range. Bulletproofs are a popular range proof.
* zkSnarks supports a public and a private input into an equation, and where a proof of correctness can be created.
* A Pedersen Commitment allows for a transaction value to be blinded. It can be used in privacy-aware cryptocurrency.
* With an interactive ZKP, Victor will generate a challenge for Peggy, whereas with a non-interactive ZKP, Peggy will generate her own challenge from a hash of various values.
* With discrete logs, g^x.y^y (mod p) is equal to g^{x+y} (mod p), and where g is a base generator and p is a prime number.
* With discrete logs, {g^x)^y (mod p) is equal to g^{xy} (mod p), and where g is a base generator and p is a prime number.
* With elliptic curve cryptography (ECC), a.G is a point on the curve, and where a is a scalar value, and G is the base point.
* A Ring signature can hide the sign of a message, and who is someone within a trusted range of signers.

Fully Homomorphic Encryption:

* FHE uses lattice methods, and where we map to points in a lattice using Learning With Errors (LWE).
* In the asymmetric key methods, a public key is used to encrypt the data, and a private key is used to decrypt the result.
* In symmetric key methods, the same key encrypts and decrypts.
* A neural network can be made up of vector and matrix operations.
* For SVM, we can train with non-encrypted data, and then export the model to run with homomorphically encrypted data.
* Bootstrapping is used to remove the buildup of noise, especially where there are multiplication operations.
* Chebyshev Approximation can be used to implement a range of mathematical functions in a lattice form.









