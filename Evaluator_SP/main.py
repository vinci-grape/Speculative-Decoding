from project.evaluator import Evaluator

def main():
    # 选择的模型、数据集和任务
    model_name = 'sample_model'
    dataset_name = 'dataset1'
    tasks = ['task1', 'task2']

    # 初始化评估器
    evaluator = Evaluator(model_name, dataset_name, tasks)
    
    # 运行评估流程
    results = evaluator.run_evaluation()

    # 打印评估结果
    print("Evaluation Results:", results)

if __name__ == '__main__':
    main()
