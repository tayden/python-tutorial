##  Shapely API example

[class Polygon(exterior[, interiors=None])](http://toblerity.org/shapely/manual.html#polygons)

    from shapely.geometry import Polygon
    polygon = Polygon([(0, 0), (1, 1), (1, 0)])
    polygon.area

    output>> 0.5

* interiors parameter is optional.  
* Documentation describes format for exterior and the methods a Polygon has
