import os

from tinamit.conect import Conectado
from tinamit.envolt.bf.sahysmod import ModeloSAHYSMOD
from tinamit.envolt.mds import gen_mds
from tinamit.unids import nueva_unidad

متحرک_نظام = gen_mds(os.path.join(os.path.split(__file__)[0], 'ونشم', 'رچنا دوآب.vpm'))
ماحولیاتی = ModeloSAHYSMOD(os.path.join(os.path.split(__file__)[0], 'ساحسمود/ابتدائی.inp'))
نمونہ = Conectado(ماحولیاتی, متحرک_نظام)

nueva_unidad('season', 'month', 6)  # ۱ موسم میں ۶ مہینے ہوتے ہیں

# ماحولیاتی اور معاشی معاشرتی نمونوں کی جوڑای
نمونہ.conectar(var_mds='زمین نمکینی ٹینامٹ براے فصل الف', mds_fuente=False, var_bf="CrA - Root zone salinity crop A")
نمونہ.conectar(var_mds='زمین نمکینی ٹینامٹ براے فصل ب', mds_fuente=False, var_bf="CrB - Root zone salinity crop B")
نمونہ.conectar(var_mds='علاقائی حصہ فصل الف ٹینامٹ', mds_fuente=False,
               var_bf="Area A - Seasonal fraction area crop A")
نمونہ.conectar(var_mds='علاقائی حصہ فصل ب ٹینامٹ', mds_fuente=False,
               var_bf="Area B - Seasonal fraction area crop B")
نمونہ.conectar(var_mds='ٹینامیٹ زیر زمین پانی کی سطح', mds_fuente=False, var_bf="Dw - Groundwater depth")
نمونہ.conectar(var_mds='برقی موصل ڈی ڈبلوٹینامٹ', mds_fuente=False, var_bf='Cqf - Aquifer salinity')
نمونہ.conectar(var_mds='حتمی بارش', mds_fuente=True, var_bf='Pp - Rainfall')
نمونہ.conectar(var_mds='ایل سی', mds_fuente=True, var_bf='Lc - Canal percolation')
نمونہ.conectar(var_mds='آبپاشی فصل الف', mds_fuente=True, var_bf='IaA - Crop A field irrigation')
نمونہ.conectar(var_mds='آبپاشی فصل ب', mds_fuente=True, var_bf='IaB - Crop B field irrigation')
نمونہ.conectar(var_mds='جی ڈبلو', mds_fuente=True, var_bf='Gw - Groundwater extraction')
نمونہ.conectar(var_mds='ممکنہ آبی بخارات براۓ فصل الف', mds_fuente=True, var_bf='EpA - Potential ET crop A')
نمونہ.conectar(var_mds='ممکنہ آبی بخارات براۓ فصل ب', mds_fuente=True, var_bf='EpB - Potential ET crop B')
نمونہ.conectar(var_mds='آبپاشی کارکردگی', mds_fuente=True, var_bf='FsA - Water storage efficiency crop A')
نمونہ.conectar(var_mds='ایف ڈبلو', mds_fuente=True, var_bf='Fw - Fraction well water to irrigation')

نمونہ.mds.conectar_var_clima(var='کم سے کم درجہ حرارت ٹینامٹ', var_clima='Temperatura mínima', conv=1)
نمونہ.mds.conectar_var_clima(var='زیادہ سے زیادہ درجہ حرارت ٹینامٹ', var_clima='Temperatura máxima', conv=1)
نمونہ.mds.conectar_var_clima(var='بارش ٹینامٹ', var_clima='Precipitación', conv=0.001)
