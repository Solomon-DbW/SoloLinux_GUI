return {
    {
        "nvim-treesitter/nvim-treesitter",
        lazy = false,
        build = ":TSUpdate",

        config = function()
            require("nvim-treesitter").setup({
                install_dir = vim.fn.stdpath("data") .. "/site",
            })

            require("nvim-treesitter").install({
                "c",
                "lua",
                "vim",
                "vimdoc",
                "query",
                "elixir",
                "heex",
                "java",
                "haskell",
                "markdown",
                "markdown_inline",
                "javascript",
                "html",
                "css",
                "cpp",
                "rust",
                "python",
            })

            vim.api.nvim_create_autocmd("FileType", {
                pattern = {
                    "c",
                    "lua",
                    "vim",
                    "vimdoc",
                    "query",
                    "elixir",
                    "heex",
                    "java",
                    "haskell",
                    "markdown",
                    "javascript",
                    "html",
                    "css",
                    "cpp",
                    "rust",
                    "python",
                },

                callback = function()
                    vim.treesitter.start()
                end,
            })
        end,
    },
}
