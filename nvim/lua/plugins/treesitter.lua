return {
    "nvim-treesitter/nvim-treesitter",
    branch = "main",
    -- Preserve the API revision from your uploaded lockfile.
    commit = "8b98b4470eb326f1c7b50dae79f8c963568e5720",
    lazy = false,
    build = ":TSUpdate",
    config = function()
        local ts = require("nvim-treesitter")
        ts.setup({ install_dir = vim.fn.stdpath("data") .. "/site" })
        local languages = {
            "c", "cpp", "lua", "vim", "vimdoc", "query", "elixir",
            "heex", "java", "haskell", "markdown", "markdown_inline",
            "javascript", "html", "css", "rust", "python",
        }
        -- Installation is asynchronous. Highlighting must tolerate unavailable parsers.
        ts.install(languages)
        local warned = {}
        vim.api.nvim_create_autocmd("FileType", {
            group = vim.api.nvim_create_augroup("SoloTreesitter", { clear = true }),
            pattern = {
                "c", "cpp", "lua", "vim", "help", "query", "elixir",
                "heex", "java", "haskell", "markdown", "javascript",
                "html", "css", "rust", "python",
            },
            callback = function(args)
                local ok, err = pcall(vim.treesitter.start, args.buf)
                local ft = vim.bo[args.buf].filetype
                if not ok and not warned[ft] then
                    warned[ft] = true
                    vim.schedule(function()
                        vim.notify("Tree-sitter (" .. ft .. "): " .. tostring(err)
                            .. "\nCheck :checkhealth nvim-treesitter; install the parser and reopen the file.",
                            vim.log.levels.WARN)
                    end)
                end
            end,
        })
    end,
}
