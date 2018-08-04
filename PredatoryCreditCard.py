# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 22:23:49 2018

@author: SIDHARTH
"""

class PredatoryCreditCard(CreditCard):
    """Compounding Interest in CreditCard"""
    
    def __init__(self,customer,bank,acnt,limit,apr):
        super().__init__(customer,bank,acnt,limit)
        self._apr = apr
        
    def charge(self,price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success
        
    def process_month(self):
        if self._balance >0:
            monthly_factor=pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
            