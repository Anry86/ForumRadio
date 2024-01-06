class MyMixin(object):
    mixin_group = ''

    def get_prop(self):     # передаваемые параметры из класса миксина
        return self.mixin_group.upper()  # возвращает входные данные в верхнем регистре

    def get_upper(self, s):  # передаваемые параметры из класса миксина
        return s.upper()  # возвращает входные данные в верхнем регистре
