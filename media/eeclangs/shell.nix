# Use this file with nix-shell or similar tools; see https://nixos.org/
with import <nixpkgs> {};

mkShell {
    buildInputs = [ (python3.withPackages (ps: with ps; [ matplotlib ])) ];
}
