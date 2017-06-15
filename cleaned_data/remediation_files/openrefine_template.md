# Scopes OpenRefine Template

---

## Prefix

```
<?xml version="1.0" encoding="UTF-8"?>
<modsCollection xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
```

## Row Template

```
<mods xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
{{if(cells['identifier_file'].value != "IGNORE", '<identifier type="filename">' + cells['identifier_file'].value +'</identifier>', '')}}
{{if(cells['title'].value != "IGNORE", '<titleInfo><title>' + cells['title'].value + '</title></titleInfo>', '')}}
{{if(cells['title_other'].value != "IGNORE", '<titleInfo type="alternative"><title>' + cells['title_other'].value + '</title></titleInfo>', '')}}
{{if(cells['abstract'].value != "IGNORE", '<abstract>' + cells['abstract'].value + '</abstract>', '')}}
{{if(cells['date_text'].value != "IGNORE", '<originInfo><dateCreated>' + cells['date_text'].value + '</dateCreated>' + if(cells['place_of_origin'].value != "IGNORE", '<place><placeTerm type="text">' + cells['place_of_origin'].value + '</placeTerm></place>', '') + '</originInfo>', '')}}
<relatedItem displayLabel='Collection' type='host'><titleInfo><title>Sue K. Hicks Papers</title></titleInfo><identifier type='local'>MPA.0136</identifier></relatedItem>
<location><physicalLocation>University of Tennessee, Knoxville.  Special Collections</physicalLocation>{{if(cells['shelf_locator'].value != "IGNORE", '<shelfLocator>' + cells['shelf_locator'].value + '</shelfLocator>', '')}}</location>
{{if(cells['extent'].value != "IGNORE", '<physicalDescription><extent>' + cells['extent'].value + '</extent>' + '<digitalOrigin>reformatted digital</digitalOrigin>' + if(cells['form'].value != "IGNORE", '<form>' + cells['form'].value + '</form>', '') +'</physicalDescription>', '')}}
{{if(cells['genre'].value != "IGNORE", '<genre>' + cells['genre'].value + '</genre>', '')}}
{{if(cells['language'].value != "IGNORE", '	<language><languageTerm type="code" authority="iso639-2b">' + cells['language'].value + '</languageTerm></language>', '')}}
{{if(cells['name_value'].value != "IGNORE", '<name' + if(cells['name_uri'].value != "IGNORE", ' authority="lcnaf" valueURI="' + cells['name_uri'].value + '"', '') + '><namePart>' + cells['name_value'].value + '</namePart>' + if(cells['name_role'].value != "IGNORE", '<role><roleTerm>' + cells['name_role'].value + '</roleTerm></role>', '') + '</name>','')}}
{{if(cells['name2_value'].value != "IGNORE", '<name' + if(cells['name2_uri'].value != "IGNORE", ' authority="lcnaf" valueURI="' + cells['name2_uri'].value + '"', '') + '><namePart>' + cells['name2_value'].value + '</namePart>' + if(cells['name_role 2'].value != "IGNORE", '<role><roleTerm>' + cells['name_role 2'].value + '</roleTerm></role>', '') + '</name>','')}}
{{if(cells['subject_topical'].value != "IGNORE", '<subject><topic>' + cells['subject_topical'].value + '</topic></subject>', '')}}
{{if(cells['subject_topical 2'].value != "IGNORE", '<subject><topic>' + cells['subject_topical 2'].value + '</topic></subject>', '')}}
{{if(cells['subject_geographic'].value != "IGNORE", '<subject><geographic>' + cells['subject_geographic'].value + '</geographic></subject>', '')}}
{{if(cells['subject_name'].value != "IGNORE", '<subject><name><namePart>' + cells['subject_name'].value + '</namePart></name></subject>', '')}}
{{if(cells['rights'].value != "IGNORE", '<accessCondition type="use and reproduction"' + if(cells['rights_uri'].value !="IGNORE", ' xlink:href="' + cells['rights_uri'].value + '"', '') + '>' + cells['rights'].value + '</accessCondition>', '')}}
{{if(cells['public_note'].value != "IGNORE", '<note>' + cells['public_note'].value + '</note>', '')}}
{{if(cells['public_note 2'].value != "IGNORE", '<note>' + cells['public_note 2'].value + '</note>', '')}}
{{if(cells['note_provenance'].value != "IGNORE", '<note type="provenance">' + cells['note_provenance'].value + '</note>', '')}}
<recordInfo>
	<recordContentSource>University of Tennessee, Knoxville. Libraries</recordContentSource
    <languageOfCataloging>
    	<languageTerm type="code" authority="iso639-2b">eng</languageTerm>
    </languageOfCataloging>
    <recordOrigin>Created and edited in general conformance to MODS Guidelines (Version 3.5).</recordOrigin>
</recordInfo>
<relatedItem displayLabel="Project" type="host">
      <titleInfo>
         <title>Of Monkeys and Men: Public and Private Views from the Scopes Trial</title>
      </titleInfo>
</relatedItem>
</mods>
```

