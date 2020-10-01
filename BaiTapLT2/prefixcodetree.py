from bitstring import BitArray
#must install bitstring module

class PrefixCodeTree:

    def __init__(self):
        self.right = None
        self.left = None
        self.symbol = ""

    def insert(self, codeword, symbol): #insert codeword to tree
        for bit in codeword:
            if bit == 1:
                if self.right is None:
                    self.right = PrefixCodeTree()
                self = self.right
            elif bit == 0:
                if self.left is None:
                    self.left = PrefixCodeTree()
                self = self.left
        self.symbol = symbol

    def decode(self, encodedData, datalen):
        # convert to list of bit 1 0
        bitList = list(BitArray(encodedData).bin)
        node = self
        decodeData = node.symbol

        if len(bitList) >= datalen :
            for bit in range(datalen):
                if bitList[bit] == '1':
                    node = node.right
                elif bitList[bit] == '0':
                    node = node.left
                if node.symbol != "":
                    decodeData += " " + node.symbol
                    node = self
                elif node == None :
                    return "False"
        else:
            for bit in range(len(bitList)):
                if bitList[bit] == '1':
                    node = node.right
                elif bitList[bit] == '0':
                    node = node.left
                if node.symbol != "":
                    decodeData += " " + node.symbol
                    node = self
                elif node == None:
                    return "False"
        return decodeData