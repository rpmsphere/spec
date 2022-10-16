Name: beef
Summary: flexible Brainfuck interpreter
Version: 1.2.0
Release: 1
Group: Development/Languages
License: Free Software
URL: https://kiyuko.org/software/beef
Source0: https://kiyuko.org/software/beef/releases/%{name}-%{version}.tar.xz
BuildRequires: readline-devel
BuildRequires: cattle-devel

%description
Beef is an interpreter for the Brainfuck programming language.

Its main goals are to be comfortable for the user and to run most
Brainfuck programs unchanged; speed is generally quite good.

Beef performs thorough error checking to make sure malformed programs are
not executed; it also supports a bunch of command-line options that can be
used for configuration or compatibility purposes.

If GVFS is installed, Beef can use any available backend as either output
or (where it makes sense) input source. GNU readline is used for
interactive input.

%prep
%setup -q
mkdir build

%build
cd build
../configure --prefix=/usr
%make_build

%install
cd build
%make_install

%files
%doc COPYING *.rst
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora