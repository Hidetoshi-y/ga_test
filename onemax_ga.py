# coding: utf8
import random
import copy

#OneMax問題をGAで解いてみる

#パラメータを定義
LIST_SIZE = 10          #0/1のリスト長　遺伝子長

POPULATION_SIZE = 10    #集合体の個体数
GENERATION = 25         #世代数
MUTATE = 0.1            #突然変異の確率10%
SELECT_RATE = 0.5       #選択割合

#適応度を計算する
def calc_fitness(individual):
    return sum(individual)  #リストの要素の合計

#集団を適応度順にソートする
def sort_fitness(population):
    #適用度と個体をタプルにしてリストへ格納する
    fp = []
for individual in population:
    fitnees = calc_fitness(individual)
    fp.append((fitnees, individual))
fp.sort(reverse=True)   #適用度でソート(Trueなので降順)

#ソートした個体を格納する集団
sorted_population = []

#個体を取り出し、集団に格納する
for fitnees, individual in fp:
    sorted_population.append(individual)
return sorted_population

#適用度の高い個体を残す
def selection(population):
    sorted_population = sort_fitness(population)
    #残す個体数　このプログラムのパラメータではnは常に５
    n = int(POPULATION_SIZE * SELECT_RATE)
    return sorted_population[0:n]

#交叉
#indlをコピーして新しい個体indを作る　その後ランダムに決めたr1~r2の範囲をind2の遺伝子に置き換える
def crossover(indl, ind2):
    r1 = random.randint(0, LIST_SIZE - 1)
    r2 = random.randint(r1 + 1, LIST_SIZE -1)
    ind = copy.deepcopy(indl)
    ind[r1:r2] = ind2[r1:r2]
    return ind

#突然変異
#突然変異確率(MUTATE)に従って突然変異させる
