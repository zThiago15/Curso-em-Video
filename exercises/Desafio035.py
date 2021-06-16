print('\033[30m=-'*20)
print('Analisador de Triângulos!')
print('=-'*20)
s1 = float(input('\033[30mPrimeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print(f'Os segmentos acima \033[33mPODEM FORMAR \033[30mum triângulo!')
else:
    print(f'Os segmentos acima \033[31mNÃO PODEM FORMAR \033[30mum triângulo!')