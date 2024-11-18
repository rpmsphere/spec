%undefine _debugsource_packages

Summary: A general purpose object oriented programming language
Name: zkl
Version: 1.14.7
Release: 1
License:  zlib/libpng License
Group: Development/Languages
Source: https://www.zenkinetic.com/Documents/zkl_vm_src.zip
URL: https://www.zenkinetic.com/zkl.html

%description
It is imperative but borrows concepts from many programming paradigms,
including functional and prototype based. It is curly-bracketed, dynamic,
reflective, and threaded. It has built in garbage collection, strings, lists,
dictionaries, threads, fibers (continuations and co-routines) and more.
The syntax strongly resembles the C programming language while the data model
is closer to that of Python and Smalltalk.

%prep
%setup -q -n ZKL
sed -i '43s|//||' VM/sfmt.c

%build
export CFLAGS="-std=c90"
make -C VM %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 Bin/%{name} %{buildroot}%{_bindir}/%{name}

%files 
%doc VM/*.txt
%{_bindir}/%{name}

%changelog
* Sun Mar 21 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.14.7
- Rebuilt for Fedora
