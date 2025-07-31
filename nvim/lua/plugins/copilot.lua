return {
    "zbirenbaum/copilot.lua",
    event = "InsertEnter", -- load only when needed
    config = function()
        require("copilot").setup({
            panel = {
                enabled = false, -- disable side panel
            },
            suggestion = {
                enabled = true,
                auto_trigger = true,
                debounce = 75,
                keymap = {
                    accept = "<C-l>",
                    next = "<C-j>",
                    prev = "<C-k>",
                    dismiss = "<C-e>",
                },
            },
        })
    end,
}
