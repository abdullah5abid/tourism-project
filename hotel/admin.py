from django.contrib import admin
from .models import HotelOwner, HotelManager, CommonBathroom, CommonToilet, Bedrooms, HotelRegistration, HotelOwnerCombine

class HotelOwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'owner_ratio', 'owner_full_address', 'owner_telegraphic_address', 'owner_telephone')

class HotelManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_name', 'manager_ratio', 'manager_full_address', 'manager_telephone')

class CommonBathroomAdmin(admin.ModelAdmin):
    list_display = ('bathroom_no', 'bathroom_floor')

class CommonToiletAdmin(admin.ModelAdmin):
    list_display = ('toilet_no', 'toilet_floor')

class BedroomsAdmin(admin.ModelAdmin):
    list_display = ('bedrooms_type', 'rooms_type', 'corridors_type', 'attached_bathroom_type', 'bathrooms_type', 'toilets_type', 'cuisine_name')

class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'establishment_year', 'commision_date',
                    'telex_number', 'phone_number', 'hotel_address', 'telegraphic_address',
                    'province', 'town', 'street', 'ownership_nature', 'hotel_area',
                    'covered_area', 'area_type', 'land_cost', 'building_cost','furniture_cost',
                    'equipment_cost', 'working_capital', 'total_investment', 'floor_numbers',
                    'room_numbers', 'room_nature','visitor_room_detail', 'reception_hall_detail',
                    'reception_hall_area','cloak_room_detail','cloak_room_area','reading_room_detail',
                    'reading_room_area','restaurant_detail','restaurant_area','staircase_no',
                    'lifts_no','car_park','area_of_compound','area_of_garden',
                    'construction_completion_date','renovation_last_date','building_files','phones_provided',
                    'hotel_premises','restaurant_name','restaurant_detail_files','monthly_guests',
                    'business_season')

# class HotelOwnerCombineAdmin(admin.ModelAdmin):
#     model = HotelOwnerCombine
#     list_display = ('get_owner', 'get_hotel')

#     def get_owner(self, obj):
#         return obj.owner_id.owner_name

#     def get_hotel(self, obj):
#         return obj.hotel_id.hotel_name


admin.site.register(HotelOwner, HotelOwnerAdmin)
admin.site.register(HotelManager, HotelManagerAdmin)
admin.site.register(CommonBathroom, CommonBathroomAdmin)
admin.site.register(CommonToilet, CommonToiletAdmin)
admin.site.register(Bedrooms, BedroomsAdmin)
admin.site.register(HotelRegistration,HotelAdmin)
admin.site.register(HotelOwnerCombine)