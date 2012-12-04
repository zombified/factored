from pyramid.renderers import render
from factored import TEMPLATE_CUSTOMIZATIONS
import os
from pyramid.path import package_path


def registerTemplateCustomizations(config, _dir, package):
    registry = config.registry
    if TEMPLATE_CUSTOMIZATIONS not in registry:
        registry[TEMPLATE_CUSTOMIZATIONS] = {}
    path = os.path.join(
        package_path(package), _dir)
    for fi in os.listdir(path):
        registry[TEMPLATE_CUSTOMIZATIONS][fi] = (package,
            os.path.join(_dir, fi))


class TemplateRendererFactory(object):

    def __init__(self, req, context):
        self.context = context
        self.req = req
        self.customizations = req.registry[TEMPLATE_CUSTOMIZATIONS]

    def render(self, tmpl):
        try:
            package = None
            tmpl_name = os.path.basename(tmpl)
            if tmpl_name in self.customizations:
                package, tmpl = self.customizations[tmpl_name]
            return render(tmpl, self.context, request=self.req, package=package)
        except ValueError:
            return ''
