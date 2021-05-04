#Test script for exam4.py

from exam4 import *

def test_countKmersPossible():
  
  string = "ATTTGGATT"
  k = 2  
  
  actual_result = countKmersPossible(string, k)
  expected_result = 8
  
  assert actual_result == expected_result
  
  
  
def test_countKmersObserved():
  
  string = "ATTTGGATT"
  k = 2  

  actual_result = countKmersObserved(string, k)
  expected_result = 5

  assert actual_result == expected_result
  


def test_createDF():
  
  string = "ATTTGGATT"

  totalO, totalP, df = createDF(string) 
  expected_totalO = 35
  expected_totalP = 40

  assert totalO == expected_totalO
  assert totalP == expected_totalP
  


def test_calcLinguistic():
  totalO = 35
  totalP = 40
    
  actual_result = calcLinguistic(totalO, totalP)
  expected_result = 0.875
    
  assert actual_result == expected_result
  
