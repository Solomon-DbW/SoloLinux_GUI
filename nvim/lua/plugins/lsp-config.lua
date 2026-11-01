return {
    "neovim/nvim-lspconfig",
    lazy = false,
    dependencies = {
        { "mason-org/mason.nvim", opts = {} },
        "mason-org/mason-lspconfig.nvim",
        "hrsh7th/cmp-nvim-lsp",
    },
    config = function()
        local capabilities = require("cmp_nvim_lsp").default_capabilities()
        local servers = {
            tailwindcss = {},
            hls = {
                filetypes = { "haskell", "lhaskell" },
                settings = { haskell = {
                    formattingProvider = "ormolu",
                    plugin = { hlint = { globalOn = true } },
                } },
            },
            texlab = {},
            lua_ls = { settings = { Lua = {
                diagnostics = { globals = { "vim" } },
                workspace = { checkThirdParty = false },
            } } },
            pyright = {},
        }
        local names = {}
        for name, config in pairs(servers) do
            config.capabilities = vim.deepcopy(capabilities)
            vim.lsp.config(name, config)
            names[#names + 1] = name
        end
        -- Configs exist before Mason enables any installed servers.
        require("mason-lspconfig").setup({
            ensure_installed = names,
            -- Java is managed exclusively by ftplugin/java.lua.
            automatic_enable = { exclude = { "jdtls" } },
        })
        -- Also enable these configs for executables installed outside Mason.
        vim.lsp.enable(names)
        vim.diagnostic.config({
            virtual_text = { prefix = "󱈸", spacing = 2 },
            signs = true, underline = true,
            update_in_insert = true, severity_sort = true,
        })
        vim.api.nvim_create_autocmd("LspAttach", {
            group = vim.api.nvim_create_augroup("SoloLspMappings", { clear = true }),
            callback = function(args)
                local function map(lhs, rhs, desc)
                    vim.keymap.set("n", lhs, rhs, { buffer = args.buf, desc = "LSP: " .. desc })
                end
                map("K", vim.lsp.buf.hover, "Documentation")
                map("<leader>gd", vim.lsp.buf.definition, "Definition")
                map("<leader>gr", vim.lsp.buf.references, "References")
                map("<leader>ca", vim.lsp.buf.code_action, "Code action")
                map("<leader>rn", vim.lsp.buf.rename, "Rename")
                map("<leader>gf", function()
                    local bufnr = vim.api.nvim_get_current_buf()
                    local clients = vim.lsp.get_clients({ bufnr = bufnr })
                    local use_null_ls = false
                    for _, client in ipairs(clients) do
                        if client.name == "null-ls" and client:supports_method("textDocument/formatting", bufnr) then
                            use_null_ls = true
                            break
                        end
                    end
                    vim.lsp.buf.format({
                        bufnr = bufnr, timeout_ms = 5000,
                        filter = function(client)
                            return not use_null_ls or client.name == "null-ls"
                        end,
                    })
                end, "Format document")
            end,
        })
    end,
}
