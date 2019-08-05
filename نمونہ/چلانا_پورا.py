from tinamit.geog.mapa import dibujar_mapa_de_res
from tinamit.mod.clima import Clima
from tinamit.mod.corrida import OpsSimulGrupoCombin
from tinamit.tiempo import EspecTiempo
from تقدیر.ذرائع import سی_اس_وی

from نمونہ.نمونہ import نمونہ
from . import نکشہ
from .حکمت_عملی import حکمت_عملی

آبوہوا_کا_خاکہ = [None, '۸.۵']

موسم_مشاہدات = سی_اس_وی(
    مسل='موسم/مشاہدہ بارش.csv', عرض=32.178207, طول=73.217391, بلندی=217,
    تبديل_ستون={'بارش': 'بارش (ملیمیٹر)', 'تاریخ': 'مہینہ'}
)
موسم = Clima(lat=32.178207, long=73.217391, elev=217, fuentes=موسم_مشاہدات)

if __name__ == '__main__':

    # وقت کا قدم مہینہ میں ہے
    و = EspecTiempo(n_pasos=12 * 50, f_inic='۱۹۸۹۱۱۰۱')
    اختیارات = OpsSimulGrupoCombin(t=و, extern=list(حکمت_عملی.values()), clima=موسم, nombre='رچنا دوآب')

    نتائج = نمونہ.simular_grupo(اختیارات)

    for خاکہ in نتائج:
        dibujar_mapa_de_res(
            نکشہ.چکور, خاکہ, t=(0, 12 * 50), var='ٹینامیٹ زیر زمین پانی کی سطح', directorio='نتیجہ',
            otras_formas=[نکشہ.باہر, نکشہ.دریا, نکشہ.نہر]
        )
