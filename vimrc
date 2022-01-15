"Vimrc SovietVim
set nowrap
set nobackup

nnoremap <Space> @g
autocmd BufReadPost *
     \ if line("'\"") > 0 && line("'\"") <= line("$") |
     \   exe "normal! g`\"" |
     \ endif

function! Curse()
	if 'h'==nr2char(strgetchar(getline('.')[col('.') - 1:], 0))
		!echo "merde"
		wq
	endif
endfunction
