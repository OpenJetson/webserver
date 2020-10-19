import jinja2
import os

class Templates:
    def __init__(self):
        loader = jinja2.FileSystemLoader(self.templatePath())
        self.environment = jinja2.Environment(loader=loader)

    def templatePath(self):
        return os.path.join(os.getcwd(), 'templates')

    def intrinsics(self, ZED_ENABLED):
        calibrationTemplate = self.environment.get_template('calibration.html')
        html = calibrationTemplate.render(zedenabled=ZED_ENABLED)
        template = self.environment.get_template('base.html')
        return template.render(body_html=html)

    def data(self, ZED_ENABLED):
        recordingTemplate = self.environment.get_template('recording.html')
        html = recordingTemplate.render(zedenabled=ZED_ENABLED)
        template = self.environment.get_template('base.html')
        return template.render(body_html=html)

    def documentation(self):
        docu_template = self.environment.get_template('documentation.html')
        html = docu_template.render()
        template = self.environment.get_template('base.html')
        return template.render(body_html=html)

    def ls(self, files, dirs):
        opts = {}
        opts['files'] = files
        opts['dirs'] = dirs
        ls_template = self.environment.get_template('ls.html')
        html = ls_template.render(state=opts)
        template = self.environment.get_template('base.html')
        return template.render(body_html=html)

    def index(self, message):
        template = self.environment.get_template('base.html')
        return template.render(body_html=message)

    def barcode(self):
        barcodeTemplate = self.environment.get_template('barcode.html')
        html = barcodeTemplate.render()
        template = self.environment.get_template('base.html')
        return template.render(body_html=html)
