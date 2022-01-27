"Vimrc SovietVim
set nowrap
set nobackup

nnoremap <Space> @g

function! Curse()
	if 'X'==nr2char(strgetchar(getline('.')[col('.') - 1:], 0))
		echo "Charatere pieger ! echec de la mission "
		sleep 3
		wq
	endif
endfunction
