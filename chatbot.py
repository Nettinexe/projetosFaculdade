import random
import nltk
from nltk.chat.util import Chat, reflections

pares = [
    (r"Olá, meu nome é Victor e estou interessado em adquirir um carro|Oi, estou querendo comprar um carro|Opa, estou querendo um carro novo", ["Você tem algum carro em mente?", "Você já tem alguma escolha predefinida?"]),
    (r"Oi meu nome é Victor e queria comprar uma moto na sua loja|Olá, estou interessado em adquirir uma moto|Oi, estou querendo comprar uma moto|Opa, estou querendo uma moto nova", ["Você tem alguma moto em mente?", "Você já tem alguma escolha predefinida?"]),
    (r"meu nome é (.*)", ["Olá %1, prazer em te conhecer, sou o DriveAssist!"]),
    (r"adeus|tchau", ["Tchau! Foi bom conversar com você.", "Até mais"]),

    (r"Sim", ["Qual seria?", "Qual modelo você tem em mente?", "Qual veículo você deseja?"]),
    
    (r"Não tenho um carro em mente", ["Ok! Irei te apresentar o catálogo de carros disponíveis\nBMW MK3\nPORSCHE GT3 RS\nDOGDE DEMON\nDOGDE CHALLENGER SRT\nAUDI RS6\nMERCEDES BENZ AMGGT\nSUPRA MK3\nKOENIGSEGG JESKO\nBUGATTI CHIRON\nFERRARI LA FERRARI\nBENTLEY CONTINENTAL GT\nROLLS ROYCE PHANTOM SPORT BLACK\nLAMBORGHINI VENENO\nCAMARO EXORCIST\nMCLAREN SENNA\nMAZDA RX7\nNISSAN GTR","Ok, vou te apresentar nosso acervo de carros!\nBMW MK3\nPORSCHE GT3 RS\nDOGDE DEMON\nDOGDE CHALLENGER SRT\nAUDI RS6\nMERCEDES BENZ AMGGT\nSUPRA MK3\nKOENIGSEGG JESKO\nBUGATTI CHIRON\nFERRARI LA FERRARI\nBENTLEY CONTINENTAL GT\nROLLS ROYCE PHANTOM SPORT BLACK\nLAMBORGHINI VENENO\nCAMARO EXORCIST\nMCLAREN SENNA\nMAZDA RX7\nNISSAN GTR"]),
    
    (r"Não tenho uma moto em mente", ["Ok! Irei te apresentar o catálogo de motos disponíveis\nKAWASAKI NINJA\nYAMAHA XJ6\nDUCATI DIAVEL\nBMW S1000 RR","Ok, vou te apresentar nosso acervo de motos!\nKAWASAKI NINJA\nYAMAHA XJ6\nDUCATI DIAVEL\nBMW S1000 RR"]),
    
    (r"BMW MK3 E46", ["Ótima escolha, irei te mostrar as especificações desse carro!\nConforto e Segurança (com pegada esportiva)\nLuxo e Conforto com Performance\nBoa para Família? Não é ideal para a família, já que é um carro esportivo com apenas dois assentos traseiros. No entanto, oferece um bom equilíbrio entre desempenho e conforto.\nBoa para Passeios? Sim, é excelente para passeios em termos de prazer de condução e performance. É confortável e tem um bom porte.\nBoa para Corridas? Sim, é um carro com ótimo desempenho em pista, especialmente nas versões com foco em desempenho (como o M3 E46 e versões mais recentes).\nMotorização: 3.2L I6 (M3 E46)\nPotência: 343 cv (no M3 E46)\nAceleração (0-100 km/h): Aproximadamente 5,1 segundos\nVelocidade Máxima: 250 km/h (limitada eletronicamente)\nTransmissão: Manual de 6 marchas ou automática de 6 marchas (SMG)\nPeso: Cerca de 1.500 kg\nEssas características te agradaram?"]),
    
    (r"PORSCHE GT3 RS", ["Ótima escolha, irei te mostrar as especificações desse carro!\nEsportividade (Foco em Dirigibilidade, Estilo e Emoção)\nBoa para Família? Não. O 911 GT3 RS é uma máquina focada em performance, com pouco espaço para os passageiros traseiros e um interior minimalista.\nBoa para Passeios? Embora não seja a melhor escolha para passeios longos, é muito divertido de dirigir, sendo uma excelente opção para quem gosta de esportivos de alto desempenho.\nBoa para Corridas? Sim, é um dos melhores carros de pista e competições, especialmente devido à sua agilidade, peso leve e motor potente.\nMotorização 4.0L H6\nPotência: 520 cv (911 GT3 RS 991.2)\nAceleração (0-100 km/h): Aproximadamente 3,2 segundos\nVelocidade Máxima: 312 km/h\nTransmissão: PDK (dupla embreagem) de 7 marchas\nPeso: Cerca de 1.420 kg\nEssas características te agradaram?"]),
    
    (r"DOGDE DEMON", ["Ótima escolha, irei te mostrar as especificações desse carro!\nEsportividade (Foco em Dirigibilidade, Estilo e Emoção)\nMuscle Cars / Potência Bruta\nBoa para Família? Não é ideal para famílias, já que é um muscle car de dois lugares. No entanto, oferece bastante espaço no banco da frente.\nBoa para Passeios? Para passeios curtos ou ocasi ais, pode ser divertido, mas não é a melhor opção para longas distâncias devido ao seu consumo de combustível.\nBoa para Corridas? Sim, é um dos carros mais potentes da sua categoria, ideal para corridas em linha reta.\nMotorização: 6.2L V8 Supercharged\nPotência: 840 cv\nAceleração (0-100 km/h): Aproximadamente 2,3 segundos\nVelocidade Máxima: 270 km/h\nTransmissão: Automática de 8 marchas\nPeso: Cerca de 1.200 kg\nEssas características te agradaram?"]),
    
    (r"Dodge Challenger SRT", ["Ótima escolha, irei te mostrar as especificações desse carro!\nEsportividade (Foco em Dirigibilidade, Estilo e Emoção)\nMuscle Cars / Potência Bruta\nBoa para Família? Sim, é mais espaçoso que muitos esportivos, com capacidade para cinco passageiros.\nBoa para Passeios? Sim, é confortável para passeios longos e viagens, com um bom espaço no porta-malas.\nBoa para Corridas? Sim, é um carro potente, ideal para corridas em linha reta e competições.\nMotorização: 6.4L V8\nPotência: 485 cv\nAceleração (0-100 km/h): Aproximadamente 4,5 segundos\nVelocidade Máxima: 250 km/h\nTransmissão: Manual de 6 marchas ou automática de 8 marchas\nPeso: Cerca de 1.800 kg\nEssas características te agradaram?"]),
    
    (r"AUDI RS6", ["Ótima escolha, irei te mostrar as especificações desse carro!\nConforto e Segurança (com pegada esportiva)\nBoa para Família? Sim, é um carro familiar com bastante espaço e conforto para todos os passageiros.\nBoa para Passeios? Sim, é muito confortável e ideal para longas viagens.\nBoa para Corridas? Sim, é um carro esportivo com excelente desempenho em pista.\nMotorização: 4.0L V8 Twin-Turbo\nPotência: 591 cv\nAceleração (0-100 km/h): Aproximadamente 3,5 segundos\nVelocidade Máxima: 305 km/h (com pacote opcional)\nTransmissão: Automática de 8 marchas\nPeso: Cerca de 2.000 kg\nEssas características te agradaram?"]),
    
    (r"Mercedes-Benz AMG GT6", ["Ótima escolha, irei te mostrar as especificações desse carro!\nEsportividade (Foco em Dirigibilidade, Estilo e Emoção)\nBoa para Família? Não é ideal para famílias, já que é um carro esportivo de dois lugares.\nBoa para Passeios? Sim, é muito divertido de dirigir e oferece uma experiência de condução emocionante.\nBoa para Corridas? Sim, é um carro de alto desempenho, ideal para pista.\nMotorização: 4.0L V8 Biturbo\nPotência: 523 cv\nAceleração (0-100 km/h): Aproximadamente 3,8 segundos\nVelocidade Máxima: 310 km/h\nTransmissão: Automática de 7 marchas\nPeso: Cerca de 1.600 kg\nEssas características te agradaram?"]),
    
    (r"Toyota Supra MK4 A80", ["Ótima escolha, irei te mostrar as especificações desse carro!\nEsportividade (Foco em Dirigibilidade, Estilo e Emoção)\nBoa para Família? Não é ideal para famílias, já que é um carro esportivo de dois lugares.\nBoa para Passeios? Sim, é divertido de dirigir e oferece uma boa experiência de condução.\nBoa para Corridas? Sim, é um carro muito popular entre os entusiastas de corridas.\nMotorização: 3.0L I6 Turbo\nPotência: 276 cv\nAceleração (0-100 km/h): Aproximadamente 4,6 segundos\nVelocidade Máxima: 250 km/h (limitada eletronicamente)\nTransmissão: Manual de 6 marchas ou automática de 4 marchas\nPeso: Cerca de 1.500 kg\nEssas características te agradaram?"]),
    
    (r"KOENIGSEGG JESKO", ["Ótima escolha, irei te mostrar as especificações desse carro!\nPerformance Extrema (Foco em Velocidade e Potência)\nBoa para Família? Não, é um carro de alto desempenho com espaço limitado.\nBoa para Passeios? Não é a melhor opção para passeios, já que é focado em performance.\nBoa para Corridas? Sim, é um dos carros mais rápidos do mundo, ideal para competições e pista.\nMotorização: 5.0L V8 Twin-Turbo\nPotência: 1.600 cv\nAceleração (0-100 km/h): Aproximadamente 2,5 segundos\nVelocidade Máxima: 480 km/h (teórica)\nTransmissão: Automática de 9 marchas\nPeso: Cerca de 1.400 kg\nEssas características te agradaram?"]),
    
    (r"BUGATTI CHIRON", ["Ótima escolha, irei te mostrar as especificações desse carro!\nPerformance Extrema (Foco em Velocidade e Potência)\nBoa para Família? Sim, é um carro de luxo com espaço para quatro passageiros.\nBoa para Passeios? Sim, é extremamente confortável e ideal para longas viagens.\nBoa para Corridas? Sim, é um dos carros mais rápidos do mundo, projetado para desempenho em pista.\nMotorização: 8.0L W16 Quad-Turbo\nPotência: 1.479 cv\nAceleração (0-100 km/h): Aproximadamente 2,5 segundos\nVelocidade Máxima: 420 km/h (limitada eletronicamente)\nTransmissão: Automática de 7 marchas\nPeso: Cerca de 1.900 kg\nEssas características te agradaram?"]),
    
    (r"FERRARI LA FERRARI", ["Ótima escolha, irei te mostrar as especificações desse carro!\nPerformance Extrema (Foco em Velocidade e Potência)\nBoa para Família? Não, é um carro esportivo de dois lugares.\nBoa para Passeios? Sim, é muito divertido de dirigir e oferece uma experiência de condução emocionante.\nBoa para Corridas? Sim, é um carro de alto desempenho, ideal para pista.\nMotorização: 6.3L V12 + Motor Elétrico\nPotência: 950 cv\nAceleração (0-100 km/h): Aproximadamente 2,6 segundos\nVelocidade Máxima: 352 km/h\nTransmissão: Automática de 7 marchas\nPeso: Cerca de 1.600 kg\nEssas características te agradaram?"]),
    
    (r"BENTLEY CONTINENTAL GT", ["Ótima escolha, irei te mostrar as especificações desse carro!\nLuxo e Conforto com Performance\nBoa para Família? Sim, é um carro espaçoso e confortável, ideal para longas viagens.\nBoa para Passeios? Sim, é extremamente confortável e luxuoso, perfeito para passeios.\nBoa para Corridas? Sim, embora não seja um carro de pista, tem um bom desempenho em estrada.\nMotorização: 6.0L W12 Twin-Turbo\nPotência: 626 cv\nAceleração (0-100 km/h): Aproximadamente 3,7 segundos\nVelocidade Máxima: 333 km/h\nTransmissão: Automática de 8 marchas\nPeso: Cerca de 2.300 kg\nEssas características te agradaram?"]),
    
    (r"ROLLS ROYCE PHANTOM SPORT BLACK", ["Ótima escolha, irei te mostrar as especificações desse carro!\nLuxo e Conforto com Performance\nBoa para Família? Sim, é um carro muito espaçoso e confortável, ideal para famílias.\nBoa para Passeios? Sim, é extremamente confortável e luxuoso, perfeito para passeios.\nBoa para Corridas? Não é o foco, mas tem um bom desempenho para um carro desse porte.\nMotorização: 6.75L V12\nPotência: 563 cv\nAceleração (0-100 km/h): Aproximadamente 5,3 segundos\nVelocidade Máxima: 250 km/h (limitada eletronicamente)\nTransmissão: Automática de 8 marchas\nPeso: Cerca de 2.500 kg\nEssas características te agradaram?"]),
    
    (r"LAMBORGHINI VENENO", ["Ótima escolha, irei te mostrar as especificações desse carro!\nPerformance Extrema (Foco em Velocidade e Potência)\nBoa para Família? Não, é um carro esportivo de dois lugares.\nBoa para Passeios? Não é a melhor opção para passeios, já que é focado em performance.\nBoa para Corridas? Sim, é um dos carros mais rápidos do mundo, ideal para competições e pista.\nMotorização: 6.5L V12\nPotência: 740 cv\nAceleração (0-100 km/h): Aproximadamente 2,8 segundos\nVelocidade Máxima: 355 km/h\nTransmissão: Automática de 7 marchas\nPeso: Cerca de 1.500 kg\nEssas características te agradaram?"]),
    
    (r"MCLAREN SENNA", ["Ótima escolha, irei te mostrar as especificações desse carro!\nPerformance Extrema (Foco em Velocidade e Potência)\nBoa para Família? Não, é um carro de alto desempenho com espaço limitado.\nBoa para Passeios? Não é a melhor opção para passeios, já que é focado em performance.\nBoa para Corridas? Sim, é um dos carros mais rápidos do mundo, ideal para competições e pista.\nMotorização: 4.0L V8 Twin-Turbo\nPotência: 800 cv\nAceleração (0-100 km/h): Aproximadamente 2,8 segundos\nVelocidade Máxima: 208 mph (335 km/h)\nTransmissão: Automática de 7 marchas\nPeso: Cerca de 1.198 kg\nEssas características te agradaram?"]),
    
    (r"MAZDA RX7", ["Ótima escolha, irei te mostrar as especificações desse carro!\nEsportividade (Foco em Dirigibilidade, Estilo e Emoção)\nBoa para Família? Não é ideal para famílias, já que é um carro esportivo de dois lugares.\nBoa para Passeios? Sim, é divertido de dirigir e oferece uma boa experiência de condução.\nBoa para Corridas? Sim, é um carro muito popular entre os entusiastas de corridas.\nMotorização: 1.3L Wankel\nPotência: 276 cv\nAceleração (0-100 km/h): Aproximadamente 5,9 segundos\nVelocidade Máxima: 250 km/h (limitada eletronicamente)\nTransmissão: Manual de 5 marchas ou automática de 4 marchas\nPeso: Cerca de 1.200 kg\nEssas características te agradaram?"]),
    
    (r"NISSAN GTR", ["Ótima escolha, irei te mostrar as especificações desse carro!\nEsportividade (Foco em Dirigibilidade, Estilo e Emoção)\nBoa para Família? Sim, é um carro esportivo com espaço para quatro passageiros.\nBoa para Passeios? Sim, é confortável para passeios longos e viagens, com um bom espaço no porta-malas.\nBoa para Corridas? Sim, é um carro potente, ideal para corridas em pista.\nMotorização: 3.8L V6 Twin-Turbo\nPotência: 565 cv\nAceleração (0-100 km/h): Aproximadamente 3,2 segundos\nVelocidade Máxima: 315 km/h\nTransmissão: Automática de 6 marchas\nPeso: Cerca de 1.700 kg\nEssas características te agradaram?"]),
    
    (r"CHEVROLET CAMARO EXORCIST", ["Ótima escolha, irei te mostrar as especificações desse carro!\nMuscle Cars / Potência Bruta\nBoa para Família? Não é ideal para famílias, já que é um muscle car de dois lugares. No entanto, oferece bastante espaço no banco da frente.\nBoa para Passeios? Para passeios curtos ou ocasi ais, pode ser divertido, mas não é a melhor opção para longas distâncias devido ao seu consumo de combustível.\nBoa para Corridas? Sim, é um dos carros mais potentes da sua categoria, ideal para corridas em linha reta.\nMotorização: 6.2L V8 Supercharged\nPotência: 1.000 cv\nAceleração (0-100 km/h): Aproximadamente 3,5 segundos\nVelocidade Máxima: 320 km/h\nTransmissão: Automática de 10 marchas\nPeso: Cerca de 1.500 kg\nEssas características te agradaram?"]),
    
    (r"KAWASAKI NINJA", ["Ótima escolha, irei te mostrar as especificações dessa moto!\nPerformance Extrema (foco em velocidade, aceleração e potência bruta)\nBoa para Família? Não é ideal para famílias, já que é uma moto esportiva de dois lugares.\nBoa para Passeios? Sim, é divertida de dirigir e oferece uma boa experiência de condução.\nBoa para Corridas? Sim, é uma moto muito popular entre os entusiastas de corridas.\nMotorização: 998cc\nPotência: 200 cv\nAceleração (0-100 km/h): Aproximadamente 3,0 segundos\nVelocidade Máxima: 300 km/h\nTransmissão: Manual de 6 marchas\nPeso: Cerca de 210 kg\nEssas características te agradaram?"]),
    
    (r"YAMAHA XJ6", ["Ótima escolha, irei te mostrar as especificações dessa moto!\nConforto (posição de pilotagem e uso em cidade/viagens)\nBoa para Família? Sim, é uma moto mais confortável para passeios e viagens.\nBoa para Passeios? Sim, é ideal para longas distâncias e oferece uma boa posição de pilotagem.\nBoa para Corridas? Não é a melhor opção para corridas, mas é divertida para pilotar em estradas.\nMotorização: 600cc\nPotência: 78 cv\nAceleração (0-100 km/h): Aproximadamente 3,5 segundos\nVelocidade Máxima: 220 km/h\nTransmissão: Manual de 6 marchas\nPeso: Cerca de 210 kg\nEssas características te agradaram?"]),
    
    (r"DUCATI DIAVEL", ["Ótima escolha, irei te mostrar as especificações dessa moto!\nConforto (posição de pilotagem e uso em cidade/viagens)\nBoa para Família? Não é ideal para famílias, já que é uma moto esportiva de dois lugares.\nBoa para Passeios? Sim, é muito confortável para passeios e viagens curtas.\nBoa para Corridas? Sim, é uma moto potente e ágil, ideal para pilotagem esportiva.\nMotorização: 1262cc\nPotência: 162 cv\nAceleração (0-100 km/h): Aproximadamente 3,2 segundos\nVelocidade Máxima: 270 km/h\nTransmissão: Manual de 6 marchas\nPeso: Cerca de 220 kg\nEssas características te agradaram?"]),
    
    (r"BMW S1000 RR", ["Ótima escolha, irei te mostrar as especificações dessa moto!\nSegurança e Controle (eletrônica embarcada e estabilidade)\nBoa para Família? Não, é uma moto esportiva de dois lugares.\nBoa para Passeios? Não é a melhor opção para passeios longos, mas é divertida para pilotar em estradas.\nBoa para Corridas? Sim, é uma das melhores motos de corrida do mercado, ideal para pista.\nMotorização: 999cc\nPotência: 205 cv\nAceleração (0-100 km/h): Aproximadamente 3,1 segundos\nVelocidade Máxima: 303 km/h\nTransmissão: Manual de 6 marchas\nPeso: Cerca de 197 kg\nEssas características te agradaram?"]),
    
    (r"Essas características me agradaram", ["Ótimo! Vamos dar início ao processo de compra!\nVocê deseja obter o nosso plano especial de garantia e segurança?\nNosso plano fornece para você 3 anos de garantia por nossa conta!\nAlém disso, você ganhará desconto de 40 porcento em qualquer seguradora brasileira durante 5 anos!"]),
    (r"Desejo obter o plano especial de garantia e segurança", ["Ótimo! Vamos para a próxima seção!\nVocê deseja adquirir o nosso plano de experiência premium?\nAtravés desse plano nós oferecemos entrega à domicílio VIP!\nTambém oferecemos a primeira revisão do veículo grátis!\nAlém disso, o plano te oferece uma consultoria de estilo(combinação de roupas, acessórios e veículo"]),
    (r"Não desejo o plano especial de garantia e segurança", ["Ok! Vamos para a próxima seção!\nVocê deseja adquirir o nosso plano de experiência premium?\nAtravés desse plano nós oferecemos entrega à domicílio VIP!\nTambém oferecemos a primeira revisão do veículo grátis!\nAlém disso, o plano te oferece uma consultoria de estilo(combinação de roupas, acessórios e veículo"]),
    (r"Desejo obter o plano de experiência premium",["Ok! Vamos para a próxima seção!\nVocê deseja adquirir o nosso plano de Facilidades financeiras?\nEsse plano oferece à você um financiamento especial do veículo!\nAlém disso, oferecemos através desse plano a opção da troca do seu usado, mediante revisão prévia!\nE também oferecemos o pagamento facilitado através de criptomoedas!"]),
    (r"Negativo para o plano de experiência premium",["Ok! Vamos para a próxima seção!\nVocê deseja adquirir o nosso plano de Facilidades financeiras?\nEsse plano oferece à você um financiamento especial do veículo!\nAlém disso, oferecemos através desse plano a opção da troca do seu usado, mediante revisão prévia!\nE também oferecemos o pagamento facilitado através de criptomoedas!"]),
    (r"Desejo obter o plano de Facilidades financeiras", ["Ótimo! Vou encaminhar você para um atendente da nossa loja e ele dará seguimento a sua compra! Muito obrigado pela preferência!"]),
    (r"Eu não desejo o plano de Facilidades financeiras", ["Ok! Vou encaminhar você para um atendente da nossa loja e ele dará seguimento a sua compra! Muito obrigado pela preferência!"]),
    (r"As características desse carro não me agradaram", ["Que pena, você deseja visualizar outro carro?"]),
    
    (r"Sim, desejo olhar outro carro", ["Ok, vou te apresentar o catálogo de carros\nBMW MK3\nPORSCHE GT3 RS\nDOGDE DEMON\nDOGDE CHALLENGER SRT\nAUDI RS6\nMERCEDES BENZ AMGGT\nSUPRA MK3\nKOENIGSEGG JESKO\nBUGATTI CHIRON\nFERRARI LA FERRARI\nBENTLEY CONTINENTAL GT\nROLLS ROYCE PHANTOM SPORT BLACK\nLAMBORGHINI VENENO\nCAMARO EXORCIST\nMCLAREN SENNA\nMAZDA RX7\nNISSAN GTR"]),
    
    (r"Não desejo visualizar outro carro", ["Que pena, você tem interesse em alguma moto?"]),
    
    (r"As características dessa moto não me agradaram", ["Que pena, você deseja visualizar outra moto?"]),
    
    (r"Sim, desejo olhar outra moto", ["Ok, vou te apresentar o catálogo de motos\nKAWASAKI NINJA\nYAMAHA XJ6\nDUCATI DIAVEL\nBMW S1000 RR"]),
    
    (r"Não desejo visualizar outra moto", ["Que pena, você tem interesse em algum carro?"]),
    
    (r"Não encontrei o carro que eu desejo", ["Que pena, você tem interesse em alguma moto?"]),
    
    (r"Não encontrei a moto que eu desejo", ["Que pena, você tem interesse em algum carro?"]),
    
    (r"Tenho interesse em comprar uma moto", ["Ótimo, vou te apresentar o catálogo de motos disponíveis!\nKAWASAKI NINJA\nYAMAHA XJ6\nDUCATI DIAVEL\nBMW S1000 RR"]),
    
    (r"Nenhuma moto me interessou no catálogo", ["Ok! Vou encerrar esse diálogo, assim que novos veículos ficarem disponíveis no nosso catálogo você receberá uma notificação através desse contato! Obrigado pela preferência!"]),
    
    (r"Tenho interesse em comprar um carro", ["Ótimo, vou te apresentar o catálogo de carros disponíveis!\nBMW MK3\nPORSCHE GT3 RS\nDOGDE DEMON\nDOGDE CHALLENGER SRT\nAUDI RS6\nMERCEDES BENZ AMGGT\nSUPRA MK3\nKOENIGSEGG JESKO\nBUGATTI CHIRON\nFERRARI LA FERRARI\nBENTLEY CONTINENTAL GT\nROLLS ROYCE PHANTOM SPORT BLACK\nLAMBORGHINI VENENO\nCAMARO EXORCIST\nMCLAREN SENNA\nMAZDA RX7\nNISSAN GTR"]),
    
    (r"Nenhum carro me interessou no catálogo", ["Ok! Vou encerrar esse diálogo, assim que novos veículos ficarem disponíveis no nosso catálogo você receberá uma notificação através desse contato! Obrigado pela preferência!"]),
    
    (r"Não tenho interesse em comprar uma moto", ["Ok! Vou encerrar esse diálogo, assim que novos veículos ficarem disponíveis no nosso catálogo você receberá uma notificação através desse contato! Obrigado pela preferência!"]),
]
reflections = {
    "eu":"você",
    "meu":"você",
    "meus":"seus",
    "minha":"sua",
    "sou":"é",
    "estou":"está",
    "fui":"foi",
    "era":"era",
    "você":"eu",
    "você é":"eu sou",
    "você está":"eu estou",
}
chatbot = Chat(pares)

garantia_seguranca = "i"
experiencia_premium = "a"
facilidades_financeiras = "t"
chatbot = Chat(pares, reflections)
def iniciar_chat():
    print("Olá! Eu sou o DriveAssist, o Assistente Virtual da Loja KingMotors\nComo posso ajudar você hoje?")
    while True:
        entrada = input("Você: ")
        if entrada.lower() == "sair":
            print("DriveAssist:Até logo!")
            break
        resposta = chatbot.respond(entrada)
        print("DriveAssist:", resposta)
        

iniciar_chat()