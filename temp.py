import pywhatkit
import xlrd

arq=xlrd.open_workbook("C:/Users/Basaglia/Desktop/Clientes_Portal.xls")
plan=arq.sheet_by_name("Dados")

x=plan.col_values(0)
y=plan.col_values(1)

for i in range(len(x)):
    print(f"Message sent to {y[i]}");
    message = "Olá, caro assinante, confira a edição do jornal desta semana! https://canaldosul.com.br/edicoes-digitais " + x[i];
    pywhatkit.sendwhatmsg_instantly(y[i], message, 15, True, 5);

    