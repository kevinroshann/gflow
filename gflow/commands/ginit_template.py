import typer
from gflow.commands.utils import run
from pathlib import Path

def ginit_template(
    name: str = typer.Argument(..., help="Project name for README"),
):
    typer.echo("📦 Initializing Git repository...")
    run("git init")

    # Create README.md
    typer.echo("📝 Creating README.md...")
    Path("README.md").write_text(f"# {name}\n\nProject created with gflow 🚀\n")

    # Create .gitignore
    typer.echo("⚙️ Creating .gitignore...")
    Path(".gitignore").write_text(
        """# Python
__pycache__/
*.py[cod]
*.egg-info/
.env
"""
    )

    # Create LICENSE (MIT)
    typer.echo("📄 Creating MIT LICENSE...")
    Path("LICENSE").write_text(
        """MIT License

Copyright (c) 2025 Kevin

Permission is hereby granted, free of charge, to any person obtaining a copy...
(full MIT license here)
"""
    )

    typer.echo("📥 Staging files...")
    run("git add .")

    typer.echo('📝 Committing initial files...')
    run('git commit -m "chore: initialize project with template files"')

    typer.secho("✅ Project initialized with README, .gitignore, and LICENSE!", fg=typer.colors.GREEN)
