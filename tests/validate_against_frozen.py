#!/usr/bin/env python3
from pathlib import Path
import geopandas as gpd
ROOT=Path(__file__).resolve().parents[1]
for scale in (250,500,1000):
    f=gpd.read_file(ROOT/f"results/frozen/pag_etr_{scale}km2.geojson")
    r=gpd.read_file(ROOT/f"results/reproduced/pag_etr_reproduced_{scale}km2.geojson")
    fo=set(f.loc[f.pag_etr_estado_geral=="MODELO_ABERTO","hex_id"])
    ro=set(r.loc[r.PAG_ETR_ESTADO=="MODELO_ABERTO","hex_id"])
    fm2=set(f.loc[f.pag_etr_m2_estado=="MODELO_ABERTO","hex_id"])
    rm2=set(r.loc[r.M2=="MODELO_ABERTO","hex_id"])
    fm4=set(f.loc[f.pag_etr_m4_estado=="MODELO_ABERTO","hex_id"])
    rm4=set(r.loc[r.M4=="MODELO_ABERTO","hex_id"])
    assert fo==ro, (scale,'overall',fo-ro,ro-fo)
    assert fm2==rm2, (scale,'M2',fm2-rm2,rm2-fm2)
    assert fm4==rm4, (scale,'M4',fm4-rm4,rm4-fm4)
    print(f"PASS {scale} km² · overall={len(fo)} · M2={len(fm2)} · M4={len(fm4)}")
