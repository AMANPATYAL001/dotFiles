" .config/nvim/init.vim"

set number
set encoding=utf-8
set wrap
syntax on
set background=dark
set smartcase
set expandtab
set incsearch
set shiftwidth=4
set cursorline

call plug#begin('~/.vim/plugged')

Plug 'morhetz/gruvbox'
Plug 'jremmen/vim-ripgrep'
Plug 'tpope/vim-fugitive'
Plug 'leafgarland/typescript-vim'
Plug 'git@github.com:Valloric/YouCompleteMe.git'
Plug 'mbbill/undotree'
Plug 'git@github.com:kien/ctrlp.vim.git'
Plug 'ycm-core/YouCompleteMe'

call plug#end()

set splitbelow
set splitright


let g:python_host_prog = '/usr/bin/python3'
let g:python3_host_prog = '/usr/bin/python3'
let g:ycm_path_to_python_interpreter="/usr/bin/python3"

nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

colorscheme gruvbox

let g:netrw_banner=0

let mapleader=" "

nnoremap <leader>h :UndotreeShow<CR>

noremap <silent> <C-Left> :vertical resize +3<CR>
noremap <silent> <C-Right> :vertical resize -3<CR>
noremap <silent> <C-Up> :resize +3<CR>
noremap <silent> <C-Down> :resize -3<CR>

map <Leader>th <C-w>t<C-w>H
map <Leader>tk <C-w>t<C-w>K

let g:python_highlight_all = 2 

hi ActiveWindow guibg=#21242b
hi InactiveWindow guibg=#282C34
set winhighlight=Normal:ActiveWindow,NormalNC:InactiveWindow
