"""Motor lógico PAG ETR transcrito da metodologia congelada de 13/08/2026.
Não substitui o piloto espacial reproduzido em reproduce_pag_etr.py.
Serve para tornar executáveis e testáveis as regras documentadas M1-M11.
"""
from enum import Enum

class EvidenceState(str, Enum):
    T='T'; F0='F0'; U='U'; X='X'; NA='NA'

N0='N0'; N1='N1'; N2='N2'; N3='N3'; N4='N4'

def present(v): return v is True or v == EvidenceState.T or v == 'T' or v == 'PRESENTE'

def decide(g1, g3=False, g4=False, coverage=True, contradiction=False):
    if not coverage or g1 in (EvidenceState.U, 'U', 'SEM_DADO', None): return N0
    if present(contradiction): return N4
    if present(g3) and present(g4): return N3
    if present(g3): return N2
    if present(g1): return N1
    return N0

def model_gates(model, e):
    p=lambda k: present(e.get(k, False))
    if model=='M1': g1=p('MAG_CARBONATITO'); g3=g1 and p('PROCESSO_CARBONATITICO_COMPATIVEL'); g4=g3 and p('ETR_LOCAL_COMPATIVEL_M1')
    elif model=='M2': g1=p('MAG_ALCALINO'); g3=g1 and p('ESPECIALIZACAO_ALCALINA'); g4=g3 and p('ETR_LOCAL_COMPATIVEL_M2')
    elif model=='M3': g1=p('HIDROTERMALISMO'); g3=g1 and p('FONTE_FERTIL') and p('PATHWAY_OU_TRAP'); g4=g3 and p('ETR_HIDROTERMAL')
    elif model=='M4': g1=p('SED_FOSFORITA'); g3=g1 and p('APATITA_FOSFATICA') and p('ORIGEM_SEDIMENTAR'); g4=g3 and p('REE_REY_FOSFATO')
    elif model=='M5': g1=p('IOA_CONFIRMADO') or p('IOCG_CONFIRMADO'); g3=(p('IOA_CONFIRMADO') and p('APATITA_RELACIONADA')) or (p('IOCG_CONFIRMADO') and p('EVIDENCIA_ETR_RELEVANTE')); g4=g3 and p('ETR_LOCAL_COMPATIVEL_M5')
    elif model=='M6': g1=p('TRAP_SEDIMENTAR'); g3=g1 and p('MINERAIS_PESADOS') and p('FONTE_POTENCIAL'); g4=g3 and p('MONAZITA_OU_XENOTIMA_DETRITICA')
    elif model=='M7': g1=p('PROTOLITO_POTENCIAL') and p('REGOLITO_PRESERVADO'); g3=g1 and p('MOBILIDADE_REE'); g4=g3 and p('FRACAO_TROCAVEL_REE')
    elif model=='M8': g1=p('PROTOLITO_FERTIL') or p('PERFIL_RESIDUAL'); g3=p('PROTOLITO_FERTIL') and p('PERFIL_RESIDUAL_IN_SITU'); g4=g3 and p('ENRIQUECIMENTO_RESIDUAL_REE')
    elif model=='M9': g1=p('GRANITO_INDIVIDUALIZADO'); g3=g1 and p('ESPECIALIZACAO_GRANITICA'); g4=g3 and p('ETR_LOCAL_COMPATIVEL_M9')
    elif model=='M10': g1=p('PEGMATITO'); g3=g1 and p('ESPECIALIZACAO_PEGMATITICA_ETR'); g4=g3 and p('MINERAL_ETR_PEGMATITO')
    elif model=='M11': g1=p('DISCORDANCIA') and p('ARQUITETURA_ESTRUTURAL'); g3=g1 and p('HIDROTERMALISMO_RELACIONADO') and p('SINAL_HREE'); g4=g3 and p('XENOTIMA_HIDROTERMAL')
    else: raise ValueError(model)
    return g1,g3,g4

def evaluate(model,e,coverage=True,contradiction=False):
    g1,g3,g4=model_gates(model,e)
    return decide(g1,g3,g4,coverage,contradiction)

def display(states):
    if N3 in states: return N3
    if N2 in states: return N2
    if N1 in states: return N1
    return N0
