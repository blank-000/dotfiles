-- [[ Basic Keymaps ]]
--  See `:help vim.keymap.set()`

-- Find and Replace word under cursor
vim.keymap.set("n", "<leader>r", function()
    local word = vim.fn.expand("<cword>")
    local escaped = vim.fn.escape(word, [[\]])
    local cmd = string.format(":%s%%s/\\V%s//g", "", escaped)
    vim.api.nvim_feedkeys(vim.api.nvim_replace_termcodes(cmd, true, false, true), "n", false)
    vim.api.nvim_feedkeys(vim.api.nvim_replace_termcodes("<Left><Left>", true, false, true), "n", false)
end, { desc = "Find and replace word under cursor" })

-- Open url under cursor in the default web browser
vim.keymap.set("n", "<leader><CR>", function()
    local url = vim.fn.expand("<cfile>")
    if not url:match("^https?://") then
        vim.notify("Not a valid URL: " .. url, vim.log.levels.WARN)
        return
    end
    vim.fn.jobstart({ "xdg-open", url }, { detach = true })
end, { desc = "Open URL under cursor" })

-- Clear highlights on search when pressing <Esc> in normal mode
--  See `:help hlsearch`
vim.keymap.set('n', '<Esc>', '<cmd>nohlsearch<CR>')

-- faster exlpore mode
vim.keymap.set("n", "<leader>e", vim.cmd.Ex)

-- Lazy shortcut
vim.keymap.set('n', '<leader>l', vim.cmd.Lazy)
-- Diagnostic keymaps
vim.keymap.set('n', '<leader>q', vim.diagnostic.setloclist, { desc = 'Open diagnostic [Q]uickfix list' })

-- Keybinds to make split navigation easier.
--  Use CTRL+<hjkl> to switch between windows
vim.keymap.set('n', '<C-h>', '<C-w><C-h>', { desc = 'Move focus to the left window' })
vim.keymap.set('n', '<C-l>', '<C-w><C-l>', { desc = 'Move focus to the right window' })
vim.keymap.set('n', '<C-j>', '<C-w><C-j>', { desc = 'Move focus to the lower window' })
vim.keymap.set('n', '<C-k>', '<C-w><C-k>', { desc = 'Move focus to the upper window' })

-- Normal mode move current line up/down
vim.keymap.set('n', '<S-A-j>', ':move+1<CR>', { desc = 'Move line up' })
vim.keymap.set('n', '<S-A-k>', ':move-2<CR>', { desc = 'Move line down' })

-- Visual mode: Move selection down/up
vim.keymap.set('v', '<S-A-j>', ":m '>+1<CR>gv=gv", { desc = 'Move selection down' })
vim.keymap.set('v', '<S-A-k>', ":m '<-2<CR>gv=gv", { desc = 'Move selection up' })
