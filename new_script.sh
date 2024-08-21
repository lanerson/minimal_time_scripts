#!/bin/bash
echo instalando dependências
pip install matplotlib --break-system-packages
pip install mmh3 --break-system-packages
pip install xxhash --break-system-packages
pip install numpy --break-system-packages
pip install scipy --break-system-packages
pip install pandas --break-system-packages

echo obtendo framework
git clone https://github.com/claytonchagas/speedupy/

param=(db-file murmur 2d-ad)

# exps=(fibonacci copy_matrix prob_calculator look_and_say test_belief_propagation)
# cada grupo vai ficar com um experimento
exp="fibonacci"

arquivo="vals.txt"

rm *.prof
rm -rf graphs/ data/ jsons/ .intpy/
cat "$arquivo" | while IFS= read -r i ; do
	rm -rf .intpy/
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

