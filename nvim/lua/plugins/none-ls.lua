return {
    "nvimtools/none-ls.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
        local null_ls = require("null-ls")
        null_ls.setup({ sources = {
            null_ls.builtins.formatting.stylua,
            null_ls.builtins.formatting.black,
            null_ls.builtins.diagnostics.chktex,
        } })
        -- Formatting keymap is defined once in lsp-config.lua.
    end,
}
