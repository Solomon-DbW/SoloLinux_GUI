local root = require("jdtls.setup").find_root({
    "mvnw", "gradlew", "pom.xml", "build.gradle", "build.gradle.kts", ".git",
})
if not root then
    root = vim.fs.dirname(vim.api.nvim_buf_get_name(0))
end
if not root or root == "" then return end
root = vim.uv.fs_realpath(root) or root
if vim.fn.executable("jdtls") ~= 1 then
    vim.notify("Java LSP: install jdtls with :MasonInstall jdtls, then reopen this file.", vim.log.levels.WARN)
    return
end
local workspace = vim.fn.stdpath("data") .. "/jdtls-workspace/"
    .. vim.fn.fnamemodify(root, ":t") .. "-" .. vim.fn.sha256(root):sub(1, 12)
vim.fn.mkdir(workspace, "p")
require("jdtls").start_or_attach({
    cmd = { "jdtls", "-data", workspace },
    root_dir = root,
    capabilities = require("cmp_nvim_lsp").default_capabilities(),
})
