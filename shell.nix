# Prerequisites:
#
#   python -m venv .venv
#   . .venv/bin/activate
#   pip install git+https://gitlab.com/da_doomer/markdown-slides.git

# Use this file with nix-shell or similar tools; see https://nixos.org/
with import <nixpkgs> {};

mkShell {
  buildInputs = [ python3 surf ];
}
