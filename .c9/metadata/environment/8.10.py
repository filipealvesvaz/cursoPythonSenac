{"filter":false,"title":"8.10.py","tooltip":"/8.10.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":32,"column":34},"action":"insert","lines":["class BombaCombustivel():","","    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):","        self.setTipoCombustivel(tipoCombustivel)","        self.setValorLitro(valorLitro)","        self.setQuantidadeCombustivel(quantidadeCombustivel)","","    def setTipoCombustivel(self, tipoCombustivel):","        self.tipoCombustivel = tipoCombustivel","","    def setValorLitro(self, valorLitro):","        self.valorLitro = float(valorLitro)","","    def setQuantidadeCombustivel(self, quantidadeCombustivel):","        self.quantidadeCombustivel = quantidadeCombustivel","","    def abastecerPorValor(self, valor):","        totalLitros = valor / self.valorLitro","        if (totalLitros <= self.quantidadeCombustivel):","            self.setQuantidadeCombustivel(","                self.quantidadeCombustivel - totalLitros)","","    def abastecerPorLitro(self, totalLitros):","        if (totalLitros <= self.quantidadeCombustivel):","            self.setQuantidadeCombustivel(","                self.quantidadeCombustivel - totalLitros)","","# Teste da classe","bomba1 = BombaCombustivel('Gasolina Aditivada', 3.03, 10000)","bomba1.abastecerPorLitro(100)","print bomba1.quantidadeCombustivel","bomba1.abastecerPorValor(100)","print bomba1.quantidadeCombustivel"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":32,"column":34},"end":{"row":32,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1597429033604,"hash":"bce325e6674d158ba968946f834c566475ebcbc4"}