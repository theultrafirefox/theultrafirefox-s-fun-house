class EndDot:
    """Данный класс предназанчен для возвращения входящего предложения
    с подставленной точкой в конце.

    """
    @staticmethod
    def end_dot(sentence):
        ending_dot = '.'
        return sentence + ending_dot
    """Данный метод возвращает входное предложение с точкой в конце"""


    @staticmethod
    def print_end_dot(sentence):
        ending_dot = '.'
        print(sentence + ending_dot)
    """Данный метод печатает входное предложение с точкой в конце"""


print(EndDot.end_dot('Эту строку надо печатать вручную'))
EndDot.print_end_dot('А тут она напечатается сразу')

