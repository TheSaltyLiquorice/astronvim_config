-- Mapping data with "desc" stored directly by vim.keymap.set().
--
-- Please use this mappings table to set keyboard mapping since this is the
-- lower level configuration and more robust one. (which-key will
-- automatically pick-up stored data by this setting.)
return {
  -- first key is the mode
  n = {
    -- second key is the lefthand side of the map
    -- mappings seen under group name "Buffer"
    ["<leader>bn"] = { "<cmd>tabnew<cr>", desc = "New tab" },
    ["<leader>bD"] = {
      function()
        require("astronvim.utils.status").heirline.buffer_picker(function(bufnr)
          require("astronvim.utils.buffer").close(
            bufnr)
        end)
      end,
      desc = "Pick to close",
    },
    -- tables with the `name` key will be registered with which-key if it's installed
    -- this is useful for naming menus
    ["<leader>b"] = { name = "Buffers" },
    -- quick save
    -- ["<C-s>"] = { ":w!<cr>", desc = "Save File" },  -- change description but the same command
    ["<A-j>"] = { "<cmd> :m .+1 <CR>==", desc = "Move line down" },
    ["<A-k>"] = { "<cmd> :m .-2 <CR>==", desc = "Move line up" },
  },
  i = {
    ["<A-j>"] = { "<Esc>:m .+1<CR>==gi", desc = "Move line down" },
    ["<A-k>"] = { "<Esc>:m .-2<CR>==gi", desc = "Move line up" },
  },
  v = {
    ["<A-j>"] = { ":m '>+1<CR>gv=gv", desc = "Move line down" },
    ["<A-k>"] = { ":m '<-2<CR>gv=gv", desc = "Move line up" },
  },
  t = {
    -- setting a mapping to false will disable it
    -- ["<esc>"] = false,
  },
}


-- nnoremap <A-j> :m .+1<CR>==
-- nnoremap <A-k> :m .-2<CR>==
-- inoremap <A-j> <Esc>:m .+1<CR>==gi
-- inoremap <A-k> <Esc>:m .-2<CR>==gi
-- vnoremap <A-j> :m '>+1<CR>gv=gv
-- vnoremap <A-k> :m '<-2<CR>gv=gv
