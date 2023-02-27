from TV import TV
class Control:
    def __init__(self, tv):
        self._tv = tv
    
    def turnOn(self):
        TV.turnOn()
    def turnOff(self):
        TV.turnOff()
    def canalUp(self):
        TV.canalUp()
    def canalDown(self):
        TV.canalDown()
    def volumenUp(self):
        TV.volumenUp()
    def volumenDown(self):
        TV.volumenDown()
    def setCanal(self):
        TV.setCanal()

    def enlazar(self, tv):
        self._tv = tv
        TV.setControl(self)
    
    def getTv(self):
        return self._tv
    def setTv(self, tv):
        self._tv = tv