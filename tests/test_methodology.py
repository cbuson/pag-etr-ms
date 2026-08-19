from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from pag_etr_logic import evaluate, N0, N1, N2, N3

def run():
    tests=[]
    tests.append(('T01', evaluate('M1',{'MAG_CARBONATITO':True})==N1))
    tests.append(('T04', evaluate('M2',{'MAG_ALCALINO':True})==N1))
    tests.append(('T06', evaluate('M3',{'HIDROTERMALISMO':True})==N1))
    tests.append(('T07', evaluate('M4',{'SED_FOSFORITA':True,'APATITA_FOSFATICA':True,'ORIGEM_SEDIMENTAR':True})==N2))
    tests.append(('T09', evaluate('M5',{})==N0))
    tests.append(('T11', evaluate('M6',{'TRAP_SEDIMENTAR':True})==N1))
    tests.append(('T13', evaluate('M7',{'PROTOLITO_POTENCIAL':True})==N0))
    tests.append(('T16', evaluate('M8',{'PERFIL_RESIDUAL':True})==N1))
    tests.append(('T18', evaluate('M9',{'GRANITO_INDIVIDUALIZADO':True})==N1))
    tests.append(('T21', evaluate('M10',{'PEGMATITO':True})==N1))
    tests.append(('T23', evaluate('M11',{'DISCORDANCIA':True})==N0))
    tests.append(('T25', evaluate('M2',{},coverage=False)==N0))
    # casos documentais do Protótipo Científico Cero
    tests.append(('P0_M2', evaluate('M2',{'MAG_ALCALINO':True})==N1))
    tests.append(('P0_M4', evaluate('M4',{'SED_FOSFORITA':True,'APATITA_FOSFATICA':True,'ORIGEM_SEDIMENTAR':True})==N2))
    tests.append(('P0_M9', evaluate('M9',{'GRANITO_INDIVIDUALIZADO':True,'ESPECIALIZACAO_GRANITICA':True,'ETR_LOCAL_COMPATIVEL_M9':True})==N3))
    bad=[x for x in tests if not x[1]]
    for tid,ok in tests: print(tid, 'PASS' if ok else 'FAIL')
    if bad: raise SystemExit(1)
    print(f'{len(tests)} testes executáveis PASS')
if __name__=='__main__': run()
