
# title = "ADEX"
logo = "https://alta.astron.nl/alta-static/images/esap/adex_logo.png"

# title = "ESFRI Science Analysis Platform"
#logo = "http://uilennest.net/static/media/tree9.da598501.png"

# the url location of the frontend application,
# this makes it possible to install multiple instances in different directories on the webserver
# that all have their own urls like 'http://esap.astron.nl/esap-gui-dev/queries'
frontend_basename="esap-gui"

# definition of the navigation bar
nav1 = {'title': 'Archives', 'route': '/archives'}
nav2 = {'title': 'Datasets', 'route': '/datasets'}
nav3 = {'title': 'Telescopes', 'route': '/telescopes'}
nav4 = {'title': 'Query', 'route': '/query'}
nav5 = {'title': 'Settings', 'route': '/about'}
navbar = [nav1,nav2,nav3,nav5]

# if datasets_enabled is set, then only these datasets are visible to the GUI
#datasets_enabled = ['apertif-observations','astron.ivoa.obscore']

# if datasets_disabled is set, then all datasets except these are returned to the GUI
datasets_disabled = ['nancay.ivoa.obscore']


# definition of the query
query_schema = {
  "title": "ASTRON Data Collection Query",
  "type": "object",
  "properties": {
    "institute": {
      "type": "string",
      "title": "Institute",
      "default": "Astron",
      "enum": ["all", "Astron"],
      "enumNames": ["all","ASTRON"]
    },

    "title": {
      "type": "string",
      "title": "Title",
      "default" : ""
    },
    "target": {
      "type": "string",
      "title": "Target"
    },
    "ra": {
      "type": "number",
      "title": "RA (degrees)",
      "default": 342.16
    },
    "dec": {
      "type": "number",
      "title": "dec (degrees)",
      "default": 33.94
    },
    "fov": {
      "type": "number",
      "title": "search radius (degrees)",
      "default": 10
    },
    "dataproduct_type": {
      "type": "string",
      "title": "DataProduct Type",
      "default": "all",
      "enum": ["all","image","cube"],
      "enumNames": ["all","image","cube"]
    },
    "dataproduct_subtype": {
      "type": "string",
      "title": "DataProduct Type",
      "default": "continuumMF",
      "enum": ["all","uncalibratedVisibility","continuumMF","continuumChunk","calibratedImage","polarisationImage","imageCube","beamCube","polarisationCube","pulsarTimingTimeSeries"],
      "enumNames": ["all","uncalibratedVisibility","continuumMF","continuumChunk","calibratedImage","polarisationImage","imageCube","beamCube","polarisationCube","pulsarTimingTimeSeries"]
    },
    "access_right": {
      "type": "string",
      "title": "Access right",
      "default": "public",
      "enum": ["all", "public"],
      "enumNames": ["all", "public"]
    },
  }
}