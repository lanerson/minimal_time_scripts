#!/bin/bash
echo instalando dependências
pip install matplotlib
pip install mmh3
pip install xxhash
pip install numpy

echo obtendo framework
git clone https://github.com/claytonchagas/speedupy/

param=(db-file murmur 2d-ad)

# exps=(fibonacci copy_matrix prob_calculator look_and_say test_belief_propagation)
# cada grupo vai ficar com um experimento
exp="fibonacci"

arquivo="vals.txt"

rm *.prof

cat "$arquivo" | while IFS= read -r i ; do
	echo "execução $i"
	python3 ${exp}.py  $i --no-cache;
	python3 analyze_profile.py ${exp}_profile.prof ${exp}_data.json
	for j in {1..5}; do
		python3 ${exp}.py $i  -s ${param[((0))]} -H ${param[((1))]} -m ${param[((2))]};
		python3 analyze_profile.py ${exp}_profile.prof ${exp}_data_cache.json
	done
done

mkdir graphs jsons data
mv *.json jsons/
rm *.prof 

