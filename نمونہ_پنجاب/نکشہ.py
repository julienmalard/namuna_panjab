import os

from tinamit.geog.mapa import Agua, Calle, FormaEstática, Bosque, Ciudad, FormaDinámicaNumérica

base_dir = os.path.dirname(os.path.realpath(__file__))

base_dir_shp = os.path.join(base_dir, 'شکلیں')

چکور = FormaDinámicaNumérica(os.path.join(base_dir_shp, 'اندرونی_چکور.shp'), col_id='Polygon_ID')

باہر = FormaEstática(os.path.join(base_dir_shp, 'بہرونی_چکور.shp'), color='#edf4da', llenar=False, alpha=1)
دریا = Agua(os.path.join(base_dir_shp, 'دریا.shp'))
نہر = Agua(os.path.join(base_dir_shp, 'نہر.shp'))
جنگل = Bosque(os.path.join(base_dir_shp, 'جنگل.shp'))
سہر = Ciudad(os.path.join(base_dir_shp, 'شہر.shp'))
سڑک = Calle(os.path.join(base_dir_shp, 'سڑک.shp'))
