# Workshop 2

The second workshop is on 15 April 2025 at 10 am (CET). If you are registered on Moodle, the link is [here](https://moodlecommunity.napier.ac.uk/course/view.php?id=960).

## 10-11am (CET) Blockchain Fundamentals

The topics covered are:
* Blockchain.
* Cryptocurrency.
* Digital Signing.

The presentation on this is [here](https://www.youtube.com/watch?v=kx5Pp-Jxi2Y) and the PowerPOint is [here](https://github.com/billbuchanan/trust4futures/blob/main/workshop_02/workshop_02_blockchain.pdf).

## 11-12pm (CET) Guest speakers

* Srijan Shetty, Fuze Finance.
* Öznur Mut Sağdıçoğlu, Chief Cryptography Researcher, at TÜBİTAK Bilgem, Blockchain Research Lab.
 
## 12-1pm (CET) Break.

## 1-1:45pm (CET) Demonstration of Blockchain and Quiz
The presentation on Smart Contracts is [here](https://www.youtube.com/watch?v=xeaDE8wgVVQ) and for the creation of NFTs is [here](https://youtu.be/p85yuFkNCbw). A sample lab is [here](https://github.com/billbuchanan/trust4futures/blob/main/workshop_02/lab.md).

## 1:45-3pm (CET) Guest speakers

* Maciej Zurawski, An introduction to decentralised finance (DeFi). 
* Greg Mclardie, Supply Chains. 

## 2:45-3pm Break
 
## 3-4pm (CET) World-leaders in Cryptography
Aggelos Kiayias is a professor at the University of Edinburgh and the chief science officer at Input Output Global (formerly IOHK). He received his PhD in 2002 from City University of New York. He is chair in cyber security and privacy, and director of the Blockchain Technology Laboratory at the University of Edinburgh. In 2021, Aggelos was elected Fellow of the Royal Society of Edinburgh (FRSE), and was recently awarded the BCS Lovelace Medal 2024 for his transformative contributions to the theory and practice of cyber security and cryptography.  H works in areas of blockchain technology and distributed systems, cryptography, e-voting and secure multiparty protocols, as well as privacy-enhanced identity management.

The discussion is [here](https://youtu.be/_zjROu-NYV4).

# Key Principles of Blockchain

## Bitcoin
* Bitcoin was created in 2019 by Satoshi Nakamoto.
* 0.00000001 Bitcoin is one Satoshi.
* A new block is created every 10 minutes or so.
* There are only 21 million Bitcoins that can be minted.
* The first reward for mining was 50 BTCs, and which halves in its reward at certain times.
* Currently, the reward for mining is 3.125 BTC.
* The first block was mined on 3 Jan 2009 and is known as the Genesis Record (Block zero).
* Each block has a hash that the miners race to find a Nonce value, which will give a hash with a given number of preceding zeros, eg 0000000000000000000215512adf2fc46a80ce14022be5584ae4459dc77283cf.
* Each block has a Merkle Root, and which is a Merkle hash of all the transactions in the block, eg 46c7f05e9c0ce7e3b2fe4abbe37b0683803c818f76d77fedc5683d61af6f7753
* A Bitcoin address is created from a random 256-bit seed value. This is used to create a Wif private key using Base-58. This key is stored in a digital wallet.
* For the Bitcoin ID, we create an ECDSA public key and then hash it with SHA-256 and RIPEMD-160 and convert it to an ID with Base-58.
* To sign a transaction, Bob uses his private key to sign a transaction, and which contains Alice's ID. Everyone can verify the transaction on the blockchain using Bob's public key.
* An example of a digital wallet is MetaMask.
* Bitcoin is a permission-less ledger and where anyone can create a wallet.
* The block size is around 2MB

## Ethereum
* Created in 2015 by Vitalik Buterin and others.
* Introduced the usage of smart contracts.
* It was hacked in 2016, and the currency was split into two: Ethereum (ETH) and Ethereum Classic (ETC).
* Miners consume gas for undertaking work.
* One Keccack256 takes 30 gas, and six more gas for every 256 bits of data.
* Each transaction has a gas fee associated with it.
* The programming language used for Ethereum is Solidity, and where we compile the code into byte code and which runs on the blockchain.
* The online compiler for Ethereum is Remix.org.
* Ethereum is a permission-less ledger and where anyone can create a wallet.
* Integrated cryptocurrency: ETH.
* Blocks produced every 10 seconds or so.
* The size of the blocks typically varies up to around 250KB, and there are between 50 and 250 transactions.
* With cryptocurrency, the smart contract creates a finite supply, and no more can be created. The creator of the contract will allocate the owner of all the coins.
* With an NFT (Non-fungible Token), no NFTs are created initially. These are minted as required and require JSON data to be added.

## Hyperledger
* The Hyperledger project is an open-source permissioned blockchain.
* Hyperledger INDY is used for digital identity.
* Hyperledger FABRIC is used to create a DLT (Distributed Ledger Technology).
* Smart contracts are created with either Golang, Java, or Node.js.
* The ledger is not public.
* No integrated cryptocurrency or token.






