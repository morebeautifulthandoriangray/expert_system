from experta import *
from boots_facts import boots_facts


class FSSeller(KnowledgeEngine):
    @Rule()
    def expert_q(self):
        response = input("Вы разбираетесь в фигурных коньках?")

        if response.strip() == 'yes':
            self.declare(Fact('budget_above_50000'))
        elif response.strip() == 'no':
            self.declare(Fact('budget_below_15000'))
        else:
            raise "\Неправильный ввод!"

    @Rule(Fact('budget_above_50000'))
    def budget_above_50000(self):
        response = input("Бюджет коньков может быть больше 50000?")
        if response.strip() == 'yes':
            self.declare(Fact('blade_change'))
        elif response.strip() == 'no':
            self.declare(Fact('intense_training'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('blade_change'), Fact('budget_above_50000')))
    def blade_change(self):
        response = input("Вы рассматриваете замену лезвий?")
        if response.strip() == 'yes':
            self.declare(Fact('shining'))
        elif response.strip() == 'no':
            self.declare(Fact('mirror_blade'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('shining'), Fact('blade_change')))
    def shining(self):
        response = input("Вы любите стразы?")
        if response.strip() == 'yes':
            self.declare(boots_facts[0])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: EDEA PIANO")
        elif response.strip() == 'no':
            self.declare(boots_facts[1])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: EDEA ICE FLY")
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('blade_change'), Fact('mirror_blade')))
    def mirror_blade(self):
        response = input("Вы рассматриваете у лезвий зеркальное покрытие для лучшего скольжения?")
        if response.strip() == 'yes':
            self.declare(boots_facts[2])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: RISPORT ROYAL PRIME")
        elif response.strip() == 'no':
            self.declare(Fact('blade_strength'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('blade_strength'), Fact('mirror_blade')))
    def blade_strength(self):
        response = input(
            "Вы рассматриваете коньки с упрочнением лезвий путем добавления слоя с углеродными наночастицами для большей стойкости лезвия?")
        if response.strip() == 'yes':
            self.declare(boots_facts[3])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: JACKSON FREESTYLE FUSION")
        elif response.strip() == 'no':
            self.declare(boots_facts[4])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: GRAF SPLENDID")
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('intense_training'), Fact('budget_above_50000')))
    def intense_training(self):
        response = input("У вас достаточно интенсивная нагрузка?")
        if response.strip() == 'yes':
            self.declare(Fact('more_than_30h'))
        elif response.strip() == 'no':
            self.declare(Fact('trainee'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('intense_training'), Fact('more_than_30h')))
    def more_than_30h(self):
        response = input("Вы тренируетесь больше 30 часов в неделю?")
        if response.strip() == 'yes':
            self.declare(boots_facts[5])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: JACKSON DJ")
        elif response.strip() == 'no':
            self.declare(boots_facts[6])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: EDEA CONCERTO")
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('intense_training'), Fact('trainee')))
    def trainee(self):
        response = input("Вы тренер?")
        if response.strip() == 'yes':
            self.declare(boots_facts[7])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: RIEDELL BRONZE STAR")
        elif response.strip() == 'no':
            self.declare(Fact('ice_dance'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('ice_dance'), Fact('trainee')))
    def ice_dance(self):
        response = input("Вы учавствуете в танцах на льду?")
        if response.strip() == 'yes':
            self.declare(boots_facts[8])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: RISPORT ROYAL ELITE")
        elif response.strip() == 'no':
            self.declare(boots_facts[9])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: JACKSON ELLE NEW")
        else:
            raise "\Неправильный ввод!"

    @Rule(Fact('budget_below_15000'))
    def budget_below_15000(self):
        response = input("Вы бы хотели найти коньки дешевле 15000?")

        if response.strip() == 'yes':
            self.declare(Fact('salaga'))
        elif response.strip() == 'no':
            self.declare(Fact('spins_3rd_component'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('budget_below_15000'), Fact('salaga')))
    def salaga(self):
        response = input("Вы новичок?")

        if response.strip() == 'yes':
            self.declare(Fact('jumps'))
        elif response.strip() == 'no':
            self.declare(Fact('double_jumps'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('salaga'), Fact('jumps')))
    def jumps(self):
        response = input("Вы собираетесь изучать прыжки?")

        if response.strip() == 'yes':
            self.declare(boots_facts[10])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: RUNA BASE")
        elif response.strip() == 'no':
            self.declare(Fact('step_choreography'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('step_choreography'), Fact('jumps')))
    def step_choreography(self):
        response = input("Вы собираетесь изучать дорожки?")

        if response.strip() == 'yes':
            self.declare(boots_facts[11])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: JACKSON CLASSIQUE MIRAGE")
        elif response.strip() == 'no':
            self.declare(boots_facts[12])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: MLS WHITE")
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('double_jumps'), Fact('salaga')))
    def double_jumps(self):
        response = input("Вы умеете прыгать двойные прыжки?")

        if response.strip() == 'yes':
            self.declare(boots_facts[13])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: RIEDELL 110")
        elif response.strip() == 'no':
            self.declare(boots_facts[14])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: ISG AXEL")
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('budget_below_15000'), Fact('spins_3rd_component')))
    def spins_3rd_component(self):
        response = input("Вращения идут ниже 3го уровня компонентов?")

        if response.strip() == 'yes':
            self.declare(Fact('jumps_combination'))
        elif response.strip() == 'no':
            self.declare(Fact('outdoor_ice'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('jumps_combination'), Fact('spins_3rd_component')))
    def jumps_combination(self):
        response = input("Программа состоит из комбинаций прыжков?")

        if response.strip() == 'yes':
            self.declare(Fact('jumps_combination_more_than_2'))
        elif response.strip() == 'no':
            self.declare(Fact('high_speed'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('jumps_combination'), Fact('jumps_combination_more_than_2')))
    def jumps_combination_more_than_2(self):
        response = input("Прыжков в комбинации больше 2?")

        if response.strip() == 'yes':
            self.declare(boots_facts[15])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: RISPORT RF2")
        elif response.strip() == 'no':
            self.declare(boots_facts[16])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: WIFA PRIMA SET LADIES")
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('high_speed'), Fact('jumps_combination')))
    def high_speed(self):
        response = input("У катающегося высокая скорость?")

        if response.strip() == 'yes':
            self.declare(boots_facts[17])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: EDEA MOTIVO")
        elif response.strip() == 'no':
            self.declare(boots_facts[18])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: WIFA STAR")
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('outdoor_ice'), Fact('spins_3rd_component')))
    def outdoor_ice(self):
        response = input("Вы будете кататься на уличном льду?")

        if response.strip() == 'yes':
            self.declare(boots_facts[19])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: EDEA CHORUS")
        elif response.strip() == 'no':
            self.declare(Fact('triple_jumps'))
        else:
            raise "\Неправильный ввод!"

    @Rule(AND(Fact('outdoor_ice'), Fact('triple_jumps')))
    def triple_jumps(self):
        response = input("Вы прыгаете тройные прыжки?")

        if response.strip() == 'yes':
            self.declare(boots_facts[20])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: RIEDELL OLYMPIA")
        elif response.strip() == 'no':
            self.declare(boots_facts[21])
            print("Вам рекомендуются к покупке сдедующие фигурные коньки: RISPORT ELECTRA LIGHT")
        else:
            raise "\Неправильный ввод!"


engine = FSSeller()
engine.reset()
engine.run()


print(engine.facts)
