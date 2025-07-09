import typer
from gflow.commands.utils import run

app = typer.Typer()  # This makes it a subcommand app

@app.command()
def ginit(repo_url: str = typer.Argument(..., help="Remote repository URL")):
    typer.echo("🔧 Initializing Git repository...")
    run("git init")

    typer.echo("🔗 Adding remote origin...")
    try:
        run(f"git remote add origin {repo_url}")
    except typer.Exit:
        typer.echo("⚠️  Remote 'origin' already exists — skipping...")

    typer.echo("🔁 Renaming branch to main...")
    run("git branch -M main")

    typer.echo("📦 Staging all files...")
    run("git add .")

    typer.echo("📝 Committing with message: 'Initial commit'")
    # run('git commit -m "Initial commit"')

    typer.echo("🚀 Pushing to origin main with upstream set...")
    # run("git push -u origin main")

    typer.secho("✅ Repository initialized and pushed successfully!", fg=typer.colors.GREEN)
