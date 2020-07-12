# Enum to make things simpler to modify and mroe stable
class KeyNames:
    CH_DOWN = "ch_down"
    CH = "ch"
    CH_UP = "ch_up"
    PREV = "prev"
    NEXT = "next"
    PAUSE_PLAY = "pause_play"
    VOL_DOWN = "vol_down"
    VOL_UP = "vol_up"
    EQ = "eq"
    ZERO = "0"
    HUNDRED_PLUS = "100_plus"
    TWO_HUNDRED_PLUS = "200_plus"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    REPEAT = "repeat"

# That's where the magic happens. Nothing special. When you receive an IR signal
# it gets translated into a number. For convinience sake (reading big intergers
# is painful and makes it easy to make mistakes) I convert those numbers to HEX.
# Each key has one assigned value. Somehow, I can detect two (depending on
# whether I am pointing directly at the IR receiver or not).
class KeysHandler:

    def __init__(self):
        self.keysToCode = {
            KeyNames.CH_DOWN : ["FFA25D", "E318261B"],
            KeyNames.CH : ["511DBB", "FF629D"],
            KeyNames.CH_UP : ["FFE21D", "EE886D7F"],
            KeyNames.PREV : ["FF22DD", "52A3D41F"],
            KeyNames.NEXT : ["FF02FD", "D7E84B1B"],
            KeyNames.PAUSE_PLAY : ["FFC23D", "20FE4DBB"],
            KeyNames.VOL_DOWN : ["F076C13B", "FFE01F"],
            KeyNames.VOL_UP : ["FFA857", "A3C8EDDB"],
            KeyNames.EQ : ["FF906F", "E5CFBD7F"],
            KeyNames.ZERO : ["FF6897", "C101E57B"],
            KeyNames.HUNDRED_PLUS : ["FF9867", "97483BFB"],
            KeyNames.TWO_HUNDRED_PLUS : ["FFB04F", "F0C41643"],
            KeyNames.ONE : ["FF30CF", "9716BE3F"],
            KeyNames.TWO : ["FF18E7", "3D9AE3F7"],
            KeyNames.THREE : ["FF7A85", "6182021B"],
            KeyNames.FOUR : ["FF10EF", "8C22657B"],
            KeyNames.FIVE : ["FF38C7", "488F3CBB"],
            KeyNames.SIX : ["FF5AA5", "449E79F"],
            KeyNames.SEVEN : ["FF42BD", "32C6FDF7"],
            KeyNames.EIGHT : ["FF4AB5", "1BC0157B"],
            KeyNames.NINE : ["FF52AD", "3EC3FC1B"],
            KeyNames.REPEAT : ["FFFFFFFF"]
        }

        self.invalid = None
        self.last_key = None

    def getKeyFromCode(self, code):
        for key in self.keysToCode:
            if code in self.keysToCode[key]:
                return key
        return self.invalid

    def getCodeFromkey(self, key):
        return self.keysToCode[key]
