import os
import typer
from gflow.commands.utils import run

SSH_KEY_PATH = os.path.expanduser("~/.ssh/id_ed25519.pub")
PRIVATE_KEY_PATH = os.path.expanduser("~/.ssh/id_ed25519")

def gssh_setup(email: str = typer.Option(..., help="Your GitHub email")):
    if os.path.exists(SSH_KEY_PATH):
        typer.echo("✅ SSH key already exists at ~/.ssh/id_ed25519.pub")
    else:
        typer.echo("🔐 No SSH key found. Generating one...")
        run(f'ssh-keygen -t ed25519 -C "{email}" -f ~/.ssh/id_ed25519 -N ""')

    typer.echo("➕ Adding key to SSH agent...")
    run(f'ssh-agent bash -c "ssh-add {PRIVATE_KEY_PATH}"')

    typer.secho("\n📋 Your public SSH key is:\n", fg=typer.colors.CYAN)
    run(f"cat {SSH_KEY_PATH}")

    typer.secho("\n🔗 Copy this key and add it to your GitHub account at:", fg=typer.colors.YELLOW)
    typer.echo("   https://github.com/settings/ssh/new")

    # 👇 This line waits for the user to paste or press enter
    typer.echo("\n📥 After adding the SSH key to GitHub, paste anything and press Enter to continue...")
    _ = input("🔄 Waiting for confirmation: ")

    typer.echo("\n🧪 Testing connection to GitHub...")
    exit_code = run("ssh -T git@github.com", ignore_error=True)

    if exit_code == 1:
        typer.secho("✅ SSH key successfully authenticated with GitHub!", fg=typer.colors.GREEN)
    else:
        typer.secho("❌ Unexpected response from GitHub SSH", fg=typer.colors.RED)

