
#title = "ESAP"

# the url location of the frontend application,
# this makes it possible to install multiple instances in different directories on the webserver
# that all have their own urls like 'http://esap.astron.nl/esap-gui-dev/queries'
frontend_basename="esap-gui"

logo = "https://alta.astron.nl/alta-static/images/esap/esap_logo.png"

# definition of the navigation bar
nav1 = {'title': 'Archives', 'route': '/archives'}
nav2 = {'title': 'Datasets', 'route': '/datasets'}
nav3 = {'title': 'Telescopes', 'route': '/telescopes'}
nav4 = {'title': 'Query', 'route': '/query'}
nav5 = {'title': 'Settings', 'route': '/about'}
navbar = [nav1,nav2,nav3,nav4,nav5]

# definition of the query
query_schema = {
  "title": "ESAP Query",
  "type": "object",
  "properties": {
    "institute": {
      "type": "string",
      "title": "Institute",
      "default": "all",
      "enum": ["all","Astron"],
      "enumNames": ["all","astron"]
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
      "title": "DataProduct Subtype",
      "default": "all",
      "enum": ["all","continuumMF","imageCube","beamCube"],
      "enumNames": ["all","continuumMF","imageCube","beamCube"]
    },
    "startdate": {
      "type": "string",
      "format" : "date",
      "title": "Start Date"
    }
    ,
    "enddate": {
      "type": "string",
      "format" : "date",
      "title": "End Date"
    },
    "instrument": {
      "type": "string",
      "title": "Instrument",
      "enum": ["all","continuumMF","imageCube","beamCube"],
    }
  }
}

