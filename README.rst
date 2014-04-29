DjangoDatabasesProject
======================
This software is only to be used as a course project in the Spring 2014 offering of CS453 at
Western Carolina University. It and any modification of it are not to be used in any other manner.
This Project is licensed under the GNU General Public License http://www.gnu.org/licenses/gpl-2.0.html

PetDispense Folder - is for all python files related to the pet dispense
------------------------------------------------------------------------
- admin.py - is were models are registered for interaction on the admin site
- models.py - determines tables and relations for the PetDispense app.
- urls.py - determines what urls will display what html.
- views.py - creates classes that display html.
- test.py - not used right now

Static Folder - is for static asset such as css, js, etc.
---------------------------------------------------------

- PetDispense - contains static css, js, etc.assets used by the app itself.

Templates folder
----------------
- contains all the html for all projects and is spilt for individual sites
- PetDispense - contains html files for the PetDispense app.
    - about.html     - give a brief over view of the project
    - agreement.html - ask if the user if they agree with the
    - contact.html   - a contact page to get in touch with app devs
    - index.html     - login screen and entry point in to the program
    - pin.html       - 
    - returns.html   - page for returning an animal
    - selection.html - determining what data you want to look at

- admin - contain html used by the admin site

- base.html - no html in this file it is just used by other html files to determine what css and js to get.

DjangoDatabasesProject folder
-----------------------------
- contains all python files that apply to the entire site i.e. settings.py

Heroku Files
------------
- Procfile - lists the process types in PetDispense

- .env - stores the environment variables of the application

- requirements.txt - tells heroku what pip packages to install

