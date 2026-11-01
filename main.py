from pathlib import Path

from jinja2 import Environment, FileSystemLoader
import yaml

PROJECTS_DIR = Path("projects")
EXPERIENCE_DIR = Path("experience")
TEMPLATE_DIR = Path("templates")
OUTPUT_PATH = Path("index.html")


def parse_experience():
    """Parse .yaml files in the experience directory"""
    experience_list = []
    for experience in EXPERIENCE_DIR.iterdir():
        if experience.is_file():
            try:
                with open(experience, "r") as f:
                    experience_info = yaml.safe_load(f)

                experience_list.append(experience_info)

            except Exception as e:
                continue

    experience_list = sorted(experience_list, key=lambda x: x["number"], reverse=True)

    return experience_list


def parse_projects():
    """Parse .yaml files in the projects directory"""
    project_list = []
    for project in PROJECTS_DIR.iterdir():
        if project.is_file():
            try:
                with open(project, "r") as f:
                    project_info = yaml.safe_load(f)

                project_list.append(project_info)

            except Exception as e:
                continue

    project_list = sorted(project_list, key=lambda x: x["number"], reverse=True)

    return project_list


def render_index(experience_list, project_list):
    """Renders index.html with project and experience information"""
    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)

    template = env.get_template("index_template.html")
    context = {"experience_list": experience_list, "project_list": project_list}

    rendered_html = template.render(context)

    OUTPUT_PATH.touch()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(rendered_html)


def main():
    """Runs the .html generator"""
    experience_list = parse_experience()
    project_list = parse_projects()
    render_index(experience_list=experience_list, project_list=project_list)


if __name__ == "__main__":
    main()
