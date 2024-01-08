def make_car(manufacturer, model, **kwargs):
    print(manufacturer, model, kwargs)


make_car(manufacturer='ceshi', model='ceshi', ceshi={'a': '1', 'b': '2'}, color='Blue')
