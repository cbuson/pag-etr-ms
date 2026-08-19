# PAG ETR · especificação computacional congelada

Esta especificação transcreve a metodologia documentada no corte de 13 de agosto de 2026. Não introduz pesos, probabilidades ou critérios novos.

## Domínio lógico

`e_i ∈ {T, F0, U, X, NA}`

T condição demonstrada
F0 ausência verificada
U desconhecido ou insuficiente
X conflito
NA não aplicável

## Estados

N0 não avaliável
N1 modelo aberto
N2 justifica prospecção geoquímica
N3 evidência local compatível
N4 contradito localmente

## Função de decisão

N0 quando cobertura é insuficiente ou G1 é desconhecido
N4 quando existe contradição verificada de requisito necessário
N1 quando G1 é verdadeiro e G3 não é verdadeiro
N2 quando G3 é verdadeiro e G4 não é verdadeiro
N3 quando G3 e G4 são verdadeiros

## Regras M1 a M11

M1_N1 = MAG_CARBONATITO
M1_N2 = M1_N1 AND PROCESSO_CARBONATITICO_COMPATIVEL
M1_N3 = M1_N2 AND ETR_LOCAL_COMPATIVEL_M1

M2_N1 = MAG_ALCALINO
M2_N2 = M2_N1 AND ESPECIALIZACAO_ALCALINA
M2_N3 = M2_N2 AND ETR_LOCAL_COMPATIVEL_M2

M3_N1 = HIDROTERMALISMO
M3_N2 = M3_N1 AND FONTE_FERTIL AND PATHWAY_OU_TRAP
M3_N3 = M3_N2 AND ETR_HIDROTERMAL

M4_N1 = SED_FOSFORITA
M4_N2 = M4_N1 AND APATITA_FOSFATICA AND ORIGEM_SEDIMENTAR
M4_N3 = M4_N2 AND REE_REY_FOSFATO

M5_N1 = IOA_CONFIRMADO OR IOCG_CONFIRMADO
M5_N2 = (IOA_CONFIRMADO AND APATITA_RELACIONADA) OR (IOCG_CONFIRMADO AND EVIDENCIA_ETR_RELEVANTE)
M5_N3 = M5_N2 AND ETR_LOCAL_COMPATIVEL_M5

M6_N1 = TRAP_SEDIMENTAR
M6_N2 = M6_N1 AND MINERAIS_PESADOS AND FONTE_POTENCIAL
M6_N3 = M6_N2 AND MONAZITA_OU_XENOTIMA_DETRITICA

M7_N1 = PROTOLITO_POTENCIAL AND REGOLITO_PRESERVADO
M7_N2 = M7_N1 AND MOBILIDADE_REE
M7_N3 = M7_N2 AND FRACAO_TROCAVEL_REE

M8_N1 = PROTOLITO_FERTIL OR PERFIL_RESIDUAL
M8_N2 = PROTOLITO_FERTIL AND PERFIL_RESIDUAL_IN_SITU
M8_N3 = M8_N2 AND ENRIQUECIMENTO_RESIDUAL_REE

M9_N1 = GRANITO_INDIVIDUALIZADO
M9_N2 = M9_N1 AND ESPECIALIZACAO_GRANITICA
M9_N3 = M9_N2 AND ETR_LOCAL_COMPATIVEL_M9

M10_N1 = PEGMATITO
M10_N2 = M10_N1 AND ESPECIALIZACAO_PEGMATITICA_ETR
M10_N3 = M10_N2 AND MINERAL_ETR_PEGMATITO

M11_N1 = DISCORDANCIA AND ARQUITETURA_ESTRUTURAL
M11_N2 = M11_N1 AND HIDROTERMALISMO_RELACIONADO AND SINAL_HREE
M11_N3 = M11_N2 AND XENOTIMA_HIDROTERMAL

## Invariantes

SEM_DADO != AUSENTE_VERIFICADO
ABAIXO_LD != ZERO
NAO_DESCRITO != AUSENTE
FORA_DA_COBERTURA != AUSENTE
ESCALA_INSUFICIENTE != AUSENTE

C + C + C + C != F
A + A + A != F

## Síntese visual

DISPLAY = N3 se qualquer modelo atingir N3
DISPLAY = N2 se nenhum N3 e algum modelo atingir N2
DISPLAY = N1 se nenhum N2 ou N3 e algum modelo atingir N1
DISPLAY = N0 caso contrário
N4 permanece específico do modelo

## Fórmulas espaciais

I(f,h) = area(f interseção h)
P_hex(f,h) = 100 * area(f interseção h) / area(h interseção MS)
P_feature(f,h) = 100 * area(f interseção h) / area(f)
L(l,h) = comprimento(l interseção h)
R(p,h) = 1 se p está em h ou toca seu limite, caso contrário 0
Ru(p,h) = 1 se U(p) interseção h não é vazia
R(c,h) = 1 se area(catchment interseção h) > 0
V(h) = N_pixels_validos(h) / N_pixels_totais(h)
COV(d,h) = area(h interseção cobertura_d) / area(h interseção MS)

## Multiescala

A250, A500 e A1000 avaliam diretamente as evidências originais em cada malha.
A500 não é média de A250.
A1000 não é média de A500.

## Versionamento

RESULTADO = f(DATA_VERSION, RULE_VERSION, GRID_VERSION, MODEL_LIBRARY_VERSION)
