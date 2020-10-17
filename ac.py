class RadioRelogio:
    def __init__(self):
        self.__hora = 0
        self.__minuto = 0
        self.__frequencia_am = 530
        self.__frequencia_fm =  879
        self.__banda = 'FM'

    def get_hora(self):
        return self.__hora

    def get_minuto(self):
        return self.__minuto

    def get_frequencia(self):
        if self.__banda == 'AM':
            return self.__frequencia_am
        else:
            return self.__frequencia_fm

    def get_banda(self):
        return self.__banda

    def set_hora(self, hora):
        if hora < 0 or hora > 23:
            self.__hora = 0
        else:
            self.__hora = hora

    def set_minuto(self, minuto):
        if minuto < 0 or minuto > 59:
            self.__minuto = 0
        else:
            self.__minuto = minuto

    def set_banda(self, banda):
        if banda == 'AM':
            self.__banda = banda
        elif banda == 'FM':
            self.__banda = banda
        else:
            self.__banda = 'AM'

    def tick(self):
        if self.__minuto == 59:
            self.__minuto = 0
            if self.__hora == 23:
                self.__hora = 0
            else:
                self.__hora += 1
        else:
            self.__minuto += 1

    def aumentar_frequencia(self):
        if self.__banda == 'AM':
            self.__frequencia_am += 10
            if self.__frequencia_am > 1700:
                self.__frequencia_am = 530
        else:
            self.__frequencia_fm += 2
            if self.__frequencia_fm > 1079:
                self.__frequencia_fm = 879
        return

    def diminuir_frequencia(self):
        if self.__banda == 'AM':
            self.__frequencia_am -= 10
            if self.__frequencia_am < 530:
                self.__frequencia_am = 1700
        else:
            self.__frequencia_fm -= 2
            if self.__frequencia_fm < 879:
                self.__frequencia_fm = 1079
        return
