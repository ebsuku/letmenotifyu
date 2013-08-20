
from gi.repository import Notify

def announce(*args):
    """Send to notification"""
    Notify.init("Letmenotifyu")
    if args[0] == "New Movie":
        print("Updating to new Movie")
        movie_show = Notify.Notification.new(args[0]+'\n',
                                             (args[1]+'\n'+args[2]).encode('utf-8'),'dialog-information')
        movie_show.show()
    else:
        series_show = Notify.Notification.new(args[0]+'\n', args[1]+'\n'+args[2], 'dialog-information')
        series_show.show()


