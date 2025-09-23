return { -- telescope fuzzy finder (ONLY <leader>sg changed)
    'nvim-telescope/telescope.nvim',
    event = 'vimenter',
    dependencies = {
        'nvim-lua/plenary.nvim',
        {
            'nvim-telescope/telescope-fzf-native.nvim',
            build = 'make',
            cond = function()
                return vim.fn.executable('make') == 1
            end,
        },
        'nvim-telescope/telescope-ui-select.nvim',
        { 'nvim-tree/nvim-web-devicons', enabled = vim.g.have_nerd_font },
    },
    config = function()
        local telescope = require('telescope')
        local builtin = require('telescope.builtin')

        telescope.setup {
            extensions = {
                ['ui-select'] = {
                    require('telescope.themes').get_dropdown(),
                },
            },
        }

        pcall(telescope.load_extension, 'fzf')
        pcall(telescope.load_extension, 'ui-select')

        -- helper: try to find git root starting from `startpath`
        local function find_git_root(startpath)
            if not startpath or startpath == '' then
                return nil
            end
            -- run git from the startpath so we find the nearest enclosing repo
            local cmd = 'git -C ' .. vim.fn.shellescape(startpath) .. ' rev-parse --show-toplevel 2>/dev/null'
            local out = vim.fn.systemlist(cmd)
            if vim.v.shell_error == 0 and out[1] and out[1] ~= '' then
                return out[1]
            end
            return nil
        end

        -- ORIGINAL keymaps left untouched except <leader>sg below
        vim.keymap.set('n', '<leader>sh', builtin.help_tags, { desc = '[s]earch [h]elp' })
        vim.keymap.set('n', '<leader>sk', builtin.keymaps, { desc = '[s]earch [k]eymaps' })
        vim.keymap.set('n', '<leader>sf', builtin.find_files, { desc = '[s]earch [f]iles' })
        vim.keymap.set('n', '<leader>ss', builtin.builtin, { desc = '[s]earch [s]elect telescope' })
        vim.keymap.set('n', '<leader>sw', builtin.grep_string, { desc = '[s]earch current [w]ord' })

        -- ONLY THIS MAPPING CHANGED: use buffer-dir -> git-root (if any) -> run live_grep with cwd
        vim.keymap.set('n', '<leader>sg', function()
            -- get directory of current buffer, fallback to process cwd
            local bufname = vim.api.nvim_buf_get_name(0)
            local startpath = nil
            if bufname and bufname ~= '' then
                startpath = vim.fn.fnamemodify(bufname, ':h')
            else
                startpath = vim.loop.cwd()
            end

            local git_root = find_git_root(startpath)
            if git_root then
                -- force live_grep to run inside the repo root
                builtin.live_grep({ cwd = git_root })
            else
                -- no git found: default behavior (search from cwd)
                builtin.live_grep()
            end
        end, { desc = '[s]earch by [g]rep (nearest git root from current file)' })

        vim.keymap.set('n', '<leader>sd', builtin.diagnostics, { desc = '[s]earch [d]iagnostics' })
        vim.keymap.set('n', '<leader>sr', builtin.resume, { desc = '[s]earch [r]esume' })
        vim.keymap.set('n', '<leader>s.', builtin.oldfiles, { desc = '[s]earch recent files' })
        vim.keymap.set('n', '<leader><leader>', builtin.buffers, { desc = '[ ] find existing buffers' })

        vim.keymap.set('n', '<leader>/', function()
            builtin.current_buffer_fuzzy_find(require('telescope.themes').get_dropdown {
                winblend = 10,
                previewer = false,
            })
        end, { desc = '[/] search in current buffer' })

        vim.keymap.set('n', '<leader>s/', function()
            builtin.live_grep {
                grep_open_files = true,
                prompt_title = 'live grep in open files',
            }
        end, { desc = '[s]earch [/] in open files' })

        vim.keymap.set('n', '<leader>sn', function()
            builtin.find_files { cwd = vim.fn.stdpath 'config' }
        end, { desc = '[s]earch [n]eovim files' })
    end,
}
