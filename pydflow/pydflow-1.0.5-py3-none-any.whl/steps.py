from argo.workflows.client import V1alpha1Template
from .op_template import OPTemplate

class Steps(OPTemplate):
    def __init__(self, name, inputs=None, outputs=None, steps=None, memoize_key=None, key=None):
        """
        Instantiate a steps
        :param name: the name of the steps
        :param inputs: inputs in the template
        :param outputs: outputs in the template
        :param steps: a sequential list of steps
        :param memoize_key: memoized key of the steps
        :param key: the key of the steps
        :return:
        """
        super().__init__(name=name, inputs=inputs, outputs=outputs, memoize_key=memoize_key, key=key)
        if steps is not None:
            self.steps = steps
        else:
            self.steps = []

    def __iter__(self):
        return iter(self.steps)

    def add(self, step):
        """
        Add a step or a list of parallel steps to the steps
        :param step: a step or a list of parallel steps to be added to the entrypoint of the workflow
        :return:
        """
        self.steps.append(step)

    def convert_to_argo(self, memoize_prefix=None, memoize_configmap="dflow-config"):
        argo_steps = []
        templates = []
        assert len(self.steps) > 0, "Steps %s is empty" % self.name
        for step in self.steps:
            # each step of steps should be a list of parallel steps, if not, create a sigleton
            if not isinstance(step, list):
                step = [step]
            argo_parallel_steps = []
            for ps in step:
                argo_parallel_steps.append(ps.convert_to_argo())
                templates.append(ps.template) # template may change after conversion
            argo_steps.append(argo_parallel_steps)
            if len(step) == 1 and step[0].check_step is not None:
                argo_steps.append([step[0].check_step.convert_to_argo()])
                templates.append(step[0].check_step.template)

        self.handle_key(memoize_prefix, memoize_configmap)
        argo_template = V1alpha1Template(name=self.name,
                steps=argo_steps,
                inputs=self.inputs.convert_to_argo(),
                outputs=self.outputs.convert_to_argo(),
                memoize=self.memoize)
        return argo_template, templates

    def run(self):
        for step in self:
            if isinstance(step, list):
                for ps in step:
                    ps.run(self)
            else:
                step.run(self)
