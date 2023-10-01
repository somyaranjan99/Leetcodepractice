class Codec:
    def __init__(self):
        self.shortUrld={}
        self.longUrld={}
        self.randStr='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.longUrld:
            surl= "".join([random.choice(self.randStr) for _ in range(9)])
            if surl not in self.shortUrld:
                self.shortUrld[surl]=longUrl
                self.longUrld[longUrl]=surl
            return self.longUrld[longUrl]

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.shortUrld[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))