import subprocess
import typer

def run(command: str, ignore_error: bool = False):
    typer.echo(f"📦 Running: {command}")
    result = subprocess.run(command, shell=True)

    if result.returncode != 0 and not ignore_error:
        typer.secho(f"❌ Command failed: {command}", fg=typer.colors.RED)
        raise typer.Exit(code=result.returncode)

    return result.returncode
