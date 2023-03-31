import cv2

system = cv2.imread("solar-system.jpg") # carrega a imagem
cv2.putText(system,
            "sistema solar", # colocando um text na imagem 
            cv2.FONT_HERSHEY_COMPLEX, # font
            0.5, # tamanho
            (32, 186, 140) # cor
            )
cv2.imshow("sistema solar",system) # cria uma nova janela com a imagem
cv2.imwrite("sistema-solar.jpg",system) # baixa a imagem depois da edição

