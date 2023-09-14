# Este programa tem o intuito de:
# - Solicitar ao usuário se o resistor é de 4, 5 ou 6 Bandas (OK)
# - Receber as cores dos resistores, e em seguida calcular suas resistências (OK)

# Adicionais a serem colocados / Aprimorados
# - Tentar reduzir o codigo mais ainda
# - Informar as cores escolhidas ao usuario

# Variaveis de controle
Max_Band = int(0)
V_min = int(0)
V_max = int(9)
V_min2 = int(0)
V_max2 = int(11)

n1 = '1'
n2 = '2'
n3 = '3'

# Variaveis de texto
txt_1 = 'Digite o numero que representa a cor da Faixa'
txt_2 = 'Digite o numero que representa a cor do Multiplicador:'
txt_3 = 'Digite o numero que representa a cor da Tolerância:'
txt_4 = 'Digite o numero que representa a cor da Temperatura:'
txt_E = 'Valores invalidos, utilizar valores entre'
txt_F3 = 'O valor total em Ohms sem contar com a variação de tolerancia é'
tabela = str('''+--+--------+-------------------+----------------------------+
| N|  Cor   | Cor da Tolerância | Coeficiente de Temperatura |
+--+--------+-------------------+----------------------------+
| 0|Preto   |                   |                            |
| 1|Marrom  |       +-    1%    |          100 PPM/C         |          
| 2|Vermelho|       +-    2%    |           50 PPM/C         |
| 3|Laranja |                   |           15 PPM/C         |
| 4|Amarelo |                   |           25 PPM/C         |
| 5|Verde   |       +-  0,5%    |                            |
| 6|Azul    |       +- 0,25%    |           10 PPM/C         |
| 7|Roxo    |       +-  0,1%    |            5 PPM/C         |
| 8|Cinza   |       +- 0,05%    |                            |
| 9|Branco  |                   |                            |
|10|Dourado |       +-    5%    |                            |
|11|Prata   |       +-   10%    |                            |
|12|Sem cor |                   |                            |
+--+--------+-------------------+----------------------------+''')

# Variavel Unitaria

Black_U = int(0)
Brown_U = int(1)
Red_U = int(2)
Orange_U = int(3)
Yellow_U = int(4)
Green_U = int(5)
Blue_U = int(6)
Purple_U = int(7)
Gray_U = int(8)
White_U = int(9)

# Variavel Decimal

Black_D = int(00)
Brown_D = int(10)
Red_D = int(20)
Orange_D = int(30)
Yellow_D = int(40)
Green_D = int(50)
Blue_D = int(60)
Purple_D = int(70)
Gray_D = int(80)
White_D = int(90)

# Variavel Cemtena

Black_C = int(000)
Brown_C = int(100)
Red_C = int(200)
Orange_C = int(300)
Yellow_C = int(400)
Green_C = int(500)
Blue_C = int(600)
Purple_C = int(700)
Gray_C = int(800)
White_C = int(900)

# Variaveis de multiplicador
Black_Mul = 10 ** 0
Brown_Mul = 10 ** 1
Red_Mul = 10 ** 2
Orange_Mul = 10 ** 3
Yellow_Mul = 10 ** 4
Green_Mul = 10 ** 5
Blue_Mul = 10 ** 6
Purple_Mul = 10 ** 7
Gray_Mul = 10 ** 8
White_Mul = 10 ** 9
Gold_Mul = 10 ** -1
Silver_Mul = 10 ** -2

# Variaveis de Tolerância
Brown_T = float(0.01)
Red_T = float(0.02)
Green_T = float(0.05)
Blue_T = float(0.025)
Purple_T = float(0.01)
Gray_T = float(0.005)
Gold_T = float(0.05)
Silver_T = float(0.10)
No_Color = float(0.20)

# Variaveis de Temperatura
Brown_TP = str('100 PPM/C')
Red_TP = str('50 PPM/C')
Orange_TP = str('15 PPM/C')
Yellow_TP = str('25 PPM/C')
Blue_TP = str('10 PPM/C')
Purple_TP = str('5 PPM/C')

# Variaveis de cor (A implementar)
#Color_1 = 0
#Color_2 = 0
#Color_3 = 0
#Color_4 = 0
#Color_5 = 0
#Color_6 = 0



