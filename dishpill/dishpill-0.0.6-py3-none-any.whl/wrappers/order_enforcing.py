import dishpill


class OrderEnforcing(dishpill.Wrapper):
    """This will produce an error if `step` is called before an initial `reset`"""

    def __init__(self, env):
        super().__init__(env)
        self._has_reset = False

    def step(self, action):
        assert self._has_reset, "Cannot call env.step() before calling reset()"
        observation, reward, done, info = self.env.step(action)
        return observation, reward, done, info

    def reset(self, **kwargs):
        self._has_reset = True
        return self.env.reset(**kwargs)
