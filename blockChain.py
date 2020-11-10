import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        #creates the genesis block.
        self.new_block(previous_hash=1,proof = 100)

    def new_block(self,proof,previous_hash=None):
        """
            create a new Block in the Blockchain
            :param proof:<int> the proof given by the Proof of Work algorithm
            :param previous_hash:(Optional) <str> Hash of previous Block
            :return <dict> New Block
        """
        block ={
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions':self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #reset the current list of transactions
        self.current_transactions =[]
        self.chain.append(block)
        return block

    def new_transaction(self,sender,recipient,amount):
        """
        this will create a new transaction that will go into the next mined Block
        and it will return the index of the Block that will hold this transaction

        """
        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1];
