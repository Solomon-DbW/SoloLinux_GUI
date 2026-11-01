return {
    "hrsh7th/nvim-cmp",
    event = "InsertEnter",
    dependencies = {
        "hrsh7th/cmp-nvim-lsp",
        "hrsh7th/cmp-buffer",
        "hrsh7th/cmp-path",
        { "L3MON4D3/LuaSnip", dependencies = { "rafamadriz/friendly-snippets" } },
        "saadparwaiz1/cmp_luasnip",
        "xzbdmw/colorful-menu.nvim",
    },
    config = function()
        local cmp = require("cmp")
        require("luasnip.loaders.from_vscode").lazy_load()
        cmp.setup({
            snippet = { expand = function(args) require("luasnip").lsp_expand(args.body) end },
            window = {
                completion = cmp.config.window.bordered(),
                documentation = cmp.config.window.bordered(),
            },
            mapping = cmp.mapping.preset.insert({
                ["<C-b>"] = cmp.mapping.scroll_docs(-4),
                ["<C-f>"] = cmp.mapping.scroll_docs(4),
                ["<C-Space>"] = cmp.mapping.complete(),
                ["<C-e>"] = cmp.mapping.abort(),
                ["<CR>"] = cmp.mapping.confirm({ select = true }),
            }),
            formatting = {
                format = function(entry, item)
                    -- Fall back to normal labels if a language parser is unavailable.
                    local ok, info = pcall(require("colorful-menu").cmp_highlights, entry)
                    if ok and info then
                        item.abbr_hl_group = info.highlights
                        item.abbr = info.text
                    end
                    return item
                end,
            },
            sources = cmp.config.sources({
                { name = "nvim_lsp" }, { name = "luasnip" }, { name = "path" },
            }, { { name = "buffer" } }),
        })
    end,
}
