import subprocess
import typer

def run(command: str):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        typer.secho(f"❌ Command failed: {command}", fg=typer.colors.RED)
        raise typer.Exit(code=result.returncode)
