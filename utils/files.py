import os


class Files:
    @staticmethod
    def create_dirs_results_reports_is_not_exist():
        results_dir = "path/to/your/results_directory"
        allure_reports_dir = os.path.join(results_dir, "allure-results")
        os.makedirs(allure_reports_dir, exist_ok=True)
