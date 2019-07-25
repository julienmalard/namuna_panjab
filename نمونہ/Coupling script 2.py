import os

from tinamit.conect import Conectado
from tinamit.geog.mapa import dibujar_mapa, FormaDinámicaNumérica, Agua, Calle, FormaEstática, Bosque, Ciudad
from tinamit.envolt.mds import gen_mds
from tinamit.envolt.bf.sahysmod import ModeloSAHYSMOD
from tinamit.mod import EspecTiempo
from tinamit.unids.conv import nueva_unidad

if __name__ == '__main__':
    use_simple = True
    climate_change = True

    base_dir = os.path.dirname(os.path.realpath(__file__))

    base_dir_shp = os.path.join(base_dir, 'Shape_files')
    # Rechna_Doab.agregar_frm_regiones(os.path.join(base_dir_shp, 'Internal_Polygon.shp'), col_id='Polygon_ID')

    baher = FormaEstática(os.path.join(base_dir_shp, 'External_Polygon.shp'), color='#edf4da', llenar=False, alpha=1)
    driya = Agua(os.path.join(base_dir_shp, 'RIVR.shp'))
    naher = Agua(os.path.join(base_dir_shp, 'CNL_Arc.shp'))
    jngl = Bosque(os.path.join(base_dir_shp, 'Forst_polygon.shp'))
    shr = Ciudad(os.path.join(base_dir_shp, 'buildup_Polygon.shp'))
    srk = Calle(os.path.join(base_dir_shp, 'road.shp'))

    # 1. Simple runs
    runs_simple = {'CWU': {'ایک کنواں کا حجم': 100.8, 'ایف ڈبلو': 0.8, 'حکمت عملی نہر پختگی': 0,
                                          'حکمت عملی تالاب': 0, 'حکمت عملی براے آبپاشی کارکردگی': 0}
                   # 'VD': {'Capacity per tubewell': 153.0, 'Fw': 0.8, 'Policy Canal lining': 0,
                   #        'Policy RH': 0, 'Policy Irrigation improvement': 0},
                   # 'CL': {'Capacity per tubewell': 100.8, 'Fw': 0.8, 'Policy Canal lining': 1,
                   #        'Policy RH': 0, 'Policy Irrigation improvement': 0},
                   # 'RWH': {'Capacity per tubewell': 100.8, 'Fw': 0.8, 'Policy Canal lining': 0,
                   #         'Policy RH': 1, 'Policy Irrigation improvement': 0},
                   # 'PIM': {'Capacity per tubewell': 100.8, 'Fw': 0.8, 'Policy Canal lining': 0,
                   #         'Policy RH': 0, 'Policy Irrigation improvement': 1}
                   }

    # 2. Complex runs
    # Switch values for runs
    ops = {
        'ایک کنواں کا حجم': [153.0, 100.8],
        'ایف ڈبلو': [0.8, 0],
        'حکمت عملی نہر پختگی': [0, 1],
        'حکمت عملی تالاب': [0, 1],
        'حکمت عملی براے آبپاشی کارکردگی': [0, 1]
    }

    runs_complex = {}

    for cp in ops['ایک کنواں کا حجم']:
        for fw in ops['ایف ڈبلو']:
            for cl in ops['حکمت عملی نہر پختگی']:
                for rw in ops['حکمت عملی تالاب']:
                    for ir in ops['حکمت عملی براے آبپاشی کارکردگی']:
                        run_name = 'TC {}, Fw {}, CL {}, RW {}, II {}'.format(
                            cp, fw, cl, rw, ir
                        )

                        runs_complex[run_name] = {
                            'ایک کنواں کا حجم': cp,
                            'ایف ڈبلو': fw,
                            'حکمت عملی نہر پختگی': cl,
                            'حکمت عملی تالاب': rw,
                            'حکمت عملی براے آبپاشی کارکردگی': ir
                        }

    # 3. Now create the model
    # Create a coupled model instance
    mds = gen_mds(os.path.join(os.path.split(__file__)[0], 'ونشم', 'Tinamit_Rechna_urdu.vpm'))
    bf = ModeloSAHYSMOD('495anew1.inp')
    modelo = Conectado(bf, mds)
    nueva_unidad('season', 'month', 6)

    # Couple models(Change variable names as needed)
    modelo.conectar(var_mds='زمین نمکینی ٹینامٹ براے فصل الف', mds_fuente=False, var_bf="CrA - Root zone salinity crop A")
    modelo.conectar(var_mds='زمین نمکینی ٹینامٹ براے فصل ب', mds_fuente=False, var_bf="CrB - Root zone salinity crop B")
    modelo.conectar(var_mds='علاقائی حصہ فصل الف ٹینامٹ', mds_fuente=False,
                    var_bf="Area A - Seasonal fraction area crop A")
    modelo.conectar(var_mds='علاقائی حصہ فصل ب ٹینامٹ', mds_fuente=False,
                    var_bf="Area B - Seasonal fraction area crop B")
    modelo.conectar(var_mds='ٹینامیٹ زیر زمین پانی کی سطح', mds_fuente=False, var_bf="Dw - Groundwater depth")
    modelo.conectar(var_mds='برقی موصل ڈی ڈبلوٹینامٹ', mds_fuente=False, var_bf='Cqf - Aquifer salinity')
    modelo.conectar(var_mds='حتمی بارش', mds_fuente=True, var_bf='Pp - Rainfall')
    modelo.conectar(var_mds='ایل سی', mds_fuente=True, var_bf='Lc - Canal percolation')
    modelo.conectar(var_mds='آبپاشی فصل الف', mds_fuente=True, var_bf='IaA - Crop A field irrigation')
    modelo.conectar(var_mds='آبپاشی فصل ب', mds_fuente=True, var_bf='IaB - Crop B field irrigation')
    modelo.conectar(var_mds='جی ڈبلو', mds_fuente=True, var_bf='Gw - Groundwater extraction')
    modelo.conectar(var_mds='ممکنہ آبی بخارات براۓ فصل الف', mds_fuente=True, var_bf='EpA - Potential ET crop A')
    modelo.conectar(var_mds='ممکنہ آبی بخارات براۓ فصل ب', mds_fuente=True, var_bf='EpB - Potential ET crop B')
    modelo.conectar(var_mds='آبپاشی کارکردگی', mds_fuente=True, var_bf='FsA - Water storage efficiency crop A')
    modelo.conectar(var_mds='ایف ڈبلو', mds_fuente=True, var_bf='Fw - Fraction well water to irrigation')

    # 4. Finally, run the model
    if use_simple:
        runs = runs_simple
    else:
        runs = runs_complex

    if not climate_change:
        # Run the model for all desired runs
        for name, run in runs.items():
            print('Runing model {}.\n-----------------'.format(name))

            # Simulate the coupled model
            modelo.simular(40, extern=run, nombre=name)  # time step and final time are in months

            # Draw maps
            # modelo.dibujar_mapa(geog=Rechna_Doab, corrida=name, var='Watertable depth Tinamit', directorio='Maps')
            # modelo.dibujar_mapa(geog=Rechna_Doab, corrida=name, var='Soil salinity Tinamit CropA', directorio='Maps')
    else:
        # Climate change runs
        location = Lugar(lat=32.178207, long=73.217391, elev=217)
        location.observar((os.path.join(base_dir, 'مشاہدہ بارش.csv')), meses='مہینہ', años='سال',
                          cols_datos={'Precipitación': 'بارش (ملیمیٹر)',
                                      'Temperatura mínima': 'درجہ_حرارت_کم',
                                      'Temperatura máxima': 'درجہ_حرارت_زیادہ'
                                      },
                          conv={'Precipitación': 1,
                                'Temperatura mínima': 1,
                                'Temperatura máxima': 1})

        modelo.mds.conectar_var_clima(var='کم سے کم درجہ حرارت ٹینامٹ', var_clima='Temperatura mínima', conv=1)
        modelo.mds.conectar_var_clima(var='زیادہ سے زیادہ درجہ حرارت ٹینامٹ', var_clima='Temperatura máxima', conv=1)
        modelo.mds.conectar_var_clima(var='بارش ٹینامٹ', var_clima='Precipitación', conv=0.001)
        modelo.estab_conv_unid_tiempo('mes', unid='season', factor=6)

        vals_inic = {x: {'mds': v} for x, v in runs.items()}
        dibs = [dict(geog=Rechna_Doab, var='ٹینامیٹ زیر زمین پانی کی سطح', directorio='Maps'),
                dict(geog=Rechna_Doab, var='زمین نمکینی ٹینامٹ براے فصل الف', colores=-1, directorio='Maps')]

        modelo.simular_grupo(paso=1, t_final=10 * 2, t_inic='01/11/1989', lugar_clima=location,
                             recalc_clima=False, clima=[0, 2.6, 4.5, 6.0, 8.5], vals_inic=vals_inic, combinar=True,
                             nombre_corrida='', dibujar=dibs, paralelo=True)
