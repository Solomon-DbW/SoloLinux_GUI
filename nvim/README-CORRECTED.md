# Corrected Solomon Neovim configuration

This is your full configuration, with targeted corrections. Your theme, general UI,
Neo-tree settings, Harpoon keys, completion keys, and VimTeX setup are retained.
Lspsaga now owns breadcrumbs; the separate breadcrumbs.nvim specification is removed.

## Install (Linux)

Close Neovim. Extract nvim-corrected.zip into a temporary directory. From the directory
containing the extracted `nvim` folder, run:

```sh
mkdir -p ~/.config
if [ -e ~/.config/nvim ]; then
    mv ~/.config/nvim ~/.config/nvim.backup-$(date +%Y%m%d-%H%M%S)
fi
cp -a nvim ~/.config/nvim
nvim
```

Replace the directory rather than merging: merging leaves removed duplicate plugin
specifications active. Your existing plugin/parser data is preserved.

Run `:Lazy install` to install missing dependencies. The existing lockfile is retained
for existing plugins; newly added cmp-buffer and cmp-path have no original lock entry.
Avoid a blanket update until you have checked version compatibility.

## Version and external tools

The LSP config uses Neovim 0.11+ APIs and Mason-LSPConfig v2. Tree-sitter is pinned
explicitly to the revision in your uploaded lockfile, preserving its existing API.
The current upstream main branch has different requirements; do not unpin and update
without checking its README against your Neovim version.

Parser compilation needs a C compiler, tree-sitter CLI, curl and tar on PATH. Use
`:checkhealth nvim-treesitter` for the installed revision's exact requirements.
Mason also needs the appropriate runtimes/toolchains for each requested server.

Install external tools you use: stylua, black, chktex, latexmk, zathura, glow, yazi,
ripgrep (Telescope live grep), and Brave for OpenInBrave. A compatible JDK and jdtls
are required for Java; `:MasonInstall jdtls` installs the server, not the JDK.
Black and StyLua may also be installed via Mason. No system packages are installed
by this archive.

## Finish parser installation

Run `:TSInstall python` and wait for completion, then reopen the Python buffer.
The startup installation list remains asynchronous. While a parser is unavailable,
a warning appears once per filetype per session instead of aborting FileType.
This contains the error; it cannot repair missing build tools or incompatible parser
binaries automatically.

Check `:checkhealth nvim-treesitter`, `:checkhealth vim.lsp`, `:Mason`, and
`:checkhealth telescope`. If Python still fails, inspect:

```vim
:lua print(vim.inspect(vim.api.nvim_get_runtime_file("parser/python.*", true)))
```

Multiple paths can indicate an older parser shadowing another. Investigate the paths
before removing anything. Python's Pyright LSP and the Python Tree-sitter parser are
separate components.

## Corrections

- Guard Tree-sitter startup, use an augroup and `help` filetype, and pin its revision.
- Declare LSP dependencies; define configs before Mason setup; use ensure_installed.
- Enable configured servers, including ones installed outside Mason; exclude Java
  from Mason automatic activation because nvim-jdtls owns it.
- Add cmp-buffer/cmp-path, declare completion dependencies and wire Colorful Menu.
- Use root-derived, unique Java workspaces passed with `-data`.
- Keep one local leader and formatting mapping; prefer none-ls when available.
- Remove duplicate Colorful Menu specification and overlapping breadcrumb plugin.
- Correct Lualine dependency syntax and declare Noice/Telescope dependencies.
- Replace undefined dashboard pickers with recent files and config files.
- Align softtabstop with four-space indentation and give the theme startup priority.
- Remove stale logs, demo TeX and package-manager leftovers from the plugin folder.

## Validation limits

All packaged Lua files were syntax-checked with Lua's loadfile via texlua. Archive
integrity and key structural changes were checked. This environment has no Neovim
installation or your installed plugins/parsers; full startup, language-server launch,
plugin-version compatibility and formatter execution must be verified on your machine.
