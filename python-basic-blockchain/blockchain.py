import datetime as d # import the datetime library for our block timestamp and rename it as d for simplicity while typing 
import hashlib as h # import the library for hashing our block data and rename it as h for simplicity while typing 


class Block: # create a Block class
    chain = []

    def __init__(self,index, timestamp, data , prevhash): # declare an initial method that defines a block, a block contains the following information
        self.index = index # a block contains an ID
        self.timestamp =timestamp # a block contains a timestamp
        self.data = data # a block contains some transactions
        self.prevhash = prevhash # a block contains a hash of the previous block
        self.hash = self.hashblock() # a block contains a hash, the hash is obtained by hashing all the data contained in the block

    def hashblock (self): # define a method for data encryption, this method will retain a hash of the block
        block_encryption=h.sha256() # We need a sha256 function to hash the content of the block, so let's declare it here
        block_encryption.update((str(self.index)+str(self.timestamp)+str(self.data)+str(self.prevhash)).encode('utf-8')) # to encrypt the data in the block, We need just to sum everything and apply the hash function on it
        return block_encryption.hexdigest() # let's return that hash result 
    
    def printDetails(self):
        print("Block ID :{} ".format(self.index)) 
        print("Timestamp:{}".format(self.timestamp))
        print("Hash of the block:{}".format(self.hash))
        print("Previous Block Hash:{}".format(self.prevhash))
        print("data:{}\n".format(self.data))

    @staticmethod # declaring a static method for the genesis block
    def genesisblock(): # declare a function for generating the first block named genesis
        return Block(0,d.datetime.now(),"genesis block transaction"," ") # return the genesis block
    
    @staticmethod# let's declare another static method to get the next block
    def newblock(lastblock): # get the next block, the block that comes after the previous block (prevblock+1)
        index = lastblock.index+1 # the id of this block will be equals to the previous block + 1, which is logic
        timestamp = d.datetime.now() # The timestamp of the next block
        hashblock = lastblock.hash # the hash of this block
        data = "Transaction " +str(index) # The data or transactions containing in that block
        return Block(index,timestamp,data,hashblock)# return the entire block

Block.chain = [Block.genesisblock()] # now it's time to initialize our blockchain with a genesis block in it
prevblock = Block.chain[0] # the previous block is the genesis block itself since there is no block that comes before it at the indice 0 

# let's print the genesis block information
prevblock.printDetails()


for i in range (0,5): # the loop starts from here, we will need only 5 blocks in our ledger for now, this number can be increased
    addblock = Block.newblock(prevblock) #  the block to be added to our chain 
    Block.chain.append(addblock) # we add that block to our chain of blocks
    prevblock = addblock #now the previous block becomes the last block so we can add another one if needed
    prevblock.printDetails()
    
