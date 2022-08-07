from rest_framework import routers

import geography.views as GeographyViews

router = routers.DefaultRouter()
router.register(r"countries", GeographyViews.CountryViewSet)
