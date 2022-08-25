from django.contrib import admin

from warehouse.admin import WarehouseAdmin
from warehouse_auth.models import WarehouseUser, WarehouseGroup, WarehouseFrontPermissions, \
    WarehouseFrontActionPermissions


@admin.register(WarehouseUser)
class WarehouseUserAdmin(WarehouseAdmin):
    fields = (('username',), ('first_name', 'last_name'), ('is_staff', 'is_active'), 'group')


@admin.register(WarehouseGroup)
class WarehouseGroupAdmin(WarehouseAdmin):
    fields = ('name', 'front_permissions')


@admin.register(WarehouseFrontPermissions)
class WarehouseFrontPermissionsAdmin(WarehouseAdmin):
    fields = ('model',)


@admin.register(WarehouseFrontActionPermissions)
class WarehouseFrontActionPermissionsAdmin(WarehouseAdmin):
    fields = ('name', 'front_permissions',)
