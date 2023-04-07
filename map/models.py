from django.contrib.gis.db import models
from django.contrib.gis.geos import Point, LineString, Polygon
from django.db.models import Manager as GeoManager


class Location(models.Model):
    """
    - PointField: Stores storing a 2D point, represented as a Point object.
    - LineStringField: Stores storing a line, represented as a LineString object.
    - PolygonField: Stores storing a polygon, represented as a Polygon object.
    - MultiPointField: Stores a collection of points, represented as a MultiPoint object.
    - MultiLineStringField: Stores a collection of lines, represented as a MultiLineString object.
    - MultiPolygonField: Stores a collection of polygons, represented as a MultiPolygon object.
    - GeometryCollectionField: Stores a collection of any type of geometry, represented as a GeometryCollection object.
    """

    name = models.CharField(max_length=255, null=True)
    point = models.PointField(null=True)
    line = models.LineStringField(null=True)
    polygon = models.PolygonField(null=True)
    multipoint = models.MultiPointField(null=True)
    multilinestring = models.MultiLineStringField(null=True)
    multipolygon = models.MultiPolygonField(null=True)
    geometrycollection = models.GeometryCollectionField(null=True)

    objects = GeoManager()

    def __str__(self):
        """
        String serializer.
        """
        return self.name
