cd ..
python -m pep517.build .
twine upload dist/* -r scicm
rm -rf build/
rm -rf dist/
rm -rf scicm.egg-info/
