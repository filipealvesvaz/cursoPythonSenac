{"filter":false,"title":"forca.py","tooltip":"/forca.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":32,"column":34},"action":"remove","lines":["class BombaCombustivel():","","    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):","        self.setTipoCombustivel(tipoCombustivel)","        self.setValorLitro(valorLitro)","        self.setQuantidadeCombustivel(quantidadeCombustivel)","","    def setTipoCombustivel(self, tipoCombustivel):","        self.tipoCombustivel = tipoCombustivel","","    def setValorLitro(self, valorLitro):","        self.valorLitro = float(valorLitro)","","    def setQuantidadeCombustivel(self, quantidadeCombustivel):","        self.quantidadeCombustivel = quantidadeCombustivel","","    def abastecerPorValor(self, valor):","        totalLitros = valor / self.valorLitro","        if (totalLitros <= self.quantidadeCombustivel):","            self.setQuantidadeCombustivel(","                self.quantidadeCombustivel - totalLitros)","","    def abastecerPorLitro(self, totalLitros):","        if (totalLitros <= self.quantidadeCombustivel):","            self.setQuantidadeCombustivel(","                self.quantidadeCombustivel - totalLitros)","","# Teste da classe","bomba1 = BombaCombustivel('Gasolina Aditivada', 3.03, 10000)","bomba1.abastecerPorLitro(100)","print bomba1.quantidadeCombustivel","bomba1.abastecerPorValor(100)","print bomba1.quantidadeCombustivel"],"id":2},{"start":{"row":0,"column":0},"end":{"row":44,"column":13},"action":"insert","lines":["palavra = input(\"Digite a palavra secreta:\").lower().strip()","for x in range(100):","    print()","digitadas = []","acertos = []","erros = 0","while True:","    senha = \"\"","    for letra in palavra:","        senha += letra if letra in acertos else \".\"","    print(senha)","    if senha == palavra:","        print(\"Você acertou!\")","        break","    tentativa = input(\"\\nDigite uma letra:\").lower().strip()","    if tentativa in digitadas:","        print(\"Você já tentou esta letra!\")","        continue","    else:","        digitadas += tentativa","        if tentativa in palavra:","            acertos += tentativa","        else:","            erros += 1","            print(\"Você errou!\")","    print(\"X==:==\\nX  :   \")","    print(\"X  O   \" if erros >= 1 else \"X\")","    linha2 = \"\"","    if erros == 2:","        linha2 = \"  |   \"","    elif erros == 3:","        linha2 = \" \\|   \"","    elif erros >= 4:","        linha2 = \" \\|/ \"","    print(\"X%s\" % linha2)","    linha3 = \"\"","    if erros == 5:","        linha3 += \" /     \"","    elif erros >= 6:","        linha3 += \" / \\ \"","    print(\"X%s\" % linha3)","    print(\"X\\n===========\")","    if erros == 6:","        print(\"Enforcado!\")","        break"]}]]},"ace":{"folds":[],"scrolltop":240,"scrollleft":0,"selection":{"start":{"row":24,"column":32},"end":{"row":24,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":16,"state":"start","mode":"ace/mode/python"}},"timestamp":1597952230635,"hash":"e46f29992ce48ead98fa9bb3b794a7f17742b20e"}