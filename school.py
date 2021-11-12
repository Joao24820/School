from time import sleep

print('====BEM VINDO A ESCOLA LEARN HOUSE===')

name = str(input('Sr(a) informe o seu primeiro nome: '))
tip = str(input('Informe o tipo de acesso ALUNO ou PROFESSOR: '))
if tip == 'ALUNO':
    resp = int(input('O Senhor tem Cadastro [0] não [1] sim:'))
    if resp == 0:
        print('REALIZE O SEU CADASTRO !!')
        sn = str(input('sr {} Informe o seu sobrenome: '.format(name)))
        datan = int(input('Informe seu ano de nascimento: '))
        s = 2021 - datan
        print('Atualmente o aluno {} tem {} anos de idade '.format(name, s))
        doc = int(input('Informe o documento que gostaria 1=RG e 2=CPF :'))
        if doc == 1:
            input('Informe o numero do seu RG: ')
        elif doc == 2:
            input('Informe o numero do seu CPF: ')
        else:
            print('Escolha errada !')

        b = str(input('Informe o bairro onde o Aluno reside: '))
        muni = str(input('Informe o municipio do bairro {} :'.format(b)))
        r = str(input('{}, Informe o nome da rua do aluno: '.format(name)))
        c = int(input('sua casa tem numero sim=1 ou não=0: '))
        if c == 1:
            input('Informe o numero da sua casa: ')
        elif c == 0:
            print('OK, Vamos continuar !!!')
        elif 'c >= 2' or '<=-1':
            print('Opção Invalida')
        else:
            print('Opção invalida')

        mod = str(input('Sr {}, informe em qual modalidade (Primaria/Fundamental/Medio/Tecnico/Graduação) '
                        'o senhor se encontra: '.format(name)))
        if mod == 'primaria':
            a = int(input('Sr {}, informe em qual ANO do ensino {} o sr(a) se encontra: '.format(name, mod)))
        if mod == 'fundamental':
            p = int(input('Sr {}, informe em qual SERIE do ensino {} o sr(a) se encontra: '.format(name, mod)))
        if mod == 'medio':
            p = int(input('Sr {}, informe em qual ANO do ensino {} o sr(a) se encontra: '.format(name, mod)))
        if mod == 'tecnico':
            pe = int(input('Sr {}, informe em qual PERIODO do ensino {} o sr(a) se encontra: '.format(name, mod)))
        if mod == 'graduação':
            fac = str(input('Sr {}, informe qual faculdade o sr esta cursando: '))
            p = int(input('Sr {}, informe em qual PERIODO do ensino {} da graduação de {} o sr(a) se encontra: '
                          ''.format(name, mod, fac)))

        tur = str(input('Sr(a) {}, escolha entre as turma (J1,J2,J3,J4,J5) em que gostaria de entrar: '.format(name)))
        print('Sr {}, o senhor será da turma {} nesse periodo na modalidade {} no periodo '.format(name, tur, mod, ))

    if resp == 1:
        mod = str(input('Sr(a){}, informe em qual modalidade (Primaria/Fundamental/Medio/Tecnico/Graduação) '
                        'o senhor se encontra: '.format(name)))
        if mod == 'primaria':
            a = int(input('Sr {}, informe em qual ANO do ensino {} o sr(a) se encontra: '.format(name, mod)))
        if mod == 'fundamental':
            p = int(input('Sr {}, informe em qual SERIE do ensino {} o sr(a) se encontra: '.format(name, mod)))
        if mod == 'medio':
            p = int(input('Sr {}, informe em qual ANO do ensino {} o sr(a) se encontra: '.format(name, mod)))
        if mod == 'tecnico':
            pe = int(input('Sr {}, informe em qual PERIODO do ensino {} o sr(a) se encontra: '.format(name, mod)))
        if mod == 'graduação':
            fac = str(input('Sr {}, informe qual faculdade o sr esta cursando: '))
            p = int(input('Sr {}, informe em qual PERIODO do ensino {} da graduação de {} o sr(a) se encontra: '
                          ''.format(name, mod, fac)))
    sleep(2)
    print('== CADASTRO FINALIZADO ==', '\n == OBRIGADO ==', '\n == SEJA BEM VINDO SR(A) {} =)'.format(name))

if tip == 'PROFESSOR':
    print('Seja bem vindo professor(a) {} '.format(name))
    sh = int(input('Professor(a): {} , por favor informe a sua senha: '.format(name)))
    if sh != 123456:
        print('A senha informada está errada !!')
        print('Programa Finalizado !!')
    else:
        mat = str(input('Informe a materia em que lesiona: '))
        con = str(input('Sr {} informe agora o aluno(a) que gostaria de analisar: '.format(name)))
        print('Estamos iniciando a consulta e lançamentos das notas do aluno(a) {} '.format(con))

        sleep(2)

        n1 = float(input('Diga a primeira nota do(a) {} :'.format(con)))
        n2 = float(input('Diga a segunda nota do(a) {} :'.format(con)))
        n3 = float(input('Diga a terceira nota do(a) {} :'.format(con)))

        media = (n1 + n2 + n3)

        if media < 17.0:
            print('O aluno(a) {} ficou com a media {:.1f} e esta REPROVADO. '.format(con, media))
        elif 18.0 <= media < 59.9:
            print('O aluno(a) {} esta com a media {:.1f} e esta de RECUPERAÇÃO. '.format(con, media))
        elif media >= 60.0:
            print('O aluno(a) {} esta com a media {:.1f} e foi APROVADO '.format(con, media))


else:
    print('OPÇÃO  INVALIDA, CONSULTA FINALIZADA !!')
