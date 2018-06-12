# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:20:51 2018

@author: vcharatsidis
"""

from .abs_auto import AbsAuto

class ChevyVolt(AbsAuto):
    def start(self):
        print('Chevrolet running')
    
    def stop(self):
        print ('Chevrolet stopping')