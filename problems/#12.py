class Solution:
    def __init__(self):
        self.data={'1000':'M','900':'CM','500':'D','400':'CD','100':'C','90':'XC',
                   '800':'DCCC','700':'DCC','600':'DC','300':'CCC','200':'CC'
                   ,'80':'LXXX','70':'LXX','60':'LX','30':'XXX','20':'XX'
                   ,'50':'L','40':'XL','10':'X','9':'IX','5':'V','4':'IV','1':'I'
                  ,'8':'VIII','7':'VII','6':'VI','3':'III','2':'II','2000':'MM',
                  '3000':'MMM'}
        self.num_list=list()
        self.result=str()
    def intToRoman(self, num: int) -> str:
        self.create_num_list(num)
        for i in range(len(self.num_list)):
            if self.num_list[i]==0:
                continue
            else:
                self.result=self.data[str(self.num_list[i]*10**i)]+self.result
        return self.result
    def create_num_list(self,num):
        while num!=0:
            self.num_list.append(num%10)
            num=int(num/10)
