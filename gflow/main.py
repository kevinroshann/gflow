import typer
from gflow.commands import init  # This is the module, not the function

app = typer.Typer()

# Register the `init.app` sub-app with the command name `ginit`
app.add_typer(init.app, name="ginit")

def run():
    app()

if __name__ == "__main__":
    run()
