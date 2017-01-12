# !/usr/bin/python2
# -*- coding: utf-8 -*-
SETTINGS_PRIORITY = 10

import logging, os
from pyforms.utils.package_finder import PackageFinder

MODULES = PackageFinder()

APP_LOG_FILENAME = 'pythonvideoannotator.log'
APP_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
APP_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

PYFORMS_LOG_HANDLER_FILE_LEVEL = logging.DEBUG
PYFORMS_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

VIDEO_FILE_PATH = None
CHART_FILE_PATH = None
PROJECT_PATH    = None
PROJECT_PATH    = 'project'

SAVED_GRAPH_FILE_PATH = ""
SAVED_BONSAI_FILE_PATH = ""

MAIN_WINDOW_GEOMETRY = 50, 200, 1000, 700
MAIN_WINDOW_GEOMETRY = 1700, 50, 1400, 1000


#VIDEO_FILE_PATH = '/home/ricardo/Downloads/fc2_save_2013-10-29-124117-0001.avi'
#VIDEO_FILE_PATH = 'C:/Users/swp/Downloads/fc2_save_2013-10-29-124117-0001.avi'
#CHART_FILE_PATH = '/home/ricardo/Desktop/01Apollo201403210900/01Apollo201403210900_out.csv', 0, 1

PYFORMS_STYLESHEET 			= os.path.join('pythonvideoannotator', 'resources','themes', 'default', 'stylesheet.css')
PYFORMS_STYLESHEET_LINUX 	= os.path.join('pythonvideoannotator', 'resources','themes', 'default', 'stylesheet_darwin.css')

MODULES += 'pythonvideoannotator_module_motioncounter'
#MODULES += 'pythonvideoannotator_module_eventsstats'
#MODULES += 'pythonvideoannotator_module_regionsfilter'
MODULES += 'pythonvideoannotator_module_smoothpaths'
MODULES += 'pythonvideoannotator_module_createpaths'
MODULES += 'pythonvideoannotator_module_virtualobjectgenerator'
MODULES += 'pythonvideoannotator_module_backgroundfinder'
MODULES += 'pythonvideoannotator_module_contoursimages'
MODULES += 'pythonvideoannotator_module_tracking'
MODULES += 'pythonvideoannotator_module_timeline'
MODULES += 'pythonvideoannotator_module_patheditor'