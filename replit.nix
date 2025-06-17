{ pkgs }: {
  deps = [
    pkgs.python39Full
    pkgs.python39Packages.uvicorn
    pkgs.python39Packages.fastapi
    pkgs.python39Packages.httpx
    pkgs.python39Packages.python-dotenv
    pkgs.python39Packages.pillow
  ];
}