while (Max_Band != 3) or (Max_Band != 4) or (Max_Band != 5) or (Max_Band != 6):
    Max_Band = int(input('Digite o valor de faixas presentes no resistor:')) 

    # Caso tenha 3 faixas
    if Max_Band == 3:

        txt_3_1 = txt_1,':',n1
        txt_3_2 = txt_1,':',n2
        
        print(tabela)
        D = int(input(txt_3_1))
        U = int(input(txt_3_2))
   
        if (D or U >= V_min) and (D or U <= V_max):

            mult = int(input(txt_2))

            match mult:
                case 0:
                    mult_f = Black_Mul
                case 1:
                    mult_f = Brown_Mul
                case 2:
                    mult_f = Red_Mul
                case 3:
                    mult_f = Orange_Mul 
                case 4:
                    mult_f = Yellow_Mul
                case 5:
                    mult_f = Green_Mul
                case 6:
                    mult_f = Blue_Mul
                case 7:
                    mult_f = Purple_Mul
                case 8:
                    mult_f = Gray_Mul
                case 9:
                    mult_f = White_Mul
                case 10:
                    mult_f = Gold_Mul
                case 11:
                    mult_f = Silver_Mul
                case _:
                    print('Valor de multiplicador invalido! Finalizando programa')
                    exit()

            if (D or U >= V_min2) and (D or U <= V_max2):

                match D:
                    case 0:
                        DF = Black_D
                    case 1:
                        DF = Brown_D
                    case 2:
                        DF = Red_D
                    case 3:
                        DF = Orange_D
                    case 4:
                        DF = Yellow_D
                    case 5:
                        DF = Green_D
                    case 6:
                        DF = Blue_D
                    case 7:
                        DF = Purple_D
                    case 8:
                        DF = Gray_D
                    case 9:
                        DF = White_D

                match U:
                    case 0:
                        UF = Black_U
                    case 1:
                        UF = Brown_U
                    case 2:
                        UF = Red_U
                    case 3:
                        UF = Orange_U
                    case 4:
                        UF = Yellow_U
                    case 5:
                        UF = Green_U
                    case 6:
                        UF = Blue_U
                    case 7:
                        UF = Purple_U
                    case 8:
                        UF = Gray_U
                    case 9:
                        UF = White_U

                Res_value = float((DF + UF) * mult_f)
                Tol_fn = float(Res_value - (Res_value * No_Color))
                Tol_fp = float(Res_value + (Res_value * No_Color))

                print(txt_F3, Res_value, 'e com tolerancia o valor é', Tol_fn, 'a', Tol_fp)
                exit()
            else:
                print(txt_E, V_min2, 'a', V_max2)
   
        else:
            print(txt_E, V_min, 'a', V_max )

    # Caso tenha 4 faixas
    elif Max_Band == 4:

        txt_3_1 = txt_1,':',n1
        txt_3_2 = txt_1,':',n2
        
        print(tabela)
        D = int(input(txt_3_1))
        U = int(input(txt_3_2))
        
   
        if (D or U >= V_min) and (D or U <= V_max):

            mult = int(input(txt_2))

            match mult:
                case 0:
                    mult_f = Black_Mul
                case 1:
                    mult_f = Brown_Mul
                case 2:
                    mult_f = Red_Mul
                case 3:
                    mult_f = Orange_Mul 
                case 4:
                    mult_f = Yellow_Mul
                case 5:
                    mult_f = Green_Mul
                case 6:
                    mult_f = Blue_Mul
                case 7:
                    mult_f = Purple_Mul
                case 8:
                    mult_f = Gray_Mul
                case 9:
                    mult_f = White_Mul
                case 10:
                    mult_f = Gold_Mul
                case 11:
                    mult_f = Silver_Mul
                case _:
                    print('Valor de multiplicador invalido! Finalizando programa')
                    exit()

            T = int(input(txt_3))

            match T:
                case 1:
                    T_f = Brown_T
                case 2:
                    T_f = Red_T
                case 5:
                    T_f = Green_T
                case 6:
                    T_f = Blue_T
                case 7:
                    T_f = Purple_T
                case 8:
                    T_f = Gray_T
                case 10:
                    T_f = Gold_T
                case 11:
                    T_f = Silver_T
                case _:
                    print('Valor de Tolerância invalido! Finalizando programa')
                    exit()

            if (D or U >= V_min2) and (D or U <= V_max2):

                match D:
                    case 0:
                        DF = Black_D
                    case 1:
                        DF = Brown_D
                    case 2:
                        DF = Red_D
                    case 3:
                        DF = Orange_D
                    case 4:
                        DF = Yellow_D
                    case 5:
                        DF = Green_D
                    case 6:
                        DF = Blue_D
                    case 7:
                        DF = Purple_D
                    case 8:
                        DF = Gray_D
                    case 9:
                        DF = White_D

                match U:
                    case 0:
                        UF = Black_U
                    case 1:
                        UF = Brown_U
                    case 2:
                        UF = Red_U
                    case 3:
                        UF = Orange_U
                    case 4:
                        UF = Yellow_U
                    case 5:
                        UF = Green_U
                    case 6:
                        UF = Blue_U
                    case 7:
                        UF = Purple_U
                    case 8:
                        UF = Gray_U
                    case 9:
                        UF = White_U

                Res_value = float((DF + UF) * mult_f)
                Tol_fn = float(Res_value - (Res_value * T_f))
                Tol_fp = float(Res_value + (Res_value * T_f))

                print(txt_F3, Res_value, 'e com tolerancia o valor é', Tol_fn, 'a', Tol_fp)
                exit()
            else:
                print(txt_E, V_min2, 'a', V_max2)
   
        else:
            print(txt_E, V_min, 'a', V_max )

    # Caso tenha 5 faixas
    elif Max_Band == 5:

        txt_3_1 = txt_1,':',n1
        txt_3_2 = txt_1,':',n2
        txt_3_3 = txt_1,':',n3
        
        print(tabela)
        C = int(input(txt_3_1))
        D = int(input(txt_3_2))
        U = int(input(txt_3_3))
   
        if (C or D or U >= V_min) and (C or D or U <= V_max):

            mult = int(input(txt_2))

            match mult:
                case 0:
                    mult_f = Black_Mul
                case 1:
                    mult_f = Brown_Mul
                case 2:
                    mult_f = Red_Mul
                case 3:
                    mult_f = Orange_Mul 
                case 4:
                    mult_f = Yellow_Mul
                case 5:
                    mult_f = Green_Mul
                case 6:
                    mult_f = Blue_Mul
                case 7:
                    mult_f = Purple_Mul
                case 8:
                    mult_f = Gray_Mul
                case 9:
                    mult_f = White_Mul
                case 10:
                    mult_f = Gold_Mul
                case 11:
                    mult_f = Silver_Mul
                case _:
                    print('Valor de multiplicador invalido! Finalizando programa')
                    exit()
            
            T = int(input(txt_3))

            match T:
                case 1:
                    T_f = Brown_T
                case 2:
                    T_f = Red_T
                case 5:
                    T_f = Green_T
                case 6:
                    T_f = Blue_T
                case 7:
                    T_f = Purple_T
                case 8:
                    T_f = Gray_T
                case 10:
                    T_f = Gold_T
                case 11:
                    T_f = Silver_T
                case _:
                    print('Valor de Tolerância invalido! Finalizando programa')
                    exit()

            if (C or D or U >= V_min2) and (C or D or U <= V_max2):

                match C:
                    case 0:
                        CF = Black_C
                    case 1:
                        CF = Brown_C
                    case 2:
                        CF = Red_C
                    case 3:
                        CF = Orange_C
                    case 4:
                        CF = Yellow_C
                    case 5:
                        CF = Green_C
                    case 6:
                        CF = Blue_C
                    case 7:
                        CF = Purple_C
                    case 8:
                        CF = Gray_C
                    case 9:
                        CF = White_C

                match D:
                    case 0:
                        DF = Black_D
                    case 1:
                        DF = Brown_D
                    case 2:
                        DF = Red_D
                    case 3:
                        DF = Orange_D
                    case 4:
                        DF = Yellow_D
                    case 5:
                        DF = Green_D
                    case 6:
                        DF = Blue_D
                    case 7:
                        DF = Purple_D
                    case 8:
                        DF = Gray_D
                    case 9:
                        DF = White_D

                match U:
                    case 0:
                        UF = Black_U
                    case 1:
                        UF = Brown_U
                    case 2:
                        UF = Red_U
                    case 3:
                        UF = Orange_U
                    case 4:
                        UF = Yellow_U
                    case 5:
                        UF = Green_U
                    case 6:
                        UF = Blue_U
                    case 7:
                        UF = Purple_U
                    case 8:
                        UF = Gray_U
                    case 9:
                        UF = White_U

                Res_value = float((CF + DF + UF) * mult_f)
                Tol_fn = float(Res_value - (Res_value * T_f))
                Tol_fp = float(Res_value + (Res_value * T_f))
                
                print(txt_F3, Res_value, 'e com tolerancia o valor é', Tol_fn, 'a', Tol_fp)
                exit()
            else:
                print(txt_E, V_min2, 'a', V_max2)
        else:
            print(txt_E, V_min, 'a', V_max )        

    # Caso tenha 6 faixas
    elif Max_Band == 6:

        txt_3_1 = txt_1,':',n1
        txt_3_2 = txt_1,':',n2
        txt_3_3 = txt_1,':',n3
        
        print(tabela)
        C = int(input(txt_3_1))
        D = int(input(txt_3_2))
        U = int(input(txt_3_3))
   
        if (C or D or U >= V_min) and (C or D or U <= V_max):

            mult = int(input(txt_2))

            match mult:
                case 0:
                    mult_f = Black_Mul
                case 1:
                    mult_f = Brown_Mul
                case 2:
                    mult_f = Red_Mul
                case 3:
                    mult_f = Orange_Mul 
                case 4:
                    mult_f = Yellow_Mul
                case 5:
                    mult_f = Green_Mul
                case 6:
                    mult_f = Blue_Mul
                case 7:
                    mult_f = Purple_Mul
                case 8:
                    mult_f = Gray_Mul
                case 9:
                    mult_f = White_Mul
                case 10:
                    mult_f = Gold_Mul
                case 11:
                    mult_f = Silver_Mul
                case _:
                    print('Valor de multiplicador invalido! Finalizando programa')
                    exit()
            
            T = int(input(txt_3))

            match T:
                case 1:
                    T_f = Brown_T
                case 2:
                    T_f = Red_T
                case 5:
                    T_f = Green_T
                case 6:
                    T_f = Blue_T
                case 7:
                    T_f = Purple_T
                case 8:
                    T_f = Gray_T
                case 10:
                    T_f = Gold_T
                case 11:
                    T_f = Silver_T
                case _:
                    print('Valor de Tolerância invalido! Finalizando programa')
                    exit()

            Temp = int(input(txt_4))

            match Temp:
                case 1:
                    TP_f = Brown_TP
                case 2:
                    TP_f = Red_TP
                case 3:
                    TP_f = Orange_TP
                case 4:
                    TP_f = Yellow_TP
                case 6:
                    TP_f = Blue_TP
                case 7:
                    TP_f = Purple_TP
                case _:
                    print('Valor do Coeficiente de Temperatura invalido! Finalizando programa')
                    exit()

            if (C or D or U >= V_min2) and (C or D or U <= V_max2):

                match C:
                    case 0:
                        CF = Black_C
                    case 1:
                        CF = Brown_C
                    case 2:
                        CF = Red_C
                    case 3:
                        CF = Orange_C
                    case 4:
                        CF = Yellow_C
                    case 5:
                        CF = Green_C
                    case 6:
                        CF = Blue_C
                    case 7:
                        CF = Purple_C
                    case 8:
                        CF = Gray_C
                    case 9:
                        CF = White_C

                match D:
                    case 0:
                        DF = Black_D
                    case 1:
                        DF = Brown_D
                    case 2:
                        DF = Red_D
                    case 3:
                        DF = Orange_D
                    case 4:
                        DF = Yellow_D
                    case 5:
                        DF = Green_D
                    case 6:
                        DF = Blue_D
                    case 7:
                        DF = Purple_D
                    case 8:
                        DF = Gray_D
                    case 9:
                        DF = White_D

                match U:
                    case 0:
                        UF = Black_U
                    case 1:
                        UF = Brown_U
                    case 2:
                        UF = Red_U
                    case 3:
                        UF = Orange_U
                    case 4:
                        UF = Yellow_U
                    case 5:
                        UF = Green_U
                    case 6:
                        UF = Blue_U
                    case 7:
                        UF = Purple_U
                    case 8:
                        UF = Gray_U
                    case 9:
                        UF = White_U

                Res_value = float((CF + DF + UF) * mult_f)
                Tol_fn = float(Res_value - (Res_value * T_f))
                Tol_fp = float(Res_value + (Res_value * T_f))
                
                print(txt_F3, Res_value, 'e com tolerancia o valor é', Tol_fn, 'a', Tol_fp)
                print('A variação de resistência por temperatura é ', TP_f)
                exit()
            else:
                print(txt_E, V_min2, 'a', V_max2)
        else:
            print(txt_E, V_min, 'a', V_max )        