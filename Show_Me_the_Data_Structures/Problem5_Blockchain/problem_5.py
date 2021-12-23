import hashlib
import datetime


class Block:

    def __init__(self, time_stamp, data):
        self.time_stamp = time_stamp
        self.data = data
        self.previous_hash = None
        self.hash = self.calc_hash()
        self.next_block = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = str(self.time_stamp).encode('utf-8') + \
            str(self.data).encode('utf-8') + \
            str(self.previous_hash).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return "Block Data: " + str(self.data) + \
               "\nBlock Hash: " + str(self.hash) + \
               "\nBlock Timestamp: " + str(self.time_stamp) + \
               "\nPrevious Block Hash: " + str(self.previous_hash) + \
               "\n---------------------------------------------"


class BlockChain:
    def __init__(self):

        self.block = Block(datetime.datetime.now(), "Genesis")
        self.head = self.block

    def append(self, data):
        block = Block(datetime.datetime.now(), data)
        block.previous_hash = self.block.hash
        self.block.next_block = block
        self.block = self.block.next_block


# My test
block_chain = BlockChain()

for n in range(10):
    block_chain.append("Block " + str(n+1))

while block_chain.head is not None:
    print(block_chain.head)
    if block_chain.head.next_block:
        assert block_chain.head.next_block.previous_hash == block_chain.head.hash
    block_chain.head = block_chain.head.next_block


