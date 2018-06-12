# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:47:03 2018

@author: vcharatsidis
"""

import abc

class AbsAuto(metaclass = abc.ABCMeta):
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @abc.abstractmethod
    def start(self):
        pass
    
    @abc.abstractmethod
    def stop(self):
        pass