import matplotlib
import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))

    CurPos = [50, 100, 640, 480]
    backend = matplotlib.get_backend()

    if 'WX' in backend:
        mgr = plt.get_current_fig_manager()
        mgr.window.SetPosition((CurPos[0], CurPos[1]))
        mgr.window.SetSize((CurPos[2], CurPos[3]))
    elif 'QT' in backend:
        mgr = plt.get_current_fig_manager()
        mgr.window.setGeometry(CurPos[0], CurPos[1], CurPos[2], CurPos[3])
    else:
        pass

    plt.show(block=False)
    plt.pause(.1)
