from tree_browsing import minimax, alpha_beta_pruning, negamax, negamax_alpha_beta
import testing_toolbox
import time

tree = testing_toolbox.generate_random_tree(nb_levels=7, nb_children=5)


nom_et_temps = []
print('===============================================================================================================')
start = time.time()
print(minimax.minimax_wrapper(tree, True))
end = time.time()
nom_et_temps.append(('minimax', end - start))
#print('Time min-max:', end - start)

print('===============================================================================================================')
start = time.time()
print(alpha_beta_pruning.alpha_beta_wrapper(tree, True))
end = time.time()
nom_et_temps.append(('alpha_beta_pruning', end - start))
#print('Time alpha-beta:', end - start)

print('===============================================================================================================')
start = time.time()
print(negamax.negamax_wrapper(tree, 1))
end = time.time()
nom_et_temps.append(('negamax', end - start))
#print('Time negamax:', end - start)

print('===============================================================================================================')
start = time.time()
print(negamax_alpha_beta.negamax_alpha_beta_wrapper(tree, 1))
end = time.time()
nom_et_temps.append(('negamax alpha-beta', end - start))
#rint('Time negamax alpha-beta:', end - start)


for algo in sorted(nom_et_temps, key=lambda algo: algo[1]):
    print(algo[0],':',' ' * (50 - len(algo[0])), algo[1])
