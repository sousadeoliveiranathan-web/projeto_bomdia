import sys

#Função principal
def main() -> None:
    #Se a lista de argumentos passados na linha de comando tiver 2 elementos,
    #executa a função conditions
    if (len(sys.argv) == 2):
        arg = sys.argv[1]
        conditions(arg)

    else:
        #Se a lista de argumentos passados na linha de comando tiver 1 elemento,
        #mensagem de erro e executar a função help
        if (len(sys.argv) == 1):
            error_no_arg()

        #Caso contrário, erro, pois o usuário terá informado mais de uma opção
        else:
            error_more_then_one_arg()

def help() -> None:
    print(
        "Para executar o programa, digite o comando: bomdia [opção para idioma]\n" \
        "O programa será finalizado logo após a execução do comando\n" \
        "Opções disponíveis:\n" \
        "--help ou -h (documentação do software);\n" \
        "--version ou -v (versão do software);\n" \
        "--pt ou -1 (idioma português);\n" \
        "--en ou -2 (idioma inglês);\n" \
        "--es ou -3 (idioma espanhol);\n" \
        "--fr ou -4 (idioma francês);\n" \
        "--it ou -5 (idioma italiano);\n" \
        "--co ou -6 (idioma coreano);\n" \
        "--ja ou -7 (idioma japonês);\n" \
        "--ru ou -8 (idioma russo);"
    )
    
def version() -> None:
    print("Versão 1.0.0")

def conditions(opcao: str) -> None:
    if (opcao == "--help" or opcao == "-h"):
        help()

    elif (opcao == "--version" or opcao == "-v"):
        version()

    elif (opcao == "--pt" or opcao == "-1"):
        print("Bom Dia!")

    elif (opcao == "--en" or opcao == "-2"):
        print("Good Morning!")

    elif (opcao == "--es" or opcao == "-3"):
        print("Buen día!")

    elif (opcao == "--fr" or opcao == "-4"):
        print("Bonjour!")

    elif (opcao == "--it" or opcao == "-5"):
        print("Buongiorno!")

    elif (opcao == "--co" or opcao == "-6"):
        print("좋은 아침이에요!")

    elif (opcao == "--ja" or opcao == "-7"):
        print("おはよう!")

    elif (opcao == "--ru" or opcao == "-8"):
        print("Доброе утро!")

    #Se o argumento informado não for igual a nenhuma das opções
    #informa que a opção informada não existe e orienta sobre o help
    else:
        error_invalid_arg()
    
def error_no_arg() -> None:
    print("Erro: opção de idioma não informada")
    help()
    
def error_more_then_one_arg() -> None:
    print(
                "Erro: mais de uma opção no comando\n" \
                "Para mais informações, digite o comando bomdia --help ou bomdia -h"
        )
    
def error_invalid_arg() -> None:
    print(
            "Erro: a opção selecionada não existe no sistema\n" \
            "Para mais informações, digite o comando bomdia --help ou bomdia -h"
        )

#Se o arquivo estiver sendo executado diretamente,
#executar a função main
if (__name__ == "__main__"):
    main()
