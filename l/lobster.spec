%undefine _debugsource_packages

Summary: The Lobster Programming Language
Name: lobster
Version: 2023.11
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

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%{_bindir}/%{name}
%{_datadir}/Lobster
%{_docdir}/Lobster

%changelog
* Sun Sep 17 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2023.11
- Rebuilt for Fedora
