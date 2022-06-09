# NSYNC: Notes synchronization

A single file script with minimal dependencies that produces boilerplate for daily notes into custom file formats.

## Usage

Your working directory for note-taking must contain a file named `Nsyncfile`, which contains configuration settings for the script.

## Requirements

Python 3, pandoc

## Features

Creates a new boilerplate markdown file for each day.
Option to create nested directory hierarchy.

## Philosophy

Lean: we want minimal dependencies and ease of installation.

Simple: configure the script with a single file, which also ensures that you are calling the script in the correct working directory. Avoid complicated command line arguments in favor of the config file.
