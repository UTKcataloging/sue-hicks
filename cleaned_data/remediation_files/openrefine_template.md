# Scopes OpenRefine Template

---

## Prefix

```<?xml version="1.0" encoding="UTF-8"?>
<modsCollection xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
```

## Row Template

```
<mods xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
{{if(cells['identifier_file'].value != "IGNORE", '<identifier type="filename">' + cells['identifier_file'].value +'</identifier>', '')}}
{{if(cells['title'].value != "IGNORE", '<titleInfo><title>' + cells['title'].value + '</title></titleInfo>', '')}}
{{if(cells['title_other'].value != "IGNORE", '<titleInfo><title type="alternative">' + cells['title_other'].value + '</title></titleInfo>', '')}}
{{if(cells['abstract'].value != "IGNORE", '<abstract>' + cells['abstract'].value + '</abstract>', '')}}
{{if(cells['date_text'].value != "IGNORE", '<originInfo><dateCreated>' + cells['date_text'].value + '</dateCreated></originInfo>', '')}}
<relatedItem displayLabel='Collection' type='host'><titleInfo><title>Sue K. Hicks Papers</title></titleInfo><identifier type='local'>MPA.0136</identifier></relatedItem>
<location><physicalLocation>University of Tennessee, Knoxville.  Special Collections</physcialLocation>{{if(cells['shelf_locator'].value != "IGNORE", '<shelfLocator>' + cells['shelf_locator'].value + '</shelfLocator>', '')}}</location>
{{if(cells['extent'].value != "IGNORE", '<physicalDescription><extent>' + cells['extent'].value + '</extent>' + if(cells['form'].value != "IGNORE", '<form>' + cells['form'].value + '</form>', '') +''</physicalDescription>, '')}}
{{if(cells['genre'].value != "IGNORE", '<genre>' + cells['genre'].value + '</genre>', '')}}
{{if(cells['language'].value != "IGNORE", '	<language><languageTerm type="code" authority="iso639-2b">' + cells['language'].value + '</languageTerm></language>', '')}}
</mods>
```

## Row Separator

**BLANK**


## Suffix

```
</modsCollection>
```