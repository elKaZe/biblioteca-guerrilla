from flask_frozen import Freezer

import main
freezer = Freezer(main.app)

if __name__ == '__main__':
        freezer.freeze()
