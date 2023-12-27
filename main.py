sustantivo= input("sustantivo:  ") 
verbo =input("verbo: ")
otroSustantivo2 =input("otroSustantivo: ")
otroSustantivo3 =input("otroSustantivo: ")
verbo2 =input("verbo: ")
otroSustantivo4 =input("otroSustantivo: ")

 

madLibs = "Hola! Te doy la bienvenida el " +sustantivo+ " del ejercicio de Python donde aprenderemos a" +verbo +" info del "+ otroSustantivo2 + " y " + verbo2 + " con los "+otroSustantivo3 + " (f-strings) y ver los resultados impresos en "+otroSustantivo4 +" consola"

madLibs2 = f"Hola! Te doy la bienvenida el {sustantivo} del ejercicio de Python donde aprenderemos a {verbo} info del {otroSustantivo2} y {verbo2}  con los {otroSustantivo4}(f-strings) y ver los resultados impresos en {otroSustantivo3} consola"


print(madLibs)