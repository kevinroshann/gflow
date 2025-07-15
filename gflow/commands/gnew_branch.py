import typer
from gflow.commands.utils import run

def gnew_branch(
    branch: str = typer.Argument(..., help="New branch name"),
    message: str = typer.Option(..., "--message", "-m", help="Commit message"),
):
    typer.echo(f"🌱 Creating and switching to branch: {branch}")
    run(f"git checkout -b {branch}")

    typer.echo("📦 Staging all changes...")
    run("git add .")

    typer.echo(f"📝 Committing with message: '{message}'")
    run(f'git commit -m "{message}"')

    typer.echo("🚀 Pushing new branch to origin...")
    run(f"git push -u origin {branch}")

    typer.secho(f"✅ Branch '{branch}' created and pushed successfully!", fg=typer.colors.GREEN)
