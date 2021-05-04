#!/usr/bin/env python3

#Carly Geissler
#Exam4
#BIO439


def countKmersPossible(string, k):
  
  """
    This function counts possible kmers with alphabet length of 4 (A, C, T, G)
    
    Parameters:
    string: string to be used
    k: length of substring
    
    Returns:
    integer: count of possible kmers
    
    """

  #will return count of observed kmers
  #use is a place holder variable to know what to loop to  
  count = 0
  use = 0
  
  #determine which to use to calculate kmers
  length = len(string)-k+1
  power = 4**k
  
  #use minimum of length and power
  if length < power:
    use = length
  else:
    use = power

  #count kmers
  for i in range(use):
    kmer = string[i:i+k]
    count += 1
  
  return count



def countKmersObserved(string, k):
  
  """
    This function counts observed kmers. It also determines the kmers and 
    adds them to a list called strList. The function then adds all unique 
    kmers to a different list called observed.
    
    Parameters:
    string: string to be used
    k: length of substring
    
    Returns:
    integer: count of observed kmers
    
    """

  #empty lists to get possible and obsesrved kmers
  strList = []
  observed = []
  
  #will return count of observed kmers
  count = 0

  #gets kmers and append to list 
  for i in range(len(string)):
    if i + k <= len(string):
      kmer = string[i:i+k]
      strList.append(kmer)
  
  #loop through list and get rid of repeats when adding to obersved list
  for i in range(len(strList)):
    if strList[i] not in observed:
      observed.append(strList[i])
  
  #count of kmers is the length of observed list
  count = len(observed)
  
  return count
  
  
import pandas as pd
  
def createDF(string):
    
  """
    This function creates a dataframe for an individual sequence.
    
    Parameters: 
    string: sequence to be used
    
    Returns:
    integer: totalO is the sum of the observed list
    integer: totalP is the sum of the possible list
    dataframe: df is a dataframe for the string given as an argument
    """
  
  observedList = []
  possibleList = []
  kList = []
  
  #count the observed, count the possible and append to empty lists
  for k in range(1, len(string) + 1):
    observed = countKmersObserved(string, k)
    possible = countKmersPossible(string, k)
    observedList.append(observed)
    possibleList.append(possible)
    kList.append(k)
  
  #calculate the sums of each list    
  totalO = sum(observedList)
  totalP = sum(possibleList)
  
  #create dictionary
  d = {'K': kList, 'Observed kmers': observedList, 'Possible kmers': possibleList}
  #create dataframe
  df = pd.DataFrame(d)
  
  return totalO, totalP, df
  
  
def calcLinguistic(totalO, totalP):
    
  """
    This function calculates linguistic complexity.
    
    Parameters:
    totalO: sum of observed list
    totalP: sum of possible list
    
    Returns:
    integer: linguistic complexity
    """
  
  linguistic = totalO/totalP
  
  return linguistic
  
  
def main():
    
  """
    This is the main function for the program. It reads the file, and for each sequence in the file
    creates a dataframe of kmers and calculates linguistic complexity. The dataframe is written to a csv file.
    
    Parameters:
    none
    
    Returns:
    none
    """
  
  #open and read file
  with open('example_text.csv', 'r') as f:
    text = f.read()
  #split file into list of sequences(strings)
  stringList = text.split()
  
  #i helps to name the output files
  i = 0
  #for each string in the file: open an output file to write to,
  #call createDF to create dataframe
  #call calcLinguistic to calculate linguistic complexity
  #write the dataframe to the output file
  
  #QUESTION: how to include statement about linguistic complexity to command line
  for string in stringList:
    i += 1
    outputName = 'output' + str(i) + '.csv'
    outputFile = open(outputName, 'w')
  
    totalO, totalP, df = createDF(string)
    linguistic = round(calcLinguistic(totalO, totalP), 3)
  
    outputFile.write(str(df))
    print("Linguistic Complexity =", linguistic)
  
