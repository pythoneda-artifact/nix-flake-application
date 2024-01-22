# vim: set fileencoding=utf-8
"""
pythoneda/artifact/nix/flake/application/git_artifact_app.py

This file defines the NixFlakeArtifactApp class.

Copyright (C) 2023-today rydnr's pythoneda-artifact/nix-flake-application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.artifact.nix.flake.infrastructure import NixFlakeGitRepo
from pythoneda.shared.application import PythonEDA


class NixFlakeArtifactApp(PythonEDA):
    """
    Runs the domain of NixFlake artifacts.

    Class name: NixFlakeArtifactApp

    Responsibilities:
        - Runs the domain of NixFlake artifacts.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new NixFlakeArtifactApp instance.
        """
        # nix_flake_artifact_banner is automatically generated by pythoneda-artifact-def/nix-flake-application
        try:
            from pythoneda.artifact.nix.flake.application.nix_flake_artifact_banner import (
                NixFlakeArtifactBanner,
            )

            banner = NixFlakeArtifactBanner()
        except ImportError:
            banner = None
        super().__init__(banner, __file__)

    def accept_github_token(self, token: str):
        """
        Specifies the Github token.
        :param token: Such token.
        :type token: str
        """
        NixFlakeGitRepo.github_token(token)


if __name__ == "__main__":
    asyncio.run(
        NixFlakeArtifactApp.main(
            "pythoneda.artifact.nix.flake.application.NixFlakeArtifactApp"
        )
    )
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End: