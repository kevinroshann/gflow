import typer
from gflow.commands import init,ssh_setup,gpush  # This is the module, not the function
from gflow.commands import gnew_branch
from gflow.commands import gfix_push
app = typer.Typer()
app.command()(gpush.gpush)

app.command()(gfix_push.gfix_push)

app.command()(gnew_branch.gnew_branch)

app.command()(ssh_setup.gssh_setup)

# Register the `init.app` sub-app with the command name `ginit`
app.add_typer(init.app, name="ginit")

def run():
    app()

if __name__ == "__main__":
    run()
