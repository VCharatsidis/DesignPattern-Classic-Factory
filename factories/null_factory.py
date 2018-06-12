# -*- coding: utf-8 -*-
from .abs_factory import AbsFactory
from autos.nullcar import NullCar

class NullFactory(AbsFactory):
    
    def create_auto(self):
        self.nullcar = nullcar = NullCar()
        nullcar.name = 'Null car'
        return nullcar