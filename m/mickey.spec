Name: mickey
Summary: An interpreter for R7RS Scheme written in pure C++
Version: 0.1
Release: 5.1
Group: Development/Language
License: LGPLv2.1
URL: https://github.com/cslarsen/mickey-scheme
Source0: %{name}-scheme-master.zip
BuildRequires: readline-devel

%description
Mickey Scheme is an incomplete, slow and buggy implementation of R7RS Scheme small.
The current project goals are to:
* Provide a correct and complete implementation of R7RS-small (WG1)
* Emphasize clarity and simplicity in the implementation
* Be a powerful platform for experimentation and creation of a more advanced scheme compiler.

%prep
%setup -q -n %{name}-scheme-master

%build
./autogen.sh
%configure
make

%install
%make_install

%files
%doc TODO README.md LICENSE COPYING AUTHORS
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_includedir}/%{name}
%{_datadir}/%{name}

%changelog
* Mon Oct 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
