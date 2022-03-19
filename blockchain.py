
class Peer:
    def __init__(self, name: str):
        self.name = name


class BlockChain:
    """
    A class to represent a specific blockchain impmentation
    
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


peer1 = Peer("peer 1")
print("First peer is %s" % (peer1.name))

