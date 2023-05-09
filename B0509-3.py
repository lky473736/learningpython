class television :
    def __init__ (self, chan, vol, on) :
        self.chan = chan # channel
        self.vol = vol # volume
        self.on = on # on
    
    def show(self) : # 출력
        print(self.chan, self.vol, self.on)
    
    def setchan (self, chan) :
        self.chan = chan
    
    def getchan (self) :
        return self.chan
    
    def setvol (self, vol) :
        self.vol = vol 
        
    def getvol (self, vol) :
        return self.vol
    
# setter와 getter는 항상 pair 관계
        
tv1 = television(11, 5, True)
tv1.show()
tv1.setchan(100)
tv1.show()

print()

tv2 = television(12, 9, False)
tv2.show()
tv2.setvol(30)
tv2.show()