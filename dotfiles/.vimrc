set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
Plugin 'airblade/vim-gitgutter'
Plugin 'mattn/emmet-vim'
Plugin 'kien/ctrlp.vim'
Plugin 'scrooloose/syntastic'
"Plugin 'pangloss/vim-javascript'
Plugin 'tpope/vim-liquid'
Plugin 'tpope/vim-dispatch'
Plugin 'terryma/vim-multiple-cursors'
Plugin 'joonty/vdebug.git'
Plugin 'scrooloose/nerdtree'
call vundle#end()

filetype plugin on

set ruler

set shiftwidth=4
set tabstop=4
set expandtab
set incsearch
set hlsearch

autocmd FileType make setlocal noexpandtab
highlight clear SignColumn
set backspace=indent,eol,start

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

let g:syntastic_cpp_compiler_options = '-std=c++11'

noremap <F8> :Make<CR>

"set makeprg=scons\ -u\ \.

syntax on
