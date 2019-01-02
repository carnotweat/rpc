util that controls aria2rpc download queue        
When executing from emacs, when you start a python shell, emacs ll
tell you to run a python process first.
In regular bash shell, however, when you type python, it does both,
starts the process and launches the shell .      
Except , first is not explicit (and hence doesn't ) occur to you
untill you dig.                  
Moreover, it is 2 libraries (roughly to execute command line         
one-liners of  aria2) , followed by flags of same commands.

All the more reason for me to try solving in elisp or bash , beofre I          
touch python.Just like I seek RPC before touching any API, let alone          
calling one.Frameworks are another story            
Yes bash has portability issues,due to variety in init systems, among     
other compatibility issues, which noob customers hate and hence    
commerce  pushes away, but I d rather bear that, than the kind of    
opacity,dependency,mediocrity and technical debt, promoted in name of
**commerce**.         
Even if it comes down to sales, I d do it my way first, then
rewrite in C and if still required, python.         
That's arguably not the optimal use of workplace resources and         
certainly an issue as people compete for resource.



Pending  - Auto pause --on-download-complete="python pause $gid"| echo "Download Complete at:\n\t$3
