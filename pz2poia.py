import logging
logging.basicConfig( #логгер в файл
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%H:%M:%S',
    handlers=[logging.FileHandler('transport_solution.log', mode='w', encoding='utf-8')]
)
log = logging.getLogger()
log.propagate = False

strategies = ["A1 (10т)", "A2 (15т)", "A3 (20т)", "A4 (25т)"] #исходные данные
demand = ["П1(10т)", "П2(15т)", "П3(20т)", "П4(25т)"]

#матрица затрат
C = [
    [6,  12,  20,  24], 
    [9,   7,   9,  28],
    [23, 18,  15,  19],
    [27, 24,  21,  15],
]

log.info("Задача транспортного предприятия")
log.info("Матрица затрат:")
for i in range(4):
    log.info(f"{strategies[i]}: {C[i]}")

log.info("КРИТЕРИЙ ВАЛЬДА") #Критерий вальда
max_costs = [max(C[i]) for i in range(4)]
wald = max_costs.index(min(max_costs))
log.info(f"Макс.затраты: {max_costs}")
log.info(f"Результат: {strategies[wald]} (W={min(max_costs)})")

log.info("\n--- МАТРИЦА РИСКОВ ---") #Матрица рисков
min_by_demand = [min(C[i][j] for i in range(4)) for j in range(4)]
R = [[C[i][j] - min_by_demand[j] for j in range(4)] for i in range(4)]
log.info(f"Минимумы по столбцам: {min_by_demand}")
for i in range(4):
    log.info(f"{strategies[i]}: {R[i]}")

log.info("КРИТЕРИЙ СЭВИДЖА") #Критерий Сэвиджа
max_risks = [max(R[i]) for i in range(4)]
savage = max_risks.index(min(max_risks))
log.info(f"Макс. риски: {max_risks}")
log.info(f"Результат: {strategies[savage]} (S={min(max_risks)})")

log.info("КРИТЕРИЙ ГУРВИЦА") #Критерий Гурвица
alpha = 0.5
min_r = [min(R[i]) for i in range(4)]
max_r = [max(R[i]) for i in range(4)]
H = [alpha * max_r[i] + (1-alpha) * min_r[i] for i in range(4)]
hurwicz = H.index(min(H))
log.info(f"H = 0.5*max + 0.5*min риска: {H}")
log.info(f"Результат: {strategies[hurwicz]} (HR={min(H)})")

#Итог
log.info("Итог:")
log.info(f"Вальд:  {strategies[wald]}")
log.info(f"Сэвидж: {strategies[savage]}")
log.info(f"Гурвиц: {strategies[hurwicz]}")

#Выбор стратегии
votes = [0, 0, 0, 0]
votes[wald] += 1
votes[savage] += 1
votes[hurwicz] += 1
final = votes.index(max(votes))

log.info(f"Рекомендуемая стратегия: {strategies[final]}")
log.info(f"(удовлетворяет {max(votes)} из 3 критериев)")