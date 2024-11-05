'''Uploads multiple shp files by country and multple
   .nc file previously downloaded from CDS climate Atlas
   https://atlas.climate.copernicus.eu/atlas
   Crops .nc files by shp files,
   saves them in a folder and uploads it to the QGIS
   interface'''

import os
import processing
from qgis.core import QgsRasterLayer, QgsProject

def clip_rasters(raster_paths, shape_paths, out_folder):
    for raster_path in raster_paths:
        raster_name = os.path.basename(raster_path)
        for shape_path in shape_paths:
            country = os.path.basename(shape_path)[:5]
            out_path = os.path.join(out_folder, country + "_a_" + raster_name)
            processing.run("gdal:cliprasterbymasklayer",
                           {'INPUT': raster_path,
                            'MASK': shape_path,
                            'SOURCE_CRS': None,
                            'TARGET_CRS': None,
                            'TARGET_EXTENT': None,
                            'NODATA': None,
                            'ALPHA_BAND': False,
                            'CROP_TO_CUTLINE': True,
                            'KEEP_RESOLUTION': False,
                            'SET_RESOLUTION': False,
                            'X_RESOLUTION': None,
                            'Y_RESOLUTION': None,
                            'MULTITHREADING': False,
                            'OPTIONS': '',
                            'DATA_TYPE': 0,
                            'EXTRA': '',
                            'OUTPUT': out_path
                            })
            layer_name = f"{country}_{raster_name}_clip" 
            rlayer = QgsRasterLayer(out_path, layer_name)
            QgsProject.instance().addMapLayer(rlayer)

    print("Clipping complete")

# Example usage
rasters = [
    "/Users/ecompu/Desktop/Climate/Maps/ERA5_dry_days.nc",
    "/Users/ecompu/Desktop/Climate/Maps/ERA5_mean_temp.nc"
]

shapes = [
    "/Users/ecompu/Desktop/Climate/Shape_files/KEN_adm0.shp",
    "/Users/ecompu/Desktop/Climate/Shape_files/UGA_adm0.shp"
]

output_folder = "/Users/ecompu/Desktop/Climate/Clipped_files/"

clip_rasters(rasters, shapes, output_folder)