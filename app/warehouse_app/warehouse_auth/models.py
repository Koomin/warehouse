from django.contrib.auth.models import AbstractUser
from django.db import models
import json

class WarehouseFrontPermissions(models.Model):
    model = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.model


class WarehouseFrontActionPermissions(models.Model):
    action = models.CharField(max_length=128, null=False, blank=False)
    warehouse_front_permission = models.ForeignKey(WarehouseFrontPermissions, on_delete=models.CASCADE, null=False,
                                                   blank=False, related_name='actions')

    def __str__(self):
        return self.action


class WarehouseGroup(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    front_permissions = models.ManyToManyField(WarehouseFrontPermissions)

    def __str__(self):
        return self.name


class WarehouseUser(AbstractUser):
    group = models.ForeignKey(WarehouseGroup, on_delete=models.CASCADE, null=True, blank=True)
    login_permission = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_permission_table(self):
        models_permission = self.group.front_permissions.all()
        permission_dict = {
            'models': [],
            'actions': {}
        }
        for perm in models_permission:
            permission_dict['models'].append(perm.model)
            permission_dict['actions'][perm.model] = [x.action for x in perm.actions.all()]
        return json.dumps(permission_dict)

    def save(self, *args, **kwargs):
        if self.group:
            self.login_permission = True
        super().save(*args, **kwargs)
