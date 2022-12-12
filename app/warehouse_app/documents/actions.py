from django.contrib import admin, messages


@admin.action(description='Export selected to optima')
def export_to_optima(modeladmin, request, queryset):
    objects_saved = 0
    for obj in queryset.filter(exported=False):
        saved = obj.save_to_optima()
        if saved:
            objects_saved += 1
    if objects_saved != 0:
        messages.add_message(request, messages.INFO, f'{objects_saved}/{queryset.count()} documents saved to Optima.')
    else:
        messages.add_message(request, messages.WARNING, f'None of documents was saved to Optima.')


@admin.action(description='Change status to active')
def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Change status to inactive')
def set_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description='Change status to realized')
def change_issued(modeladmin, request, queryset):
    queryset.update(issued=True, realized=True)
