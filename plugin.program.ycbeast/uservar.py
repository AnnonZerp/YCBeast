import os, xbmc

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = 'plugin.program.ycbeast'
ADDONTITLE     = 'YCBeast Wizard'
EXCLUDES       = [ADDON_ID , 'repository.ycbeast']
BUILDFILE      = 'http://ycrepo.info/ycbeast/repo/builds.txt'                     # Text File with build info in it.
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0                                                                        

# Dont need to edit just here for icons stored locally
HOME           = xbmc.translatePath('special://home/')
PLUGIN         = os.path.join(HOME,     'addons',    ADDON_ID)                                   
ART            = os.path.join(PLUGIN,   'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/ 
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#          ICONSETTINGS  = 'http://yctool.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONMAINT      = 'http://'
ICONBUILDS     = 'http://'
ICONCONTACT    = 'http://'
ICONTRAKT      = 'http://'
ICONSETTINGS   = 'http://'
HIDESPACERS    = 'No'                                                                    # Hide the ====== seperators 'Yes' or 'No'                           

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'white'
THEME1         = '[COLOR '+COLOR1+'][YCBeast][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'    # Primary menu items   / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'                                          # Build Names          / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'                                          # Alternate items      / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]' # Current Build Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]' # Current Theme Header / %s is the menu item and is required

# Message for Contact Page
HIDECONTACT    = 'No'                                                                    # Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing YCBeast Wizard.\n\nContact us on twitter at http://twitter.com/ForTheJest'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
AUTOUPDATE     = 'No'                                                                    # Enable Auto Update 'Yes' or 'No'
WIZARDFILE     = 'http://ycrepo.info/ycbeast/repo/builds.txt'                          # Url to wizard version
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
NOTIFICATION   = ''                                                                      # Url to notification file
ENABLE         = 'No'                                                                    # Enable Notification screen Yes or No
FONTSETTINGS   = 'Font12'                                                                # Font for Notification Window
BACKGROUND     = ''                                                                      # Background for Notification Window
#########################################################