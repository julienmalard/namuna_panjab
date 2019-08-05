import os

from tinamit.envolt.bf.sahysmod import ModeloSAHYSMOD

# ساحسمود کے ابتدائی کوائف کا راستا
راستا = os.path.dirname(__file__)
ابتدایئ_کوائف = os.path.join(راستا, 'ابتدائی.inp')

# ساحسمود کا جلد بنانا
نمونہ_ساحسمود = ModeloSAHYSMOD(archivo=ابتدایئ_کوائف)
