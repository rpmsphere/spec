Name: teapot
Summary: Table Editor And Planner, Or: Teapot!
Version: 2.3.0
Release: 10.1
Group: Editor
License: GPLv3
URL: https://www.syntax-k.de/projekte/teapot/
Source0: https://www.syntax-k.de/projekte/%{name}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: fltk-devel
BuildRequires: fltk-static
BuildRequires: ncurses-devel
BuildRequires: lyx
BuildRequires: python
BuildRequires: latex2html
BuildRequires: libtirpc-devel

%description
A spread sheet program for UNIX. The current release has the following features:
o  curses based user interface with easy to understand menus
o  FLTK 1.3 based GUI following common user interface conventions
o  Cross-platform compatibility
o  UTF-8 support
o  portable sheet file format uses XDR or ASCII format
o  tbl, LaTeX, HTML, CSV or formatted text files can be generated and
   simple SC and WK1 sheets can be imported
o  typed expression evaluator with the types int, float, string, error,
   pointer to cell and empty
o  iterative expressions
o  powerful cell addressing
o  three-dimensional sheets
o  new expression evaluator functions can be added very easy
o  a user guide, available as PDF and HTML
o  It is still a small and simple program!

%prep
%setup -q
sed -i '14i decl {\\#include <unistd.h>} {private global\n}\n' fteapot.fl

%build
export CFLAGS="%{optflags} -I/usr/include/tirpc -ltirpc"
%cmake -DENABLE_HELP=OFF .
%cmake_build

%install
%cmake_install
install -Dm755 libteapotlib.so %{buildroot}%{_libdir}/libteapotlib.so

%files
%{_bindir}/%{name}
%{_datadir}/doc/%{name}
%{_mandir}/man1/%{name}.1.*
%{_libdir}/libteapotlib.so

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.0
- Rebuilt for Fedora
* Sun Jul 04 2010 Erk <eric.noulard@gmail.com>
- Generated by CPack RPM
