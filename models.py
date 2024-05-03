# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TEmpresa(models.Model):
    id_empresa = models.IntegerField(primary_key=True)
    empresa = models.CharField(max_length=45)
    cuit = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 't_empresa'


class TFabrica(models.Model):
    id_fabrica = models.IntegerField(primary_key=True)
    fecha_fabricacion = models.CharField(max_length=50, blank=True, null=True)
    granja_fabricacion = models.IntegerField(blank=True, null=True)
    codigo_formula = models.IntegerField(blank=True, null=True)
    kilos_fabricados = models.IntegerField(blank=True, null=True)
    precio_costo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_fabrica'


class TFormulas(models.Model):
    id_formula = models.IntegerField(primary_key=True)
    tipo_formula = models.IntegerField(blank=True, null=True)
    pienso = models.CharField(max_length=45, blank=True, null=True)
    materia_prima = models.CharField(max_length=45, blank=True, null=True)
    id_materia_prima = models.IntegerField(blank=True, null=True)
    kilos = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fabricper = models.IntegerField(db_column='FABRICPER', blank=True, null=True)  # Field name made lowercase.
    fabricacu = models.IntegerField(db_column='FABRICACU', blank=True, null=True)  # Field name made lowercase.
    impperiod = models.DecimalField(db_column='IMPPERIOD', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    impacum = models.DecimalField(db_column='IMPACUM', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    control = models.CharField(db_column='CONTROL', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_formulas'
        db_table_comment = '\t'


class TMateriaPrima(models.Model):
    id_materia_prima = models.IntegerField(primary_key=True)
    materia_prima = models.CharField(max_length=45, blank=True, null=True)
    precio = models.DecimalField(max_digits=50, decimal_places=4, blank=True, null=True)
    precio_almacen = models.DecimalField(max_digits=50, decimal_places=4, blank=True, null=True)
    cantidad_inicial = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    cantidad_actual = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    entrada_periodo = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    entrada_acumulada = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    entrada_impuesto_periodo = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    entrada_impuesto_acumulado = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    existencia_real = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    salidas_periodo = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    salidas_acumuladas = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    salidas_impuesto_periodo = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    salidas_impuesto_acumuladas = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    diferencia_materia_prima = models.DecimalField(max_digits=50, decimal_places=0, blank=True, null=True)
    impuesto_diferencia_materia_prima = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_materia_prima'


class TProveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    proveedor = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    puntos = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    localidad = models.CharField(max_length=45, blank=True, null=True)
    provincia = models.CharField(max_length=45, blank=True, null=True)
    codigo_postal = models.CharField(max_length=45, blank=True, null=True)
    cuit = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_proveedor'
