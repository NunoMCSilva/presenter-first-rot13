"""ROT13 main module"""

from rot13.model import ApplicationModel
from rot13.presenter import ApplicationPresenter
from rot13.view import ApplicationView


def main():
    model = ApplicationModel()
    view = ApplicationView.get_view()
    _ = ApplicationPresenter(model, view)

    model.run()


if __name__ == '__main__':
    main()
