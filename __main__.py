# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:31:54 2018

@author: vcharatsidis
"""

from factories import loader

for factory_name in 'chevy_factory', 'tesla_factory', 'mercedes':
    
    factory = loader.load_factory(factory_name)
    car = factory.create_auto()
    
    car.start()
    car.stop()