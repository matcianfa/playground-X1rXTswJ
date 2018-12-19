def ma_fonction(lat_a,long_a,lat_b,long_b):
    rayon=6371.
    x=(long_b-long_a)*pi/180*cos((lat_a+lat_b)*pi/360)
    y=(lat_b-lat_a)*pi/180
    distance = rayon*sqrt(x**2+y**2)
    return (round(distance,3))
