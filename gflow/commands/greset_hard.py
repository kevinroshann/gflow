import typer
import subprocess
from gflow.commands.utils import run

def greset_hard():
    typer.echo("📡 Fetching latest changes from origin...")
    run("git fetch origin")

    typer.echo("🔍 Detecting current branch...")
    result = subprocess.run(
        "git rev-parse --abbrev-ref HEAD",
        shell=True,
        capture_output=True,
        text=True
    )
    current_branch = result.stdout.strip()

    if not current_branch:
        typer.secho("❌ Could not detect current branch!", fg=typer.colors.RED)
        raise typer.Exit()

    typer.echo(f"📍 Current branch: {current_branch}")
    typer.echo(f"🧹 Resetting local branch to match origin/{current_branch}...")

    run(f"git reset --hard origin/{current_branch}")

    typer.echo("🧽 Cleaning untracked files...")
    run("git clean -fd")

    typer.secho("✅ Local branch reset and cleaned!", fg=typer.colors.GREEN)
