from typing import List, Dict, Any

class AutomationTool:
    """A class representing the automation tool."""
    
    def __init__(self, name: str, version: str) -> None:
        """Initialize the automation tool with name and version."""
        self.name = name
        self.version = version
        self.tasks: List[Dict[str, Any]] = []

    def add_task(self, task: Dict[str, Any]) -> None:
        """Add a new task to the automation tool."""
        self.tasks.append(task)

    def run_tasks(self) -> None:
        """Execute all tasks in the automation tool."""
        for task in self.tasks:
            print(f'Running task: {task.get("name", "Unnamed Task")}')
            # Here, some specific logic would be executed for each task.

    def get_task_summary(self) -> List[str]:
        """Return a summary of all tasks."""
        return [task.get("name", "Unnamed Task") for task in self.tasks]

if __name__ == '__main__':
    tool = AutomationTool(name='Automation Tool 83', version='1.0')
    tool.add_task({'name': 'Task 1', 'action': 'action_1'})
    tool.add_task({'name': 'Task 2', 'action': 'action_2'})
    tool.run_tasks()
    print(tool.get_task_summary())