"""
  PLEASE NOTICE THIS BEFORE YOU USE IT!
  THIS FILE WRITTEN BY DAVIS ARRIZQI
  IF YOU WANT TO USE THIS, JUST DELETE ALL OF
  THE COMMENTS ON THIS FILE
  SALAM ALAYK!
"""

# validate function
def validate(myCode):
    # check 'def' rules
    if('def' not in myCode): return 'missing def'
        
    # check ':' rules
    if(':' not in myCode): return 'missing :'
        
    # check '(' and ')' rules
    if('(' not in myCode and ')' not in myCode): return 'missing paren'
        
    # () checking - no parameter function
    for element in range(len(myCode)):
        if(myCode[element] == ')' and myCode[element-1] == '('):
            return 'missing param'
    
    # indentation check
    if ('   ' not in myCode): return 'missing indent'
        
    # 'validate' return variable check
    if ('validate' not in myCode): return 'wrong name'
        
    # check 'return' rules
    if ('return' not in myCode): return 'missing return'
        
    # send True if there is no problem at all
    return True
  
  
  """
  HARAP UNTUK MEMBACA INI SEBELUM MENGGUNAKAN!
  FILE INI DITULIS OLEH DAVIS ARRIZQI
  JIKA ANDA INGIN MENGGUNAKAN FILE INI, HAPUS
  SEMUA COMMENT YANG ADA PADA FILE INI
  SALAM ALAYK!
"""
