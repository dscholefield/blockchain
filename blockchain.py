
from operator import truediv
import hashlib 

class BlockNotValid(Exception):
    def __init__(self, message):
        self.message = message

class Peer:
    def __init__(self, name: str):
        self.name = name
        self.last_block = None
        self.block_list = None

    def add_block(self, block: Block):
        pass




class BlockChainConfig:
    """
    A class to represent a specific blockchain implementation config
    (not a blockchain itself)
    
    ...
    
    Attributes
    ----------
    difficulty : int
        the current minding difficulty expressed as minimum leading zeros required for hash
    vote_threshold : int
        the number of peers required to vote for a nonce before block added to all peer chains
    peers : list(Peer)
        the list of peers currently registered with blockchain

    Methods
    -------
    add_peer(peer : Peer): None
        adds a peer to the list of peers (if not already present)

    del_peer(peer ; Peer): None
        removes a peer from the list of peers (if present)

    list_peers(): list(str)
        returns a list of names (peer.name) from all peers in blockchain
    """

    def __init__(self, difficulty: int, vote_threshold: int):
        self.difficulty = difficulty
        self.vote_threshold = vote_threshold
        self.peers = []
    
    def add_peer(self, peer: Peer) -> None:
        if (peer not in self.peers):
            self.peers.append(peer)

    def del_peer(self, peer: Peer) -> None:
        if (peer in self.peers):
            self.peers.remove(peer)

    def list_peers(self) -> list[str]:
        name_list = []
        for peer in self.peers:
            name_list.append(peer.name)
        return name_list



class Block:
    """
    This is the main class to define an individual block in a blockchain

    ...

    Attributes
    ----------

    config : BlockChainConfig
        the current config for this blockchain
    block_number : int
        the unique number (in a chain) for this block, starting at 0 for first block
    previous_hash : str
        the hash of the previous block (or 'None' for block number 0)
    _nonce : int
        the mined integer to create the hash with the relevant difficulty (from BlockChainConfig.difficulty)
    this_hash : str
        the hash for this block once mined
    content : str
        any string content desired (or None if not yet added)
    _is_mined : bool
        indicates whether the this_hash has a valid hash for the content

    Methods
    -------
    check -> bool
        checks that the block is mined and valid by hashing the relevant fields and
        comparing the resulting hash with the difficulty requirement

    has_zeros(hash: str, count: int) -> bool
        confirms that the given hash has at least 'count' number of trailing zeros
        which is used to confirm that the difficulty level is met

    """

    def __init__(self, config: BlockChainConfig, block_number: int, previous_hash: str) -> None:
        self.config = config
        self.block_number = block_number
        self.previous_hash = previous_hash
        self.nonce = None
        self.this_hash = None
        self.content = None
        self._is_mined = False

    # confirm whether last few characters are zeros or not
    @staticmethod
    def has_zeros(hash: str, count: int) -> bool:
        # expecting a sha256 hash which is 32 chars
        last_char = -1
        matched = True
        first_char = last_char - count 
        for pos in range(-1,first_char,-1):
                if hash[pos] != "0":
                        matched = False
        return matched

    # create a hash of this block
    def block_hash(self) -> str:
        content_to_hash = str(self.block_number) \
                            + ':' + self.previous_hash \
                            + ':' + str(self.nonce) \
                            + ':' + self.content
        hash = hashlib.sha256(content_to_hash.encode())

    # check that the claimed hash in the block is the actual hash
    # of the content and other required fields and that it has
    # the correct minimum level of difficulty
    def check(self) -> bool:
        hash = hashlib.sha256(self.block_hash())
        return (hash == self.this_hash) and (has_zeros(hash, self.config.difficulty))


    @property
    def is_mined(self):
        return self._is_mined

    @is_mined.setter
    def is_mined(self, flag):
        # if the block becomes 'unmined' then the nonce is cleared
        # and the hash for this block is cleared
        if not flag:
            self.nonce = None
            self.this_hash = None
            self._is_mined = False
        else:
            # we're setting this block to 'is mined' so we need
            # to check it
            if self.check():
                self._is_mined = True
            else:
                BlockNotValid("block hash is not correct - not mined")





peer1 = Peer("peer 1")
print("First peer is %s" % (peer1.name))

