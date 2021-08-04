#!/usr/bin/env python3
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import netCDF4 as nc
import numpy as np
import argparse
import glob
import os
from datetime import datetime

def plot_world_map(lon, lat, lont, latt, plotpath):
    # plot generic world map
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.add_feature(cfeature.GSHHSFeature(scale='auto'))
    ax.set_extent([-138, -56.5, 17.5, 60.0],crs=ccrs.PlateCarree())
#   ax.set_extent([-100.25, -100.0, 40, 40.25],crs=ccrs.PlateCarree())
    cmap = 'viridis'
    cbarlabel = 'grid'
#       cmap = 'bwr'
    asize=lon.shape 
    print(asize)
    nx=asize[0]
    ny=asize[1]

    lon_left=np.empty(nx)
    lat_left=np.empty(nx)
    lon_left=lon[:,0]
    lat_left=lat[:,0]

    lon_right=np.empty(nx)
    lat_right=np.empty(nx)
    lon_right=lon[:,ny-1]
    lat_right=lat[:,ny-1]

    lon_top=np.empty(ny)
    lat_top=np.empty(ny)
    lon_top=lon[0,:]
    lat_top=lat[0,:]

    lon_bot=np.empty(ny)
    lat_bot=np.empty(ny)
    lon_bot=lon[nx-1,:]
    lat_bot=lat[nx-1,:]

    cs = ax.scatter(lon_left, lat_left,c='r')
    cs = ax.scatter(lon_right,lat_right,c='r')
    cs = ax.scatter(lon_top, lat_top,c='r')
    cs = ax.scatter(lon_bot,lat_bot,c='r')

    asize=lont.shape
    print(asize)
    nx=asize[0]
    ny=asize[1]

    lon_left=np.empty(nx)
    lat_left=np.empty(nx)
    lon_left=lont[:,0]
    lat_left=latt[:,0]

    lon_right=np.empty(nx)
    lat_right=np.empty(nx)
    lon_right=lont[:,ny-1]
    lat_right=latt[:,ny-1]

    lon_top=np.empty(ny)
    lat_top=np.empty(ny)
    lon_top=lont[0,:]
    lat_top=latt[0,:]

    lon_bot=np.empty(ny)
    lat_bot=np.empty(ny)
    lon_bot=lont[nx-1,:]
    lat_bot=latt[nx-1,:]

    cs = ax.scatter(lon_left, lat_left,c='b')
    cs = ax.scatter(lon_right,lat_right,c='b')
    cs = ax.scatter(lon_top, lat_top,c='b')
    cs = ax.scatter(lon_bot,lat_bot,c='b')



#   exit()
#   cs = ax.scatter(lon, lat,s=35,marker="o",c='r')
#   cs = ax.scatter(lont, latt,s=35,marker="s",c='b')
#   cs = ax.pcolormesh(lons, lats, data,vmin=vmin,vmax=vmax,cmap=cmap)
#   cb = plt.colorbar(cs, orientation='horizontal', shrink=0.5, pad=.04)
#   cb.set_label(cbarlabel, fontsize=12)

#   plttitle = 'JEDI FV3 grid in 0.25x0.25 box by %s' % (os.environ['LOGNAME'])
    plttitle = 'Blue: EMC 3km CONUS v.s. Red: GSL 3km CONUS'
    plt.title(plttitle)
    plt.savefig(plotpath,bbox_inches='tight',dpi=100)
    plt.close('all')

def read_var(geopath,geopath1):
    tmpdata = nc.Dataset(geopath,'r')
    tmplat = tmpdata.variables['geolat'][:]
    tmpdata.close()

    tmpdata = nc.Dataset(geopath1,'r')
    tmplatt = tmpdata.variables['geolat'][:]
    tmpdata.close()

    arrayshapet = tmplatt.shape
    lontout = np.empty(arrayshapet)
    lattout = np.empty(arrayshapet)

    arrayshape = tmplat.shape
    lonout = np.empty(arrayshape)
    latout = np.empty(arrayshape)

    geonc = nc.Dataset(geopath)
    lat = geonc.variables['geolat'][:]
    lon = geonc.variables['geolon'][:]
    geonc.close()

    geonc = nc.Dataset(geopath1)
    latt = geonc.variables['geolat'][:]
    lont = geonc.variables['geolon'][:]
    geonc.close()

    latout[:,:] = lat
    lonout[:,:] = lon
    lattout[:,:] = latt
    lontout[:,:] = lont

    return lonout, latout, lontout, lattout


def gen_figure(geopath,geopath1):
    # read the files to get the 2D array to plot
    lon, lat, lont, latt = read_var(geopath,geopath1)
    now=datetime.now()
    t=now.strftime("_%Y%m%d%H%M")
    plotpath ='fv3grid'+t+'.png'
    plot_world_map(lon, lat, lont, latt, plotpath)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-g', '--geoin', help="path to prefix of input files with geolat/geolon", required=True)
    ap.add_argument('-g1', '--geoin1', help="path to prefix of input files with geolat/geolon1", required=True)
    MyArgs = ap.parse_args()
    gen_figure(MyArgs.geoin,MyArgs.geoin1)
