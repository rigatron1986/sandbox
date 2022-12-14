# -*- coding: utf-8 -*-
"""
We have an idea to avoid 'cursor already closed' in XM that we can close connections every 30 secs.
Not sure it is helpful, if not, we should remove it.
"""


class MG:
    import logging
    logger = logging.getLogger(__name__)
    # {thread_id: [conn1_timer, conn2_timer, ...]}
    threads = {}
    time_out_seconds = 30


try:
    from PyQt4 import QtCore

    class Timer(QtCore.QObject):
        def __init__(self, conn, time_out_seconds=None):
            super(Timer, self).__init__()

            self.conn = conn
            if time_out_seconds is None:
                self.time_out_seconds = MG.time_out_seconds
            else:
                self.time_out_seconds = time_out_seconds
            # QtTimer requires msecs, so we should use secs * 1000
            self.timer_id = self.startTimer(self.time_out_seconds * 1000)

        def timerEvent(self, QTimerEvent):
            if QTimerEvent.timerId() == self.timer_id:
                MG.logger.debug('close connection because time out of {} secs'.format(self.time_out_seconds))
                try:
                    self.conn.close()
                except:
                    MG.logger.warning('failed to close the connection')

                # it should only trigger once, so delete it later after conn closed.
                self.killTimer(self.timer_id)
                self.deleteLater()
                try:
                    MG.threads[QtCore.QThread.currentThread()].remove(self)
                except:
                    MG.logger.warning('failed to delete qt object')
            else:
                return super(Timer, self).timerEvent(QTimerEvent)
except ImportError:
    QtCore = None


def add_connection(conn):
    # if QtCore doesn't exist, do nothing
    if QtCore is None or QtCore.QCoreApplication.instance() is None:
        return

    # if current_thread is not existing in the dict
    # add it and set default value as an empty set.
    # current_thread = QtCore.QThread.currentThreadId()  # currentThreadId doesn't exist in PySide2
    current_thread = QtCore.QThread.currentThread()
    if current_thread not in MG.threads:
        MG.threads[current_thread] = set()
    timers = MG.threads[current_thread]

    # add a new timer
    timer = Timer(conn)
    timers.add(timer)
