#!/bin/bash
# instalando dependências
pip install matplotlib
pip installnmmh3
pip install xxhash


# Realizando probe
python3 probe.py

# obtendo framework
git clone https://github.com/claytonchagas/speedupy/

# obtendo experimentos
wget https://raw.githubusercontent.com/claytonchagas/speedupy_experiments/main/01pilots/01pilots_exp01_fibonacci/fibonacci.py
wget https://raw.githubusercontent.com/claytonchagas/speedupy_experiments/main/01pilots/01pilots_exp06_eq_solver/eq_solver.py
wget https://raw.githubusercontent.com/claytonchagas/speedupy_experiments/main/01pilots/01pilots_exp07_prob_calculator/prob_calculator.py
wget https://raw.githubusercontent.com/claytonchagas/speedupy_experiments/main/04benchproglangs/04benchpl_exp02_look_and_say_OK/look_and_say.py
wget https://raw.githubusercontent.com/claytonchagas/speedupy_experiments/main/04benchproglangs/04benchpl_exp06_belief_propagation_OK/test_belief_propagation.py

# definindo variáveis para execução
exps=('fibonacci.py' 'eqsolver.py' 'prob_calculator.py' 'qho2.py' 'test_belief_propagation.py')


params1=('file' 'murmur' '2d-ad')
params2=('file' 'xxhash' '2d-ad')
params3=('db-file' 'murmur' '2d-ad')
params4=('file' 'xxhash' '2d-ad')
params5=('db-file' 'murmur' '2d-ad')

params=(params1 params2 params3 params4 params5)
vals1=(5 10 15 20 25 30 35 40 45 50)
vals2=()
vals3=()
vals4=()
vals5=()

vals=(vals1 vals2 vals3 vals4 vals5)
for i in {0..4}; do
	for j in {0..9}; do
		for k in {1..5}; do
			python3 ${exps[i]} ${vals[$((10*i+j))]}  -s ${params[$(3*i)]} -H ${params[$((3*i+1))]} -m ${params[$((3*i+2))]};
		done
		python3 ${exps[i]}  ${vals[$((10*i+j))]} --no-cache;
	done
done
