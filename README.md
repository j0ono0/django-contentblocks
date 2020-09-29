# Overview: Contentblocks Django App
A Django application that allows authors to create blocks of content for pre-defined locations in templates.

## Features
+ Multiple blocks per template location. allowing for granular content control 
+ Markdown parsing
+ Limited template variable parsing for authenticated users (accessing the request.user object)
+ Arbitary block ordering by assigning 'weight'
+ Publish and unpublish by date/time
+ Render based on authentication status

## Dependencies
Contentblocks allows authors to use markdown, ensure it is installed or remove the feature.
+ markdown (https://python-markdown.github.io/)

## Installing
Follow the installation process as per any Django app.
+ Add `contentblocks` to INSTALLED_APPS 
+ Include 'contentblocks.urls' into your base urls
+ Makemigration and migrate to update your database with the contentblock model

##  Templates
+ Add `{% load contentblock_extras %}` near the top of every template that will be displaying contentblocks.

+ Insert `{% contentblock '<location_label>' request.user %}` where you want the contentblocks to appear. Replace `<location_label>` with your own label. `request.user` is optional and should be removed if the block is not intended to support template variables

+ Add your location_label into the `LOCATIONS` variable found in models.py

## Notes
A db query is done for each block location. The query code is stored in the  `templatetag/contentblock_extras.py` file. Whilst it is convenient, and makes fast development, moving the query code into `view.py` may allow for more efficient querying where multiple contentblock tags are in a template.