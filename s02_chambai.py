def chambai(testcase, bailam_f):
  assert 'output' in testcase, 'MUST HAVE :output in testcase to score :bailam ^^'
  o_TESTCASE = testcase.get('output')

  assert callable(bailam_f), 'MUST HAVE bailam_f() method to score :bailam ^^'
  
  try:
    o_BAILAM = bailam_f(**testcase['input'])  # aka input_DAPAN
  except:
    o_BAILAM = None

  score01 = int(o_BAILAM == o_TESTCASE)
  return score01, o_BAILAM
