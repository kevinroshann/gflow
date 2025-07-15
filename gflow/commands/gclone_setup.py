import os
import typer
import subprocess
from gflow.commands.utils import run

def gclone_setup(repo_url: str = typer.Argument(..., help="Git repository URL")):
    typer.echo(f"🔗 Cloning repository: {repo_url}")
    run(f"git clone {repo_url}")

    # Extract repo name from URL
    repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
    typer.echo(f"📁 Entering repository folder: {repo_name}")
    os.chdir(repo_name)

    typer.echo("🔍 Detecting current branch...")
    result = subprocess.run("git rev-parse --abbrev-ref HEAD", shell=True, capture_output=True, text=True)
    current_branch = result.stdout.strip()
    typer.echo(f"📍 You are on branch: {current_branch}")

    typer.echo("📡 Pulling latest changes...")
    run("git pull")

    typer.secho("✅ Repository cloned and set up successfully!", fg=typer.colors.GREEN)
