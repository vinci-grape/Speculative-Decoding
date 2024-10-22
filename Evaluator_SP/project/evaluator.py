from project.factory import TaskFactory, DatasetFactory, ModelFactory

class Evaluator:
    def __init__(self, model_name, dataset_name, tasks):
        self.model = ModelFactory.create_model(model_name)
        self.dataset = DatasetFactory.create_dataset(dataset_name)
        self.tasks = [TaskFactory.create_task(task) for task in tasks]

    def run_evaluation(self):
        results = {}
        for task in self.tasks:
            print(f"Running {task.__class__.__name__}")
            results[task.__class__.__name__] = task.evaluate(self.model, self.dataset)
        return results
