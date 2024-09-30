# Turing Geovisualisation Engine (TGVE)

<div style="text-align: center;">
  <img src="https://user-images.githubusercontent.com/408568/108049506-44d59d00-7040-11eb-9f4e-0a083829bfa5.png" width="90%">
</div>

The Turing Geovisualisation Engine (TGVE) is a web-based, interactive visual analytics tool for geospatial data analysis. The paper is published in the procedings of EuroVIS 2023. It can be cited as:

```bib
@inproceedings {10.2312:evs.20231045,
  booktitle = {EuroVis 2023 - Short Papers},
  editor = {Hoellt, Thomas and Aigner, Wolfgang and Wang, Bei},
  title = {{TGVE: a Tool for Analysis and Visualization of Geospatial Data}},
  author = {Hama, Layik and Beecham, Roger and Lomax, Nik},
  year = {2023},
  publisher = {The Eurographics Association},
  ISBN = {978-3-03868-219-6},
  DOI = {10.2312/evs.20231045}
}
```

### Visualise geospatial
The TGVE deployed app here: https://tgve.github.io, can visualise any geospaital data including network data.
* give it a an accessible dataset from a remote server using the "defaultURL" key, like so:
https://tgve.github.io/app/?defaultURL=https://raw.githubusercontent.com/layik/eatlas-data/main/casualties_100.geojson

For example this is a sample from NPT scot dataset visualised by GitHub:
<div style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/91b203e9-dc7b-425b-b595-794315240f43" width="80%">
</div>

And in the TGVE app:
https://tgve.github.io/app/?defaultURL=https://raw.githubusercontent.com/nptscot/npt/main/data-raw/routes.geojson

<div style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/b63e1c5c-8098-4441-9416-169940d9b0e6" width="80%">
</div>



* upload datasets as one containign the geographic data or seprate files with a column defining the geographic data in a separate file.

* currently supports: csv, geojsn and shapefile formats.

### Custom DeckGL layer
This [tutorial](https://layik.github.io/decklayer) was written with lots of help from the Slack channels of the DeckGL developers.

The showcase for the custom DeckGL layer is visualising a custom rectangle with at least two variables. One to represent the colour of the rectangle and the other to represent the rotation angle of the rectangle.

The tutorial tells you how to build your custom layer using the DeckGL APIs.

<div style="text-align: center;">
  <img src="https://user-images.githubusercontent.com/408568/83650639-7a208480-a5b0-11ea-8a44-39d0dac0c31c.png" width="90%">
</div>

The same basic understanding of custom DeckGL layer can be used to generate any network visualisation idea for your hack.

### Hack idea

Edge bundling DeckGL layer. Instead of showing a hairball, show an image like this. This would require considerable thinking and a possible threshold as to when the alogorithm should be applied. The hack could also be a new layer for MapLibreGL or Leaflet.

<div style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/eefab641-d3db-441c-95b4-e6736015ce5a" width="90%">
</div>
