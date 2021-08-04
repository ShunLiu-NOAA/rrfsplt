#python plot_jedi_tiles.py -i /scratch2/NCEPDEV/fv3-cam/scrub/Shun.Liu/jedilamda/Data/increment/20201013.000000.3dvar-gfs.fv_core.res.nc -t inc -v T -l 60 -g /scratch2/NCEPDEV/fv3-cam/scrub/Shun.Liu/guess.tm00/grid_spec.nc
#python plt_fv3lam_grid.py -g /scratch2/NCEPDEV/fv3-cam/scrub/Shun.Liu/guess.tm00/grid_spec.nc
python plt_fv3lam_grid.py -g /scratch2/NCEPDEV/fv3-cam/scrub/Shun.Liu/guess.tm00/GSL_gfs_data.tile7.halo0.nc \
                         -g1 /scratch2/NCEPDEV/fv3-cam/scrub/Shun.Liu/guess.tm00/EMC_gfs_data.tile7.nc
