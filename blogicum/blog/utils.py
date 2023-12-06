from django.http import Http404


def get_object_from_posts_or_404(sequence, **params):
    """Функция найдёт объект в последовательности
       или вызовет 404.
    """
    for item in sequence:
        # узнаём что все имена параметров которые мы ищем есть в item
        if not set(params).difference(item):
            for k in params:
                # если значение одного параметра не совпадёт
                # останавливаем цикл
                if item[k] != params[k]:
                    break
            else:
                return item
    raise Http404('Page not found.')
