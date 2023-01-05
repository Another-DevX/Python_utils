class VotingBooth:
    
    def __init__(self, identifier, valid_regions):
        self._identifier = identifier
        self._valid_regions = valid_regions
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._valid_regions:
            self._region = region
        else:
            raise ValueError(f"The region {region} is'nt valid" )


booth = VotingBooth(123,['Mexico','Morelos'])
print(booth.region)
booth.region = 'Mexico'
print(booth.region)