import typer
from gflow.commands.utils import run

def gpush(message: str = typer.Option(..., "--message", "-m", help="Commit message")):
    typer.echo("📦 Staging all changes...")
    run("git add .")

    typer.echo(f"📝 Committing with message: '{message}'")
    run(f'git commit -m "{message}"')

    typer.echo("🚀 Pushing to remote...")
    run("git push")

    typer.secho("✅ Changes pushed successfully!", fg=typer.colors.GREEN)
