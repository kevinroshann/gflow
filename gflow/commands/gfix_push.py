import typer
from gflow.commands.utils import run

def gfix_push():
    typer.echo("📦 Staging all changes...")
    run("git add .")

    typer.echo("🛠 Amending last commit (without editing message)...")
    run("git commit --amend --no-edit")

    typer.echo("🚀 Force pushing to remote...")
    run("git push --force")

    typer.secho("✅ Commit amended and force-pushed!", fg=typer.colors.GREEN)
