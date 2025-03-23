{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
	packages = with pkgs; [
		python312Full
		portaudio
		alsa-lib
		python312Packages.pyaudio
		python312Packages.numpy
		python312Packages.soundcard
	];
}
