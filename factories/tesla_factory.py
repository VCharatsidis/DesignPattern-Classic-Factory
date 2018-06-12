# -*- coding: utf-8 -*-


from .abs_factory import AbsFactory
from autos.tesla import Tesla

class TeslaFactory(AbsFactory):
    
    def create_auto(self):
        self.chevy = chevy = Tesla()
        chevy.name = 'Chevy Volt'
        return chevy