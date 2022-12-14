# -*- coding: utf-8 -*-
import time


class Monitoring(object):
    _monitorings_ = []

    def __init__(self, name="default", f=None):
        super(Monitoring, self).__init__()
        self._monitorings_.append(self)
        self.name = name
        self.f = f

        class MonitoringDecorator(object):
            _monitoring_ = self
            _decorators_ = []
            _statistics_methods_ = {}
            _before_func_running_callbacks_ = {}
            _after_func_running_callbacks_ = {}

            def __init__(self, name=None):
                super(MonitoringDecorator, self).__init__()
                self._decorators_.append(self)
                self.name = name

            def before_func_running_callback(self, func, args, kwargs):
                return {name: cb(self, func, args, kwargs) for name, cb in self._before_func_running_callbacks_.items()}

            def __call__(self, func):
                if self.name is None:
                    self.name = func.__name__

                def decorator_func(*args, **kwargs):
                    before_callback_return_values = self.before_func_running_callback(func, args, kwargs)
                    return_value = func(*args, **kwargs)
                    self.after_func_running_callback(func, return_value, before_callback_return_values)
                    return return_value

                return decorator_func

            def after_func_running_callback(self, func, return_value, before_callback_return_values):
                for name, cb in self._after_func_running_callbacks_.items():
                    cb(self, func, return_value, before_callback_return_values[name])

            def get_result(self):
                return {name: method(self) for name, method in self._statistics_methods_.items()}

            @classmethod
            def get_results(cls):
                return [decorator.get_result() for decorator in cls._decorators_]

            @classmethod
            def register_statistics_method(cls, name, method):
                cls._statistics_methods_[name] = method

            @classmethod
            def register_before_func_running_callback(cls, name, method):
                cls._before_func_running_callbacks_[name] = method

            @classmethod
            def register_after_func_running_callback(cls, name, method):
                cls._after_func_running_callbacks_[name] = method

        self.decorator = MonitoringDecorator

        self.decorator.register_statistics_method(
            "MonitorName",
            lambda x: self.name)
        self.decorator.register_statistics_method(
            "ItemName",
            lambda x: x.name)

    def get_results(self, f=None):
        _f = f or self.f
        result = self.decorator.get_results()
        if _f:
            _f.write(str(result))
        return result

    @classmethod
    def get_all_results(cls, f=None):
        return [monitoring.get_results(f) for monitoring in cls._monitorings_]


class CallingCountMonitoring(Monitoring):
    def __init__(self, f=None):
        super(CallingCountMonitoring, self).__init__(f)

        class MonitoringDecorator(self.decorator):
            def __init__(self, name=None):
                super(MonitoringDecorator, self).__init__(name)
                self.calling_time_history = []

        self.decorator = MonitoringDecorator

        def func_start_time(decorator, calling_function, args, kwargs):
            return time.time()

        self.decorator.register_before_func_running_callback("calling_time", func_start_time)

        def func_end_time(decorator, calling_function, return_value, before_callback_return_value):
            decorator.calling_time_history.append((before_callback_return_value, time.time()))

        self.decorator.register_after_func_running_callback("calling_time", func_end_time)

        self.decorator.register_statistics_method(
            "calling_count",
            lambda x: len(x.calling_time_history))
        self.decorator.register_statistics_method(
            "time_used",
            lambda x: sum([end_time - start_time for start_time, end_time in x.calling_time_history]))
        self.decorator.register_statistics_method(
            "ave_time_used",
            lambda x: sum([end_time - start_time
                           for start_time, end_time in x.calling_time_history]) / (len(x.calling_time_history) or 1))
