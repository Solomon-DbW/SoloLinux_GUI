return {
    "nvimdev/dashboard-nvim",
    event = "VimEnter",
    config = function()
        require("dashboard").setup({
            theme = "hyper",
            config = {
                -- header text generated using (figlet -f ANSIShadow.flf "neovim")
                header = {
                    "███╗   ██╗███████╗ ██████╗ ██╗   ██╗██╗███╗   ███╗",
                    "████╗  ██║██╔════╝██╔═══██╗██║   ██║██║████╗ ████║",
                    "██╔██╗ ██║█████╗  ██║   ██║██║   ██║██║██╔████╔██║",
                    "██║╚██╗██║██╔══╝  ██║   ██║╚██╗ ██╔╝██║██║╚██╔╝██║",
                    "██║ ╚████║███████╗╚██████╔╝ ╚████╔╝ ██║██║ ╚═╝ ██║",
                    "╚═╝  ╚═══╝╚══════╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝     ╚═╝",
                    "                                                  ",
                },
                shortcut = {
                    { desc = "󰊳 Update", group = "@property", action = "Lazy update", key = "u" },
                    {
                        icon = " ",
                        icon_hl = "@variable",
                        desc = "Files",
                        group = "Label",
                        action = "Telescope find_files",
                        key = "f",
                    },
                    {
                        desc = " Recent files",
                        group = "DiagnosticHint",
                        action = "Telescope oldfiles",
                        key = "a",
                    },
                    {
                        desc = " dotfiles",
                        group = "Number",
                        action = function()
                            require("telescope.builtin").find_files({ cwd = vim.fn.stdpath("config"), hidden = true })
                        end,
                        key = "d",
                    },
                },
            },
        })
    end,
    dependencies = { { "nvim-tree/nvim-web-devicons" } },
}
