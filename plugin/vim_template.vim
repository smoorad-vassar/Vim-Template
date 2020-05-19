let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')
python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import plugin
EOF

function! DefaultTemplate()
  python3 plugin.default_template()
endfunction

function! CustomTemplate(template)
   python3 plugin.custom_template()
endfunction

command! -nargs=0 DefaultTemplate call DefaultTemplate()
command! -nargs=1 CustomTemplate call CustomTemplate(<f-args>)
