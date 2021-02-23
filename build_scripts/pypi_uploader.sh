cd ..
python -m pep517.build .
twine upload dist/*
rm -rf build/
rm -rf dist/
rm -rf scicm.egg-info/
