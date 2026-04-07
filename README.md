# ELC_Paper1

Code to reproduce maps, masks, and figures from Nofi et al. (2025a) "Nearly Full-Sky Low-Multipole CMB Temperature Anisotropy: I. Foreground Cleaned Maps" (https://arxiv.org/abs/2509.03718).

### Cleaned CMB Maps

We recommend the use of the **final cleaned maps** produced via the final cleaning procedure described in Section 3.6. These maps are referred to as **External Linear Combination (ELC) maps** and are available in the [ELC_Maps/](ELC_Maps/) directory.

### Data Requirements
Note that we provide copies of the smoothed, downgraded template files used in the foreground cleaning in the [Templates/](Templates/) directory.
* Planck frequency maps  
  Available on the Planck Legacy Archive (PLA):  
  https://pla.esac.esa.int/#maps
* WMAP frequency maps  
  Available on LAMBDA:  
  https://lambda.gsfc.nasa.gov/product/wmap/dr5/maps_band_smth_r9_i_9yr_get.html
* Planck 545 GHz  
  Available on Planck Legacy Archive (PLA):  
  https://pla.esac.esa.int/#maps
* Planck 857 GHz  
  Available on Planck Legacy Archive (PLA):  
  https://pla.esac.esa.int/#maps
* Planck Type 2 CO J=1-0  
  Available on Planck Legacy Archive (PLA):  
  https://pla.esac.esa.int/#maps
* WMAP MEM free-free  
  Available on LAMBDA:  
  https://lambda.gsfc.nasa.gov/product/wmap/dr5/mem_maps_get.html
* Haslam 408 MHz destriped  
  Available on LAMBDA:   
  https://lambda.gsfc.nasa.gov/product/foreground/fg_2014_haslam_408_get.html
* DIRBE 240 μm ZSMA    
  Available on CADE:    
  https://cade.irap.omp.eu/dokuwiki/doku.php?id=dirbe 

### Structure
* [ELC_Maps/](ELC_Maps/)  
  Final foreground-cleaned maps (recommended for analysis)
* [ELC_Masks/](ELC_Masks/)  
  Masks used for cleaning and statistical analysis in Nofi et al. 2025a
* [Figure_Notebooks/](Figure_Notebooks/)  
  Notebooks to reproduce all figures in Nofi et al. 2025a
* [Templates/](Templates/)  
  Templates used for cleaning at a common resolution
* 1_Downgrade&Smooth_Templates.ipynb  
  Downgrades and smooths templates to common resolution
* 2_Initial_Cleaning.ipynb  
  Implements the initial cleaning procedure (Section 3.3)
* 3_Percent_Masks.ipynb  
  Generates the sky masks used in the analysis (Section 3.5)
* 4_Final_Cleaning.ipynb  
  Implements the final cleaning procedure used to produce the ELC maps (Section 3.6)

### Contact:
Hayley Nofi: hnofi1@jh.edu
