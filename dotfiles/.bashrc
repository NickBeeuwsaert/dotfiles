PATH=$PATH:$HOME/.rvm/bin # Add RVM to PATH for scripting
PATH=$HOME/.local/bin:$PATH
#Whats this junk?
function dataURI() {
    printf "data:%s;base64,%s" `file -b --mime-type $1` `base64 $1`
}

function git_prompt () {
    local branchName=''
    local status=''
    if [ $(git rev-parse --is-inside-work-tree 2> /dev/null) ]; then
        branchName="$(git symbolic-ref --quiet --short HEAD 2> /dev/null || 
                      git rev-parse --short HEAD 2> /dev/null ||
                      echo "(unknown)")"
        #echo "on $branchName[$status]"
        echo " (on $branchName)"
    fi
}
HISTCONTROL=ignoreboth
#export PS1='\h:\W \u$(git_prompt)\$ '
PS1="\[\e[0;31m\]\u\[\e[0m\]@\[\e[0;33m\]\h\[\e[0m\]:\[\e[0;32m\]\w"'$(git_prompt)'"\$ "

while read line
do
    if [[ :$PATH: != *":$line:"* ]]; then
        PATH=$PATH:$line
    fi
done < /etc/paths
source /usr/local/bin/virtualenvwrapper.sh

alias :q='echo "Why don'"'"'t you try doing that in vim next time?"'
alias :wq=:q
alias :w=:q
