from pathlib import Path

from jinja2 import Environment, FileSystemLoader
import markdown
import yaml

PROJECTS_DIR = Path("projects")
EXPERIENCE_DIR = Path("experience")
TEMPLATE_DIR = Path("templates")
OUTPUT_DIR = Path("docs")
OUTPUT_PATH = Path("index.html")
BLOG_DIR = Path("blog")


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


def parse_blog_posts():
    """Parses .md files in blog directory and renders blog .html"""

    md_parser = markdown.Markdown(extensions=["meta", "fenced_code"])
    blog_list = []
    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)
    template = env.get_template("blog_post_template.html")

    for blog in BLOG_DIR.iterdir():
        if blog.is_file():
            try:
                with open(blog, "r") as f:
                    blog_md = f.read()

                md_parser.reset()

                post_html = md_parser.convert(blog_md)
                post_title = md_parser.Meta.get("title")[0]
                post_date = md_parser.Meta.get("date")[0]
                post_description = md_parser.Meta.get("description")[0]
                post_number = int(md_parser.Meta.get("number", [0])[0])

                blog_file = f"{post_title.replace(' ', '-').lower()}.html"

                OUTPUT_DIR.mkdir(exist_ok=True)
                blog_content = {
                    "content": post_html,
                    "title": post_title,
                    "date": post_date,
                }
                rendered_blog = template.render(blog_content)

                with open(Path(OUTPUT_DIR, blog_file), "w") as f:
                    f.write(rendered_blog)

                post_metadata = {
                    "title": post_title,
                    "date": post_date,
                    "description": post_description,
                    "number": post_number,
                    "file": blog_file,
                }

                blog_list.append(post_metadata)

            except Exception:
                continue

    blog_list = sorted(blog_list, key=lambda x: x["number"], reverse=True)

    return blog_list


def render_index(experience_list, project_list, blog_list):
    """Renders index.html with project and experience information"""
    file_loader = FileSystemLoader(TEMPLATE_DIR)
    env = Environment(loader=file_loader)

    template = env.get_template("index_template.html")
    context = {
        "experience_list": experience_list,
        "project_list": project_list,
        "blog_list": blog_list,
    }

    rendered_html = template.render(context)

    with open(Path(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(rendered_html)


def main():
    """Runs the .html generator"""
    experience_list = parse_experience()
    project_list = parse_projects()
    blog_list = parse_blog_posts()
    render_index(
        experience_list=experience_list, project_list=project_list, blog_list=blog_list
    )


if __name__ == "__main__":
    main()
