import random
import string


# =========================
# EXCEPCIONES PERSONALIZADAS
# =========================

class LongitudInvalidaError(Exception):
    """Se lanza cuando la longitud es menor a 8."""
    pass


class EntradaNoNumericaError(Exception):
    """Se lanza cuando el usuario no ingresa un número."""
    pass


class ContrasenaInvalidaError(Exception):
    """Se lanza cuando la contraseña no cumple las reglas."""
    pass


# =========================
# CLASE CONTRASEÑA
# =========================

class Contrasena:
    caracteres_especiales = "¿¡?=)(/¨*+-%&$#!"

    def __init__(self, longitud):
        self.longitud = longitud
        self.contrasena = ""

    def validar_longitud(self):
        if self.longitud < 8:
            raise LongitudInvalidaError(
                "La longitud mínima debe ser de 8 caracteres."
            )

    def generar(self):
        self.validar_longitud()

        mayuscula = random.choice(string.ascii_uppercase)
        minuscula = random.choice(string.ascii_lowercase)
        numero = random.choice(string.digits)
        especial = random.choice(self.caracteres_especiales)

        caracteres_disponibles = list(
            set(
                string.ascii_letters +
                string.digits +
                self.caracteres_especiales
            )
        )

        password = [mayuscula, minuscula, numero, especial]

        while len(password) < self.longitud:
            caracter = random.choice(caracteres_disponibles)

            # Evitar caracteres repetidos
            if caracter not in password:
                password.append(caracter)

        # Mezclar aleatoriamente
        random.shuffle(password)

        self.contrasena = "".join(password)

        return self.contrasena

    def validar(self):
        password = self.contrasena

        if len(password) < 8:
            raise ContrasenaInvalidaError(
                "La contraseña tiene menos de 8 caracteres."
            )

        if len(password) != len(set(password)):
            raise ContrasenaInvalidaError(
                "La contraseña tiene caracteres repetidos."
            )

        if not any(c.isupper() for c in password):
            raise ContrasenaInvalidaError(
                "Falta una letra mayúscula."
            )

        if not any(c.islower() for c in password):
            raise ContrasenaInvalidaError(
                "Falta una letra minúscula."
            )

        if not any(c.isdigit() for c in password):
            raise ContrasenaInvalidaError(
                "Falta un número."
            )

        if not any(c in self.caracteres_especiales for c in password):
            raise ContrasenaInvalidaError(
                "Falta un carácter especial."
            )

        return True


# =========================
# CLASE COFRE
# =========================

class Cofre:

    def __init__(self, tipo, puntos):
        self.tipo = tipo
        self.puntos = puntos

    @staticmethod
    def generar_cofre_valido():
        cofres = [
            Cofre("Común", 10),
            Cofre("Raro", 25),
            Cofre("Legendario", 50)
        ]

        return random.choice(cofres)

    @staticmethod
    def cofre_maldito():
        return Cofre("Maldito", -20)


# =========================
# CLASE JUEGO
# =========================

class JuegoCazador:

    def __init__(self):
        self.puntos = 0

    def jugar(self):

        print("===================================")
        print("  JUEGO CAZADOR DE CONTRASEÑAS")
        print("===================================")

        while True:

            try:
                entrada = input(
                    "\nIngrese la longitud de la contraseña: "
                )

                if not entrada.isdigit():
                    raise EntradaNoNumericaError(
                        "Debe ingresar un número válido."
                    )

                longitud = int(entrada)

                contrasena_obj = Contrasena(longitud)

                password = contrasena_obj.generar()

                contrasena_obj.validar()

                cofre = Cofre.generar_cofre_valido()

                self.puntos += cofre.puntos

                print("\n✅ Contraseña válida generada:")
                print(password)

                print(f"\n🎁 Cofre obtenido: {cofre.tipo}")
                print(f"⭐ Puntos ganados: {cofre.puntos}")

            except (
                LongitudInvalidaError,
                EntradaNoNumericaError,
                ContrasenaInvalidaError
            ) as error:

                print(f"\n❌ Error: {error}")

                cofre = Cofre.cofre_maldito()

                self.puntos += cofre.puntos

                print(f"\n☠ Cofre obtenido: {cofre.tipo}")
                print(f"💀 Penalización: {cofre.puntos} puntos")

            finally:
                print(f"\n🏆 Puntaje acumulado: {self.puntos}")

            continuar = input(
                "\n¿Desea jugar otra ronda? (s/n): "
            ).lower()

            if continuar != "s":
                print("\nGracias por jugar.")
                print(f"Puntaje final: {self.puntos}")
                break


# =========================
# PROGRAMA PRINCIPAL
# =========================

if __name__ == "__main__":
    juego = JuegoCazador()
    juego.jugar()

