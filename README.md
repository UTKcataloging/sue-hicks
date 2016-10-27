# sue-hicks #

An xsl stylesheet to convert a modsCollection to a series of individual MODS records.
* drops elements with 'null' text nodes
* (_attempts_ at) processing `name/namePart` elements that contain the valueURI for the `name`
* splits the modsCollection on each mods child (this could be genericized a bit more).