## Row Separator

**BLANK**


## Suffix

```
</modsCollection>
```

## The Original Bad Export Template

Keeping this so we can remember how nutty this wa.

```
<mods xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
  <abstract>{{jsonize(cells["abstract"].value).replace('"', '')}}</abstract>
  <abstract>{{jsonize(cells["abstract 1"].value).replace('"', '')}}</abstract>
  <abstract>{{jsonize(cells["abstract 2"].value).replace('"', '')}}</abstract>
  <relatedItem displayLabel="Collection" type="host">
    <titleInfo>
      <title>{{jsonize(cells["collection"].value).replace('"', '')}}</title>
    </titleInfo>
    <identifier>{{jsonize(cells["collection_identifier"].value).replace('"', '')}}</identifier>
  </relatedItem>
  <relatedItem displayLabel="Project" type="host">
    <titleInfo>
      <title>Of Monkeys and Men: Public and Private Views from the Scopes Trial</title>
    </titleInfo>
  </relatedItem>
  <genre>{{jsonize(cells["genre"].value).replace('"', '')}}</genre>
  <genre>{{jsonize(cells["genre 1"].value).replace('"', '')}}</genre>
  <genre>{{jsonize(cells["genre 2"].value).replace('"', '')}}</genre>
  <relatedItem type="host">
    <titleInfo>
      <title>{{jsonize(cells["host_title"].value).replace('"', '')}}</title>
    </titleInfo>
  </relatedItem>
  <identifier>{{jsonize(cells["identifier"].value).replace('"', '')}}</identifier>
  <identifier>{{jsonize(cells["identifier 2"].value).replace('"', '')}}</identifier>
  <identifier type="filename">{{jsonize(cells["identifier_file"].value).replace('"', '')}}</identifier>
  <identifier type="filename">{{jsonize(cells["identifier_file 2"].value).replace('"', '')}}</identifier>
  <identifier type="opac">{{jsonize(cells["identifier_opac"].value).replace('"', '')}}</identifier>
  <typeOfResource>{{jsonize(cells["item_type"].value).replace('"', '').toLowercase()}}</typeOfResource>
  <language>
    <languageTerm type="code" authority="iso639-2b">{{jsonize(cells["language"].value).replace('"', '')}}</languageTerm>
  </language>
  <language>
    <languageTerm type="code" authority="iso639-2b">{{jsonize(cells["language 1"].value).replace('"', '')}}</languageTerm>
  </language>
  <language>
    <languageTerm type="code" authority="iso639-2b">{{jsonize(cells["language 2"].value).replace('"', '')}}</languageTerm>
  </language>
  <recordInfo>
    <recordIdentifier>{{'record_'+jsonize(cells["identifier_file"].value).replace('"', '')}}</recordIdentifier>
    <recordContentSource>University of Tennessee, Knoxville. Libraries</recordContentSource>
    <languageOfCataloging>
      <languageTerm type="code" authority="iso639-2b">eng</languageTerm>
    </languageOfCataloging>
    <recordOrigin>Created and edited in general conformance to MODS Guidelines (Version 3.5).</recordOrigin>
   </recordInfo>
  <location>
    <physicalLocation>{{jsonize(cells["repository"].value).replace('"', '')}}</physicalLocation>
    <holdingSimple>
      <copyInformation>
        <shelfLocator>{{jsonize(cells["shelf_locator"].value).replace('"', '')}}</shelfLocator>
      </copyInformation>
    </holdingSimple>
  </location>
  <titleInfo>
    <title>{{jsonize(cells["title"].value).replace('"', '')}}</title>
  </titleInfo>
  <titleInfo type="alternative">
    <title>{{jsonize(cells["title 2"].value).replace('"', '')}}</title>
  </titleInfo>
  <name>
    <namePart>{{jsonize(cells["name"].value).replace('"', '')}}</namePart>
    <role>
      <roleTerm>{{jsonize(cells["name_role"].value).replace('"', '')}}</roleTerm>
    </role>
  </name>
  <name>
    <namePart>{{jsonize(cells["name 1"].value).replace('"', '')}}</namePart>
    <role>
      <roleTerm>{{jsonize(cells["name_role 1"].value).replace('"', '')}}</roleTerm>
    </role>
  </name>
  <name>
    <namePart>{{jsonize(cells["name 2"].value).replace('"', '')}}</namePart>
    <role>
      <roleTerm>{{jsonize(cells["name_role 2"].value).replace('"', '')}}</roleTerm>
    </role>
  </name>
  <name>
    <namePart>{{jsonize(cells["name 3"].value).replace('"', '')}}</namePart>
    <role>
      <roleTerm>{{jsonize(cells["name_role 3"].value).replace('"', '')}}</roleTerm>
    </role>
  </name>
  <name>
    <namePart>{{jsonize(cells["name 4"].value).replace('"', '')}}</namePart>
    <role>
      <roleTerm>{{jsonize(cells["name_role 4"].value).replace('"', '')}}</roleTerm>
    </role>
  </name>
  <subject>
    <topic>{{jsonize(cells["subject_topical"].value).replace('"', '')}}</topic>
  </subject>
  <subject>
    <topic>{{jsonize(cells["subject_topical 1"].value).replace('"', '')}}</topic>
  </subject>
  <subject>
    <topic>{{jsonize(cells["subject_topical 2"].value).replace('"', '')}}</topic>
  </subject>
  <subject>
    <topic>{{jsonize(cells["subject_topical 3"].value).replace('"', '')}}</topic>
  </subject>
  <subject>
    <topic>{{jsonize(cells["subject_topical 4"].value).replace('"', '')}}</topic>
  </subject>
  <subject>
    <topic>{{jsonize(cells["subject_topical 5"].value).replace('"', '')}}</topic>
  </subject>
  <subject>
    <geographic>{{jsonize(cells["subject_geographic"].value).replace('"', '')}}</geographic>
  </subject>
  <subject>
    <geographic>{{jsonize(cells["subject_geographic 1"].value).replace('"', '')}}</geographic>
  </subject>
  <subject>
    <geographic>{{jsonize(cells["subject_geographic 2"].value).replace('"', '')}}</geographic>
  </subject>
  <subject>
    <geographic>{{jsonize(cells["subject_geographic 3"].value).replace('"', '')}}</geographic>
  </subject>
  <subject>
    <geographic>{{jsonize(cells["subject_geographic 4"].value).replace('"', '')}}</geographic>
  </subject>
  <subject>
    <geographic>{{jsonize(cells["subject_geographic 5"].value).replace('"', '')}}</geographic>
  </subject>
  <subject>
    <name>
      <namePart>{{jsonize(cells["subject_name"].value).replace('"', '')}}</namePart>
    </name>
  </subject>
  <subject>
    <name>
      <namePart>{{jsonize(cells["subject_name 1"].value).replace('"', '')}}</namePart>
    </name>
  </subject>
  <subject>
    <name>
      <namePart>{{jsonize(cells["subject_name 2"].value).replace('"', '')}}</namePart>
    </name>
  </subject>
  <subject>
    <name>
      <namePart>{{jsonize(cells["subject_name 3"].value).replace('"', '')}}</namePart>
    </name>
  </subject>
  <subject>
    <name>
      <namePart>{{jsonize(cells["subject_name 4"].value).replace('"', '')}}</namePart>
    </name>
  </subject>
  <subject>
    <name>
      <namePart>{{jsonize(cells["subject_name 5"].value).replace('"', '')}}</namePart>
    </name>
  </subject>
  <note>{{jsonize(cells["public_note"].value).replace('"', '')}}</note>
  <note>{{jsonize(cells["public_note 1"].value).replace('"', '')}}</note>
  <note>{{jsonize(cells["public_note 2"].value).replace('"', '')}}</note>
  <note type="ownership">{{jsonize(cells["note_provenance"].value).replace('"', '')}}</note>
  <originInfo>
    <publisher>{{jsonize(cells["publisher"].value).replace('"', '')}}</publisher>
    <dateCreated>{{jsonize(cells["date_text"].value).replace('"', '')}}</dateCreated>
    <dateCreated keyDate="yes" encoding="edtf">{{jsonize(cells["date_key"].value).replace('"', '')}}</dateCreated>
    <place>
      <placeTerm type="text">{{jsonize(cells["place_of_origin"].value).replace('"', '')}}</placeTerm>
    </place>
    <place>
      <placeTerm type="text">{{jsonize(cells["place_of_origin 1"].value).replace('"', '')}}</placeTerm>
    </place>
    <place>
      <placeTerm type="text">{{jsonize(cells["place_of_origin 2"].value).replace('"', '')}}</placeTerm>
    </place>
  </originInfo>
  <physicalDescription>
    <extent>{{jsonize(cells["extent"].value).replace('"', '')}}</extent>
    <digitalOrigin>reformatted digital</digitalOrigin>
    <form>{{jsonize(cells["form"].value).replace('"', '')}}</form>
    <form>{{jsonize(cells["form 1"].value).replace('"', '')}}</form>
    <form>{{jsonize(cells["form 2"].value).replace('"', '')}}</form>
  </physicalDescription>
  <accessCondition>{{jsonize(cells["rights"].value).replace('"', '')}}</accessCondition>
  <note displayLabel="Transcription">{{jsonize(cells["transcriptions"].value).replace('"', '')}}</note>
</mods>
```