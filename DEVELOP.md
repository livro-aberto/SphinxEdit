
## Important files

    application/view.py

    application/template/edit.html

## You may need to use the virtual environment

    source vir/bin/activate

## Init translations

You may need:

    source vir/bin/activate

In the applications folder

    pybabel extract -F babel.cfg -o messages.pot .

    pybabel init -i messages.pot -d translations -l de

    pybabel compile -d translations

## Update translations

You may need:

    source vir/bin/activate

Then in folder `applications` type:

    pybabel extract -F babel.cfg -o messages.pot .

    pybabel update -i messages.pot -d translations

Do the actual translation, then

    pybabel compile -d translations

## Code style

  - indent always by 2 spaces.
