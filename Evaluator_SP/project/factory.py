from project.tasks.CodeFixes import CodeFixes
from project.tasks.CodeGeneration import CodeGeneration
from project.tasks.CodeTranslation import CodeTranslation
from project.tasks.TestCaseGeneration import TestCaseGeneration


class TaskFactory:
    @staticmethod
    def create_task(task_name):
        if task_name == 'task1':
            return CodeFixes()
        elif task_name == 'task2':
            return CodeGeneration()
        elif task_name ==   'task3':
            return CodeTranslation()
        elif task_name ==   'task4':
            return TestCaseGeneration()
        else:
            raise ValueError(f"Unknown task: {task_name}")

class DatasetFactory:
    @staticmethod
    def create_dataset(dataset_name):
        print(f"Loading dataset: {dataset_name}")
        # 假设返回数据集实例
        return f"Dataset({dataset_name})"

class ModelFactory:
    @staticmethod
    def create_model(model_name):
        print(f"Loading model: {model_name}")
        # 假设返回模型实例
        return f"Model({model_name})"
