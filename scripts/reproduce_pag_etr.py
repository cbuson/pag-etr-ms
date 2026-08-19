#!/usr/bin/env python3
from pathlib import Path
import geopandas as gpd
import pandas as pd
import json, hashlib

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/source"
GRIDS = ROOT / "data/grids"
OUT = ROOT / "results/reproduced"
OUT.mkdir(parents=True, exist_ok=True)

GEOLOGY = gpd.read_file(SOURCE / "mapa_geologico_ms.geojson")
RESOURCES = gpd.read_file(SOURCE / "mapa_recursos_minerais_ms.geojson")

# Evidence-selection rules frozen from the pilot
M2 = GEOLOGY[GEOLOGY["NOME"].fillna("").eq("Corpo Feixe dos Morros")].copy()
M4 = GEOLOGY[GEOLOGY["NOME"].fillna("").isin(["Formação Bocaina", "Formação Tamengo"])].copy()
P = RESOURCES[RESOURCES["SUBSTANCIAS"].fillna("").str.strip().eq("Fósforo")].copy()

M2.to_file(OUT / "reproduced_evidence_M2_Feixe_dos_Morros.geojson", driver="GeoJSON")
M4.to_file(OUT / "reproduced_evidence_M4_fosforitos.geojson", driver="GeoJSON")
P.to_file(OUT / "reproduced_pontos_fosforo.geojson", driver="GeoJSON")

expected = {250: {"cells":1554,"open":49,"m2":3,"m4":46}, 500:{"cells":793,"open":37,"m2":3,"m4":34}, 1000:{"cells":412,"open":24,"m2":2,"m4":22}}
summary=[]

for scale, gridfile in [(250,"malha_250km2.geojson"),(500,"malha_500km2.geojson"),(1000,"malha_1000km2.geojson")]:
    grid=gpd.read_file(GRIDS/gridfile)
    # Reproject evidence only if required. All frozen files are WGS84 in this package.
    m2=M2.to_crs(grid.crs) if M2.crs != grid.crs else M2
    m4=M4.to_crs(grid.crs) if M4.crs != grid.crs else M4
    pts=P.to_crs(grid.crs) if P.crs != grid.crs else P
    u2=m2.geometry.union_all()
    u4=m4.geometry.union_all()
    grid=grid.copy()
    grid["M2"]="NAO_AVALIAVEL"
    grid.loc[grid.geometry.intersects(u2),"M2"]="MODELO_ABERTO"
    grid["M4"]="NAO_AVALIAVEL"
    grid.loc[grid.geometry.intersects(u4),"M4"]="MODELO_ABERTO"
    # Point evidence opens M4 only in the cell(s) that contain or touch each observation.
    for geom in pts.geometry:
        if geom is not None and not geom.is_empty:
            grid.loc[grid.geometry.intersects(geom),"M4"]="MODELO_ABERTO"
    grid["PAG_ETR_ESTADO"]="NAO_AVALIAVEL"
    grid.loc[(grid["M2"]=="MODELO_ABERTO") | (grid["M4"]=="MODELO_ABERTO"),"PAG_ETR_ESTADO"]="MODELO_ABERTO"
    grid["MODELO_RESPONSAVEL"]=""
    grid.loc[grid["M2"]=="MODELO_ABERTO","MODELO_RESPONSAVEL"]="M2"
    grid.loc[grid["M4"]=="MODELO_ABERTO","MODELO_RESPONSAVEL"]="M4"
    # The current pilot has no overlap between M2 and M4; preserve both if that changes.
    both=(grid["M2"]=="MODELO_ABERTO") & (grid["M4"]=="MODELO_ABERTO")
    grid.loc[both,"MODELO_RESPONSAVEL"]="M2;M4"
    out=OUT/f"pag_etr_reproduced_{scale}km2.geojson"
    grid.to_file(out,driver="GeoJSON")
    counts={"scale_km2":scale,"cells":len(grid),"open":int((grid.PAG_ETR_ESTADO=="MODELO_ABERTO").sum()),"m2":int((grid.M2=="MODELO_ABERTO").sum()),"m4":int((grid.M4=="MODELO_ABERTO").sum())}
    counts["matches_expected"] = all(counts[k]==expected[scale][k] for k in ["cells","open","m2","m4"])
    summary.append(counts)

pd.DataFrame(summary).to_csv(OUT/"reproduction_summary.csv",index=False)
print(pd.DataFrame(summary).to_string(index=False))
if not all(x["matches_expected"] for x in summary):
    raise SystemExit("FAIL: reproduced counts do not match the frozen pilot")
print("PASS: M2/M4 spatial pilot reproduced at 250, 500 and 1000 km²")
