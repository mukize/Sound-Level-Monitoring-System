{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
	packages = with pkgs; [
		python312Full
		python312Packages.numpy
		python312Packages.soundcard
	];
}
