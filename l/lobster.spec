%undefine _debugsource_packages

Summary: The Lobster Programming Language
Name: lobster
Version: 2024.0
Release: 1
License: Apache v2
Group: Development/Language
URL: https://strlen.com/lobster/
Source0: https://github.com/aardappel/lobster/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Lobster is a programming language that tries to combine the advantages of
static typing and compile-time memory management with a very lightweight,
friendly and terse syntax, by doing most of the heavy lifting for you.

%prep
%setup -q

%build
cd dev
cmake -DSDL_STATIC=FALSE -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=release .
sed -i 's|SDL2-static|SDL2|' CMakeFiles/lobster.dir/link.txt
make

%install
cd dev
%make_install

%files
%{_bindir}/%{name}
%{_datadir}/Lobster
%{_docdir}/Lobster

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2024.0
- Rebuilt for Fedora
