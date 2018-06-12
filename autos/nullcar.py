# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:23:11 2018

@author: vcharatsidis
"""

from .abs_auto import AbsAuto

class NullCar(AbsAuto):
    
    def start(self):
        print('Unknown car "%s".')
        
    def stop(self):
        print('Unknown car "%s".')