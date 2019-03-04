from django.contrib import admin
from .models import Vehiculo
from .models import Estado
from .models import Cliente
from .models import Usuario
from .models import Poliza
from .models import Incidente
from .models import Archivo
from .models import Comentarios


admin.site.register(Vehiculo)
admin.site.register(Estado)
admin.site.register(Cliente)
admin.site.register(Usuario)
admin.site.register(Poliza)
admin.site.register(Incidente)
admin.site.register(Archivo)
admin.site.register(Comentarios)