class TimeFinder:
    entities = []
    def __init__(self, sentence):
        self.sentence = sentence

    def get_sentence(self):
        return self.sentence

    @staticmethod
    def if_time_word_in_sentence(list_):
        if any(['вечера' in list_, 'ночи' in list_, 'утра' in list_]):
            return True
        return False

    def changer_core(self, list_, index_, is_night=False):
        if is_night:
            if int(list_[index_ - 1]) <= 12:
                list_[index_- 1] = str(int(list_[index_- 1]) + 12)
        if index_ != -1:
            list_[index_] = list_[index_ - 1] + ':' + '00'
            del list_[index_ - 1]
        return list_

    def changer(self):
        workspace = self.sentence.split()
        while TimeFinder.if_time_word_in_sentence(workspace):
            if 'утра' in workspace:
                workspace = TimeFinder.changer_core(self, workspace, workspace.index('утра'))
            if 'вечера' in workspace:
                workspace = TimeFinder.changer_core(self, workspace, workspace.index('вечера'), True)
            if 'ночи' in workspace:
                workspace = TimeFinder.changer_core(self, workspace, workspace.index('ночи'))
        self.sentence = workspace

    def checker(self):
        entities = []
        for element in self.sentence:
            clockwork = element.split(':')
            if len(clockwork) == 2:
                entities.append(element)
        self.entities = entities

    def get_entities(self):
        return self.entities

    def execution(self):
        TimeFinder.changer(self)
        TimeFinder.checker(self)


bruh = TimeFinder('Я встану в 6 утра')
bruh.execution()
print(*bruh.get_entities(), sep='\n')

print()

bruh = TimeFinder('Жду тебя в 18:20')
bruh.execution()
print(*bruh.get_entities(), sep='\n')

print()

bruh = TimeFinder('1 дня это 13:00')
bruh.execution()
print(*bruh.get_entities(), sep='\n')

print()

bruh = TimeFinder('2 брата вернулись лишь в 8 вечера')
bruh.execution()
print(*bruh.get_entities(), sep='\n')