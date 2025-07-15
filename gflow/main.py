import typer
from gflow.commands import (
     gpush,
    gnew_branch, gfix_push,
    greset_hard, gclone_setup,
    ginit_template
)

app = typer.Typer(help="⚡ Simplify Git workflows with one-liner automations.")

# app.command()(ginit.ginit)
# app.command()(gssh_setup.gssh_setup)
app.command()(gpush.gpush)
app.command()(gnew_branch.gnew_branch)
app.command()(gfix_push.gfix_push)
app.command()(greset_hard.greset_hard)
app.command()(gclone_setup.gclone_setup)
app.command()(ginit_template.ginit_template)

if __name__ == "__main__":
    app()
