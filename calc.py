class Function:
    step = 0.000001
    divisions = 100000

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self.func(*args)

    def prime(self, step=None):
        step = step or self.step
        return Function(lambda x: float(self(x + step) - self(x)) / float(step))

    def integral(self, method="riemann", **kwargs):
        if method == 'riemann':
            return self._riemann_sum(**kwargs)
        elif method == 'trapezoid':
            return self._trapezoid_rule(**kwargs)
        elif method == 'simpsons':
            return self._simpsons_rule(**kwargs)
        else:
            raise ValueError("Integration is only supported using one of 'riemann', 'trapezoid', or 'simpsons'")

    def _trapezoid_rule(self, **kwargs):
        pass

    def _simpsons_rule(self, **kwargs):
        pass

    def _riemann_sum(self, **kwargs):
        divisions = kwargs.get("divisions", self.divisions)
        lims = kwargs.get("lims")
        side = kwargs.get("side", "left")
        if lims is None:
            def integral(x):
                step = float(x) / float(divisions)
                if side == "left":
                    return sum(self(j * step) * step for j in range(divisions))
                if side == "right":
                    return sum(self(j * step) * step for j in range(1, divisions + 1))
                if side == "center":
                    return sum(self((j + 0.5) * step) * step for j in range(divisions))

            return Function(integral)

        step_size = float(lims[1] - lims[0]) / float(divisions)
        if side == "left":
            return sum(self(lims[0] + j * step_size) * step_size for j in range(divisions))
        if side == "right":
            return sum(self(lims[0] + j * step_size) * step_size for j in range(1, divisions + 1))
        if side == "center":
            return sum(self(lims[0] + (j + 0.5) * step_size) * step_size for j in range(divisions))
