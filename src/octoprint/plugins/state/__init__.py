# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class StatePlugin(octoprint.plugin.StartupPlugin,
                  octoprint.plugin.TemplatePlugin,
                  octoprint.plugin.SettingsPlugin,
                  octoprint.plugin.AssetPlugin):

 def on_after_startup(self):
     self._logger.info("Hello State")

 def get_template_configs(self):
     return [
         dict(type="tab", custom_bindings=False)
     ]

 def get_assets(self):
    return dict(
    	#css=["css/state.css"],
        js=["js/state.js"]
    )

__plugin_name__ = "State"
__plugin_implementation__ = StatePlugin()