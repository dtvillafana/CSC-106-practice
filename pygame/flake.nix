{
  description = "pygame dev flake";
  inputs = {
    nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs =
    {
      nixpkgs,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python-env = (
          pkgs.python3.withPackages (
            ps: with ps; [
              pygame
              black
            ]
          )
        );
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            python-env
          ];
        };
      }
    );
}

