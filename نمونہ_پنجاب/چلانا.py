from tinamit.mod.corrida import OpsSimulGrupo

from نمونہ_پنجاب.حکمت_عملی import حکمت_عملی
from نمونہ_پنجاب.نمونہ import نمونہ

اختیارات = OpsSimulGrupo(t=240, extern=list(حکمت_عملی.values()), nombre=list(حکمت_عملی))  # وقت کا قدم مہینہ میں ہے
نمونہ.simular_grupo(اختیارات, paralelo=False)
