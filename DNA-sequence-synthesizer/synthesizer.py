
class Synthesiser:
  def getSeqParts(self,seq):
        #assuming last one wil not have linkages

    result = dict()
    for i in range(0,len(seq)-2,4):
     
      if (i==len(seq)-3):
        base_sugar = seq[i:]
      else:
        base_sugar = seq[i:i+3]
        linkage = seq[i+3]
        if linkage in result:
          result[linkage] += 1
        else:
          result[linkage] = 1
        
      if base_sugar in result:
        result[base_sugar] += 1
      else:
        result[base_sugar] = 1

      

    return result


  def getMassSeq(self,seqParts):

      total = 0

      for key in seqParts:
        total += self.askChemistForMass(key) * seqParts[key]
      return total

  def askChemistForMass(self,elem):
    return len(elem)*10 

  


  def getLabel(self,sequence):
    label = ""
    seqsplit = sequence.split("-")[1:]
    prevDna = False
    for i in range(len(seqsplit)):

      if "d" in seqsplit[i].lower() and not prevDna:
        label += "["
        prevDna = True

      elif "d" not in seqsplit[i].lower() and prevDna:
        label += "]"
        prevDna = False

      label +=seqsplit[i][0]

      if "d" in seqsplit[i].lower() and prevDna and i == len(seqsplit)-1:
        label += "]"
      

    return label

  def validateSeq(self,seq):
    #assuming last one wil not have linkages
    modifiers =  set([ "-", "m", "b", "i"])
    bases = set(["A", "G", "C", "T", "U", "I"])
    sugars = set(["d", "r", "m", "f", "a", "i","p"])
    linkages= set(["o","s"])
    result = True

    if seq[-1] in linkages:
      result = False
      print("Incorrect Linkage at location ", len(seq))
    

    for i in range(0,len(seq)-2,4):
    
      if i == len(seq)-3:
        m = seq[i]
        b = seq[i+1]
        s = seq[i+2]
        if m not in modifiers:
          result = False
          print("Incorrect Modifier at location ", i+1)
        if  b not in bases:
          result = False
          print("Incorrect Base at location ", i+2)
        if s not in sugars:
          result = False
          print("Incorrect Sugar at location ", i+3)
     
      else:
        m = seq[i]
        b = seq[i+1]
        s = seq[i+2]
        l = seq[i+3]
        if m not in modifiers:
          result = False
          print("Incorrect Modifier at location ", i+1)
        if  b not in bases:
          result = False
          print("Incorrect Base at location ", i+2)
        if s not in sugars:
          result = False
          print("Incorrect Sugar at location ",i+3)
        if l not in linkages:
          result = False
          print("Incorrect Linkage at location ", i+4)
          
    return result
    
  def testQ1(self):
    parts = self.getSeqParts("-Uro-Uro-Gro-Ums-Um")
    print(parts)
    mass = self.getMassSeq(parts)
    print(mass)

  def testQ2(self):
    
    print(self.getLabel("-Gdo-Gdo-Ado-Ado-Tdo-Gro-Gro-Cro-Uro-Uro-Uro-Ur"))
    print(self.getLabel("-Gmo-Gmo-Amo-Amo-Tmo-Gro-Gro-Cro-Uro-Uro-Uro-Urd"))
  def testQ3(self):
    
    print(self.validateSeq("-Gdo-Gdo-Ado-Ado-Tdo-Gro-Gro-Cro-Uro-Uro-Uro-Ur"))

synthesiser = Synthesiser()

synthesiser.testQ1()

synthesiser.testQ2()

synthesiser.testQ3()