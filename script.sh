#!/bin/bash
echo instalando dependências
pip install matplotlib
pip install mmh3
pip install xxhash
pip install numpy

echo obtendo framework
git clone https://github.com/claytonchagas/speedupy/

# definindo variáveis para execução (específicas para esse teste)

params1=(file murmur 2d-ad)
params2=(db-file murmur 2d-ad)
params3=(db-file murmur 2d-ad)
params4=(file xxhash 2d-ad)
params5=(db-file murmur 2d-ad)

vals1=(3 6 9 12 15 18 21 24 27 30)
vals2=(100 200 300 400 500 600 700 800 900 1000)
vals3=(100 150 200 250 300 350 400 450 500 550)
vals4=(30 31 32 33 34 35 36 37 38 39 40)
vals5=(10 20 30 40 50 60 70 80 90 100)

exps=(fibonacci copy_matrix prob_calculator look_and_say test_belief_propagation)

for k in {0..4}; do
	for i in {0..9}; do
		python3 ${exps[k]}.py  ${vals1[((i))]} --no-cache;
		python3 analyze_profile.py ${exps[k]}_profile.prof ${exps[k]}_data.json
		for j in {1..5}; do
			python3 ${exps[k]}.py ${vals1[$((i))]}  -s ${params1[((0))]} -H ${params1[((1))]} -m ${params1[((2))]};
			python3 analyze_profile.py ${exps[k]}_profile.prof ${exps[k]}_data_cache.json
		done
	done
done

mkdir graphs jsons
mv *.json jsons/