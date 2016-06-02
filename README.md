# ATXGreenAtlas
ATXGreenAtlas is an environmental asset mapping platform aimed at residential and government use in Austin, Texas.

## About
ATXGreenAtlas is the application stemming from [this project](https://github.com/atxhack4change/2016-project-proposals/issues/5) at the civic hackathon ATX Hack 4 Change in Austin, Texas, on June 3rd-5th, 2016.

Here is an excerpt from the aforementioned project: 

"  Our project has been expanded to provide some more user functionality. Using the data (coordinate pairs, name) on places around Austin that qualify as either an 'Environmental Good' (parks, solar panel generation, vegan grocery stores, healthy restaurants, clean creeks and rivers, etc) and 'Environmental Negatives' (high pollution concentrations, gas spills, landfills), we will provide an interactive web-based map with layers to be toggled.  
We will also be providing a lookup function by zipcode, so after entering your zipcode, we can leverage this data and send you a customized email with the closest environmental goods and negatives to in your neighborhood.  
Once again, I'd like to highlight the intended audience for this application, also stated below. We envision this being used by perspective Austin residents to gain insight into the positive and negative aspects of their new dwellings. Our second intended audience is Austin city members and city council, whom, in accordance with Mayor Adler's Smart City proposal, need more new data and centralized analytics on environmental areas of concern in Austin.  "

## Technologies
We are leveraging [AngularJS](https://angularjs.org/) with a [LeafletJS directive](https://github.com/tombatossals/angular-leaflet-directive.git) and [NodeJS](https://nodejs.org/en/).

NodeJS is used as a web server to deliver all the static assets, like json data, html, and javascript. We also used NodeJS to parse the raw data and form it per-zipcode. 

Python was used to parse raw json datasets and create leaflet compatible objects.