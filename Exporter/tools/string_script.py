import tools.script_exporter as script_exporter


class StringScript:
    def __init__(self, value):
        self.value = value

    def add_line(self, v):
        self.value = script_exporter.add_line(self.value, v)

    def add_space_line(self, v):
        self.value = script_exporter.add_space_line(self.value, v)

    def add_line_end(self):
        self.add_line("end")

    def get_value(self):
        return self.value
