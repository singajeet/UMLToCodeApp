"""
.. module: config
"""
from configparser import ConfigParser, ExtendedInterpolation
import pathlib


################ Config variables #########################
CONFIG_FILE = 'uml_to_code.ini'
DEFAULT_SECTION = 'default'
APP_BASE_PATH_KEY = 'app_base_path'
CODE_GEN_SECTION = 'code_generator'
OUTPUT_FOLDER_PATH_KEY = 'output_folder_path'
INPUT_FOLDER_PATH_KEY = 'input_folder_path'
RESOURCES_FOLDER_PATH_KEY = 'resources_folder_path'
TEMPLATES_FOLDER_PATH_KEY = 'templates_folder_path'
OVERWRITE_FILE_KEY = 'overwrite_file'

UMLTOCODEAPP_PKG = 'UMLToCodeApp'
RESOURCES_PKG = '%s.resources' % UMLTOCODEAPP_PKG

_conf_path = pathlib.Path(__file__).parent
_conf_file = _conf_path.joinpath(CONFIG_FILE)
CONFIG_FILE = pathlib.Path(_conf_file).absolute()
_config_parser = ConfigParser(interpolation=ExtendedInterpolation())
_config_parser.read(CONFIG_FILE)

APP_BASE_PATH = _config_parser.get(DEFAULT_SECTION, APP_BASE_PATH_KEY)
OUTPUT_FOLDER_PATH = _config_parser.get(CODE_GEN_SECTION, OUTPUT_FOLDER_PATH_KEY)
OVERWRITE_FILE = _config_parser.get(CODE_GEN_SECTION, OVERWRITE_FILE_KEY)
INPUT_FOLDER_PATH = _config_parser.get(CODE_GEN_SECTION, INPUT_FOLDER_PATH_KEY)
RESOURCES_FOLDER_PATH = _config_parser.get(CODE_GEN_SECTION, RESOURCES_FOLDER_PATH_KEY)
TEMPLATES_FOLDER_PATH = _config_parser.get(CODE_GEN_SECTION, TEMPLATES_FOLDER_PATH_KEY)

############## Templates ###############################
MODULE_TEMPLATE = 'module_template.skel'
SIMPLE_CLASS_TEMPLATE = 'simple_class.skel'
SIMPLE_FUNCTION_TEMPLATE = 'simple_function.skel'
