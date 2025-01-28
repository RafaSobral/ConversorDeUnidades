from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tamanho(request):
    if request.method == "POST":
        valor = float(request.POST.get('tamanho'))
        un1 = request.POST.get('unidade1')
        un2 = request.POST.get("unidade2")
        def converter_unidade(valor, un1, un2):
            unidades = {
                'metro': 1,
                'quilometro': 1000,
                'milha': 1509.34,
                'centimetro': 0.01
            }
            valor_metro = valor * unidades[un1]
            valor_convertido = valor_metro / unidades[un2]
            return valor_convertido
        valor_convertido = converter_unidade(valor, un1, un2)
        return render(request, 'tamanho.html', {'valor_convertido': valor_convertido, 'un2': un2})

    return render(request, 'tamanho.html')

def peso(request):
    if request.method == "POST":
        valor = float(request.POST.get('peso'))
        un1 = request.POST.get('unidade1')
        un2 = request.POST.get("unidade2")
        def converter_unidade(valor, un1, un2):
            unidades = {
                'kg': 1,      
                'g': 1000,    
                'lb': 2.20462, 
                'oz': 35.274   
            }
            valor_metro = valor * unidades[un1]
            valor_convertido = valor_metro / unidades[un2]
            return valor_convertido
        valor_convertido = converter_unidade(valor, un1, un2)
        return render(request, 'peso.html', {'valor_convertido': valor_convertido, 'un2': un2})

    return render(request, 'peso.html')


def temperatura(request):
    if request.method == "POST":
        valor = float(request.POST.get('temperatura'))  
        un1 = request.POST.get('unidade1')  
        un2 = request.POST.get('unidade2')  
        def converter_temperatura(valor, un1, un2):
            if un1 == un2:
                return valor  
            
            # Celsius para outras unidades
            if un1 == 'C':
                if un2 == 'F':
                    return (valor * 9/5) + 32 
                elif un2 == 'K':
                    return valor + 273.15  
                elif un2 == 'R':
                    return (valor + 273.15) * 9/5  

            # Fahrenheit para outras unidades
            if un1 == 'F':
                if un2 == 'C':
                    return (valor - 32) * 5/9 
                elif un2 == 'K':
                    return (valor - 32) * 5/9 + 273.15  
                elif un2 == 'R':
                    return valor + 459.67  

            # Kelvin para outras unidades
            if un1 == 'K':
                if un2 == 'C':
                    return valor - 273.15  
                elif un2 == 'F':
                    return (valor - 273.15) * 9/5 + 32  
                elif un2 == 'R':
                    return valor * 9/5  

            # Rankine para outras unidades
            if un1 == 'R':
                if un2 == 'C':
                    return (valor - 491.67) * 5/9  
                elif un2 == 'F':
                    return valor - 459.67  
                elif un2 == 'K':
                    return valor * 5/9  

            return valor  

        valor_convertido = converter_temperatura(valor, un1, un2)
        return render(request, 'temperatura.html', {'valor_convertido': valor_convertido, 'un2': un2})

    return render(request, 'temperatura.html')


