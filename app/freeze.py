from flask_frozen import Freezer


from app import main
freezer = Freezer(main)

if __name__ == '__main__':
        freezer.freeze()

