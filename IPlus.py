# "IPlus" means "Input Plus", I also have "FPlus"(File Plus) that'll be uploaded soon.
# Please change your input keyword to let your users know what he/she needs to input.
def input_int(kwd=''):
  i=input(kwd)
  try:
    return int(i)
  except:
    print('please input a int, not "'+i+'".')
    return input_int(kwd)
  
def input_bool(kwd=''):
  i=input(kwd)
  try:
    return bool(i)
  except:
    print('please input a bool(True or False), not "'+i+'".')
    return input_bool(kwd)

def choose(kwd='Choose:',opt=['A','B']):
  i=input(kwd)
  try:
    opt.index(i)
    return i
  except:
    print('"'+i+'" is'+"n't a chooseable option. Please input the options you can choose.")
    return choose(kwd,opt)
    
def input_list(kwd='Input:',len=1,answerTypes=['str']):#Only supported str,int,bool
  l=[]
  print(kwd)
  for i in range(len):
    eval({'str':'input(),}[answerTypes[i]])
    l.append(input())
    return i

def input_dict(kwd='',kwds=[]):
  d={}
  for i in range(len(kwds)-1):
    d[kwds[i]]=input(kwds[i])
  return d
