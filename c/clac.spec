%undefine _debugsource_packages

Name:     clac
Version:  0.3.3
Release:  1
Summary:  A command line, stack-based calculator with postfix notation
License:  BSD-2-Clause
Group:    Other
URL:      https://github.com/soveran/clac
Source:   %name-%version.tar.gz

%description
A command line, stack-based calculator with postfix notation that displays the
stack contents at all times. As you type, the stack changes are reflected
immediately.

%prep
%setup -q
sed -i '/STRIP/d' makefile

%build
%make_build

%install
make install PREFIX=%buildroot%_prefix

%files
%_bindir/*
%_mandir/man1/*
%doc README*

%changelog
* Thu Dec 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuilt for Fedora
* Tue Feb 27 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.3.1-alt1
- new version 0.3.1
* Thu Jun 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
