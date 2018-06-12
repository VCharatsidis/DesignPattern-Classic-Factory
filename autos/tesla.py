# -*- coding: utf-8 -*-

from .abs_auto import AbsAuto

class Tesla(AbsAuto):
    def start(self):
        print('Tesla running')
    
    def stop(self):
        print ('Tesla stopping')